import datetime
from flask import Flask, render_template, request, redirect, flash, session, g
from application import *

# 使用Flask 对象创建一个app 对象
app = Flask(__name__)
app.secret_key = 'foifjigioojgio'
app.permanent_session_lifetime = datetime.timedelta(seconds=20*60)

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def login():
    session.permanent = True
    # 登录的功能
    # return '需要实现登录的逻辑'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 服务器接收到账号后链接数据库，校验密码
        print('从服务器接收到的数据：', username, password)
        result = verify(username, password)
        if result == 1:
            session['user_name'] = username
            # 登录成功后，跳转到管理页面
            return redirect('/home')
        else:
            flash('用户名或密码错误！')
            return redirect('/')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 注册账号，并与数据库已有数据做对比
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 服务器接收到账号后链接数据库，校验密码
        print('从服务器接收到的数据：', username, password)
        result = register_sql(username, password)
        if result == 1:
            # 登录成功后，跳转到管理页面
            flash('注册成功！')
            return redirect('/')
        else:
            flash('用户已存在！')
            return redirect('/register')
    return render_template('register.html')


@app.route('/home')
def home():
    if hasattr(g, 'user'):
        print(g.user)
    context = {
        'user': g.user
    }
    # print(g.user)
    return render_template('home.html', **context)

@app.route('/read')
def read():
    return render_template('read.html')

@app.before_request
def before_request():
    user_name = session.get('user_name')
    if user_name:
        g.user = user_name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6900)
