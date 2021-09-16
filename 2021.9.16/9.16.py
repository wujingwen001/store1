info = '''==============================================
|------------中国工商银行账户管理系统------------|
|------------1、开户              ------------|
|------------2、存钱              ------------|
|------------3、取钱              ------------|
|------------4、转账              ------------|
|------------5、查询              ------------|
|------------6、退出              ------------|
=============================================='''
print(info)
import random
import pymysql
UserID=[]



# {'Frank': {'account': 15394946, 'password': '123456', 'country': '中国', 'province': '北京', 'street': '起码路', 'door': '001', 'money': 0, 'bank_name': '工商银行起码路分行'}}
bank_name = "工商银行起码路分行"
def con_mysql():
    con=pymysql.connect(host="localhost",user='root',password='',database='bank')
    cursor = con.cursor()
    return con,cursor
def get_UserID(cursor):
    sql="select username from user"
    cursor.execute(sql)
    data=cursor.fetchall()
    for i in data:
        UserID.append(i[0])
def close(con,cursor):
    cursor.close()
    con.close()


#                 一一对应  ，  不是名称对应
def bank_adduser(add_info):
    con, cursor = con_mysql()
    get_UserID(cursor)
    if len(UserID) > 100: return 3  # bank_adduer=3
    if add_info['username'] in UserID: return 2 # bank_adduer=2
    sql = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [add_info['account'], add_info['username'], add_info['password'], add_info['country'],
             add_info['province'], add_info['street'], add_info['door'],add_info['registerDate'],bank_name,add_info['money']]

    cursor.execute(sql, param)
    con.commit()
    close(con, cursor)
    return 1



def adduser():
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    registerDate = input("\t\t请输入您的注册日期：")
    account = random.randint(10000000, 99999999)
    add_info = {'account': account, 'username': username, 'password': password, 'country': country,
                'province': province,
                'street': street, 'door': door, 'registerDate': registerDate, 'money': 0}
    status = bank_adduser(add_info)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    注册日期：%s
                    开户行名称：%s
                    余额：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door,registerDate, bank_name, add_info["money"]))
    elif status == 2:
        print("用户已存在")
    else:
        print("用户库已满")


def save(username, money1):
    con, cursor = con_mysql()
    get_UserID(cursor)
    print(UserID)
    if username not in UserID:
        return False
    else:
        sql = "select money from user where username=%s"
        param = [username]
        cursor.execute(sql, param)
        money = cursor.fetchall()
        sql1 = "update user set money=%s where username=%s"
        param1 = [money[0][0] + money1, username]
        cursor.execute(sql1, param1)
        con.commit()
        close(con, cursor)
        return True


def save1():
    username = input("请输入用户名")
    money = int(input("请输入您的存款金额"))
    status = save(username, money)
    if status == True:
        if money < 0:
            print("非法")

        else:
            print("存OK")
            # print(UserID)
    else:
        print("用户名不对")
def get(username, password, money):
    con,cursor=con_mysql()
    get_UserID(cursor)
    print(UserID)
    if username not in UserID:
        return 1
    else:
        sql = "select password,money from user where username=%s"
        param = [username]
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if password != data[0][0]:
            return 2
        else:
            if money > data[0][1] or money <= 0:
                return 3
            else:
                sql1 = "update user set money=%s where username=%s"
                param1 = [data[0][1] - money, username]
                cursor.execute(sql1, param1)
                con.commit()
                close(con, cursor)
                return 0

def get1():
    username = input("请输入用户名")
    password = input("请输入您的密码")
    money = int(input("请输入您的取款金额"))
    status = get(username, password, money)
    if status == 0:
        print("取钱成功")

    elif status == 3:
        print("金额不正常")

    elif status == 2:
        print("您的密码不正确")
    else:
        print("用户不存在")


def transfer(username, password, username1, money):
    con, cursor = con_mysql()
    get_UserID(cursor)
    sql = "select password,money from user where username=%s"
    param = [username]
    cursor.execute(sql, param)
    OUT_data = cursor.fetchall()
    sql1 = "select money from user where username=%s"
    param1 = [username1]
    cursor.execute(sql1, param1)
    IN_data = cursor.fetchall()
    if username not in UserID or username1 not in UserID:
        return 1
    else:
        if password == OUT_data[0][0]:
            if OUT_data[0][1] >= money > 0:
               sql2="update user set money=%s where username=%s"
               param2=[OUT_data[0][1]-money,username]
               cursor.execute(sql2,param2)
               sql3="update user set money=%s where username=%s"
               param3=[IN_data[0][0]+money,username1]
               cursor.execute(sql3,param3)
               con.commit()
               close(con,cursor)
               return 0
            else:
                return 3
        else:
            return 2


def transfer1():
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    username1 = input("请输入您要转账的用户名")
    money = int(input("请输入您要转的金额"))
    status = transfer(username, password, username1, money)
    if status == 0:
        print("转出OK")
    elif status == 1:
        print("用户不存在")
    elif status == 2:
        print("您的密码不对")
    else:
        print("金额不够")


def select(username, password):
    con, cursor = con_mysql()
    get_UserID(cursor)
    if username not in UserID:
        return 1
    else:
        sql = "select * from user where username=%s"
        param = [username]
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if password == data[0][2]:
            return 0
        else:
            return 2


def select1():

    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    status = select(username, password)
    if status == 1:
        print("该用户不存在")
    elif status == 0:
        con, cursor = con_mysql()
        get_UserID(cursor)
        sql = "select * from user where username=%s"
        param = [username]
        cursor.execute(sql, param)
        data = cursor.fetchall()
        print("查询成功，下面是您的账户信息：")
        info = '''
                                ------------个人信息------------
                                用户名:%s
                                账号：%s
                                密码：********
                                国籍：%s
                                省份：%s
                                街道：%s
                                门牌号：%s
                                余额：%s
                                开户行名称：%s
                            '''
        print(info % (username, data[0][0], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][8]))
        close(con, cursor)
    else:
        print("您的密码错误,请重新输入")


while True:
    begin = input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    elif begin == "2":
        print("2、存钱")
        save1()
    elif begin == "3":
        print("3、取钱")
        get1()
    elif begin == "4":
        print("4、转账")
        transfer1()
    elif begin == "5":
        print("5、查询 ")
        select1()
    elif begin == "6":
        print("6、退出")
        break