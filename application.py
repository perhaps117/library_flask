import pymysql
'''
链接数据库实现用户账户验证和注册
'''
def verify(user, password):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='728411552', database='library_user')
    # 创建yo
    cur = conn.cursor()
    # 验证账户和密码，返回结果
    params = [user, password]
    sql = 'select * from user where username = %s and u_password = %s'
    ret = cur.execute(sql, params)
    cur.close()
    conn.close()
    if ret == 1:
        # 1代表账户和密码正确，可以登录，0表示错误
        print('登录成功')
        return 1
    else:
        print('账号或密码错误')
        return 0


def register_sql(user, password):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='728411552', database='library_user')
    # 创建yo
    cur = conn.cursor()
    params = [user, password]
    # 判断用户是否重复
    sql_request = 'select * from user where username = %s'
    ret1 = cur.execute(sql_request, params[0])
    if ret1 == 1:
        # 0表示用户已存在, 1表示注册成功
        print('用户已存在')
        cur.close()
        conn.close()
        return 0
    else:
        sql_insert = 'insert into user values(null, %s, %s)'
        ret = cur.execute(sql_insert, params)
        print('注册成功')
        conn.commit()
        cur.close()
        conn.close()
        return 1

if __name__ == '__main__':
    re = verify('10496321', 'boe123456')
    print(re)
    new_user = register_sql(' ', ' ')
    print(new_user)

