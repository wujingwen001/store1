info='''==============================================
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
bank={'Frank': {'account': 15394946, 'password': '123456', 'country': '中国', 'province': '北京', 'street': '起码路', 'door': '001', 'money': 0, 'bank_name': '工商银行起码路分行'}}
#{'Frank': {'account': 15394946, 'password': '123456', 'country': '中国', 'province': '北京', 'street': '起码路', 'door': '001', 'money': 0, 'bank_name': '工商银行起码路分行'}}
bank_name="工商银行起码路分行"
#                 一一对应  ，  不是名称对应
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100 :return 3#bank_adduer=3
    if username in bank:return 2#bank_adduer=2
    bank[username]={
        "account": account,#键：你输入的值account=random.randint(10000000,99999999)
        "password": password,# password = input("请输入您的密码")
        "country": country,#country = input("\t\t请输入您的国家")
        "province": province,
        "street": street,
        "door": door,
        "money":0,
        "bank_name":bank_name
    }
    print(bank)
    return 1#bank_adduer=1
def adduser():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    status=bank_adduser(account,username,password,country,province,street,door)
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
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif status == 2:
        print("用户已存在")
    else:
        print("用户库已满")




def save(username,money):
     if username not in bank:
         return False
     else:
         bank[username]["money"] =bank[username]["money"]+money
         return True
def save1():
    username=input("请输入用户名")
    money=int(input("请输入您的存款金额"))
    status=save(username,money)
    if status==True:
        if money<0:
            print("非法")

        else:
             print("存OK")
             print(bank)
    else:
        print("用户名不对")



def get(username,password,money):
    if username not in bank:
        return 1
    else:
        if password==bank[username]["password"] and  0<money <=bank[username]["money"]:

            bank[username]["money"] = bank[username]["money"] - money
            return 0
        else:
            if money > bank[username]["money"] or money<=0:
                return 3
            else:
                if password!=bank[username]["password"]:
                    return 2


def get1():
    username=input("请输入用户名")
    password=input("请输入您的密码")
    money = int(input("请输入您的取款金额"))
    status=get(username,password,money)
    if status == 0:
         print("取钱成功")
         print(bank)

    elif status == 3:
         print("金额不正常")

    elif status == 2:
         print("您的密码不正确")
    else:
         print("用户不存在")

def transfer(username,password,username1,money):
    if username not in bank or username1 not in bank:
        return 1
    else:
           if password==bank[username]["password"]:
              if bank[username]["money"]>=money>0:
                bank[username]["money"]=bank[username]["money"]-money
                bank[username1]["money"]=bank[username1]["money"]+money
                return 0
              else:
                  return 3
           else:
             return 2


def transfer1():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    username1= input("请输入您要转账的用户名")
    money=int(input("请输入您要转的金额"))
    status=transfer(username,password,username1,money)
    if status==0:
        print("转出OK")
    elif status==1:
        print("用户不存在")
    elif status==2:
        print("您的密码不对")
    else:
        print("金额不够")
def select(username,password):
    if username not in bank:
        return 1
    else:
        if password==bank[username]["password"]:
            return 0
        else:
            return 2

def select1():
    username=input("请输入您的用户名")
    password=input("请输入您的密码")
    status=select(username,password)
    if status==1:
        print("该用户不存在")
    elif status==0:
        print(bank[username])
    else:
        print("您的密码错误")




while True:
    begin=input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、存钱")
        save1()
    elif  begin == "3":
        print("3、取钱")
        get1()
    elif  begin == "4":
        print("4、转账")
        transfer1()
    elif  begin == "5":
        print("5、查询 ")
        select1()
    elif  begin == "6":
        print("6、退出")
        break

