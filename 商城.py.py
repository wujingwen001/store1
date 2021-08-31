'''
    Jason的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10辣条优惠券（0.3），20机械革命优惠券（0.9）。
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''
import  time
import random
# 1.商品
shop = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["辣条",2.5],
    ["老干妈",13]
]

# 1.1 准备20个优惠券，然后随机给用户发一张
preferential = [
    ["机械革命",0.8] * 5, # 5张机械革命8折优惠券
    ["MAC PC",0.75] * 10,# 10张MAC电脑7.5折优惠券
    ["HUAWEI watch",0.9] * 8 #8张华为手环9折优惠券
]

# 1.2.初始化您的余额
money = ""
while True:
    m =  input("请输入您的钱包余额:")
    if m.isdigit():
        money = int(m)
        break
    else:
        print("金额不能为其他数据，只能为数字，请重新输入！")

# 缓冲加载
print("系统正在加载",end="")
for i in range(5):
    print(".",end="")
    time.sleep(1) # 每打印一个. 停1秒钟。

# 2抽取优惠券环节
favour = None # 空的优惠券
while True:
    print("\n下面是正式购物环节，是否要先抽取一个优惠券？1[yes] ，  2[no]:")
    ch = input("")
    if ch == "1": # 想要一张优惠券。
        favour = preferential[random.randint(0,len(preferential)-1)] # 随机获取一张优惠券揣兜里
        print("恭喜，您抽取了一张",favour[0],"的",favour[1],"折优惠券！")
        # 将商场的关于这张优惠券的对应的商品价格都改掉
        for index,value in enumerate(shop):
            if value[0] == favour[0]:  #value 代表后台商品库shop每种商品的信息（名称、价格）  value（0）代表该商品的名称
                shop[index][1] = shop[index][1] * favour[1] # 原价 * 折扣 = 现价，在更新现在商品价格
        break
    elif ch == '2':
        print("很遗憾，您不想要本次优惠券！祝您本次购物愉快！")
        break
    else:
        print("输入错误！难道您不想要优惠券？重新输入吧！")

# 3.准备一个空的购物车
mycart = []

# 4. 买东西
while True:
    # 展示商品
    print("-----------------------------------------")
    print("-编号\t名称\t\t原价\t\t现价-")
    print("-----------------------------------------")
    for index,value in enumerate(shop): # 枚举，将角标和商品整体都打印
        if value[0] == favour[0]:
            print("|",index,"\t",value[0],"\t",(value[1] / favour[1]),"\t",(value[1]))
        else:
            print("|",index,"\t",value[0],"\t",value[1],"\t",value[1])
    print("------------------------------------------")

    # 请输入您要的商品
    chose = input("请输入您要的商品：")

    # 看是否存在
    if chose.isdigit():  # 是否能被看成数字：
        chose = int(chose)
        # 看商品是否存在
        if chose > len(shop) - 1:  #在列表中下标默认从0开始，因此6个商品的列表，最大序号为5
            print("您要的商品不存在！")
        else:
            # 看钱是否足够
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                # 钱减去
                money = money - shop[chose][1]
                print("恭喜，成功添加购物车，您的余额还剩：￥",money)
            else:
                print("对不起，穷鬼，余额不足，请到其它地方去购买！")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您的输入商品不存在！别瞎弄!")

# 打印小票
print("下面是您的购物小条，请拿好：")
for  index,value in enumerate(mycart):
    print(index,"   ",value)
print("您的钱包还剩：￥",money)


















