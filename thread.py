'''
    抢票：
        需求：
            全局：500张票
            张三，李四，王五，同时在抢票，看谁抢的多
    xxx同时在做。
    xxx要实现多线程。
'''
# from threading import  Thread
#  全局500张票
# ticket = 20000
# import time
# class User(Thread):
#     username = "" # 用户名
#     count = 0 # 票的计数器
#
#     def run(self) -> None:
#         #  抢票
#         global ticket
#         while True:
#             if ticket > 0:
#                 self.count = self.count + 1
#                 ticket = ticket - 1
#                 print(self.username,"成功抢了一张票！还剩",ticket,"张票！")
#                 time.sleep(0.1)
#             else:
#                 print(self.username,"总共抢了",self.count,"张票！")
#                 break
# u1 = User()
# u2 = User()
# u3 = User()
# u1.username = "jason"
# u2.username = "旺财"
# u3.username = "陈光环"
#
# u1.start()
# u2.start()
# u3.start()

from threading import Thread
basket=0
import time
class chief(Thread):
    name=''
    def run(self) -> None:
        global basket
        while True:
            if basket > 500:
                print("等待三秒")
                time.sleep(3)
            else:
                basket = basket + 1
                print("哈哈", self.name, "造了个蛋挞")



everyegg=2
money=3000
class person(Thread):
    name=''
    def run(self) -> None:
        global egg, money,basket
        while True:
            if basket < 0:
                print("请等待2秒")
                sleep(2)
            else:
                if money < 0:
                    print("不好意思",self.name,"钱不够了")
                    break
                else:
                    money = money - everyegg
                    print("好开心哦，",self.name,"买了一个蛋挞")

c1=chief()
c2=chief()
c3=chief()
c1.name="zhang"
c2.name="li"
c3.name="wang"
c1.start()
c2.start()
c3.start()
p1=person()
p2=person()
p3=person()
p1.name="xxx"
p2.name="jjj"
p3.name="www"
p1.start()
p2.start()
p3.start()



















