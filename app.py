from flask import Flask, render_template, request, redirect

# 使用Flask 对象创建一个app 对象
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 登录的功能
    # return '需要实现登录的逻辑'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 服务器接收到账号后链接数据库，校验密码
        print('从服务器接收到的数据：', username, password)
        # 登录成功后，跳转到管理页面
        return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
