from interface import bank
from interface import shop
from interface import user
from libs import common
user_info = {'user': None}


def register():
    print('欢迎来到注册界面')
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请再次输入密码：').strip()

        if password == re_password:
            flag, msg = user.register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def login():
    print('欢迎来到登录界面')
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        flag, msg = user.login_interface(username, password)
        if flag:
            print(msg)
            user_info['user'] = username
            break
        else:
            print(msg)
@common.login_auth
def check_balance():
    print('查看余额界面')
    msg = bank.check_balance_interface(user_info['user'])
    print(msg)

@common.login_auth
def withdraw():
    print('欢迎来到取款界面')
    while True:
        money = input('请输入取款金额')
        if not money.isdigit():
            print('请输入正确的金额')
            continue
        money = int(money)
        flag, msg = bank.withdraw_interface(user_info.get('user'), money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth
def repay():
    print('还款界面')
    while True:
        money = input('请输入还款金额：').strip()
        if not money.isdigit():
            print('金额必须是数字')
            continue
        money = int(money)
        msg = bank.repay_interface(user_info['user'], money)
        print(msg)
        break

@common.login_auth
def transfer():
    print('欢迎来到转账界面')
    while True:
        to_username = input('请输入转账目标用户：').strip()

        money = input('请输入转账金额：').strip()
        if not money.isdigit():
            print('金额必须是数字')
            continue

        money = int(money)
        flag, msg = bank.transfer_interface(user_info['user'], to_username, money)
        if flag:
            print(msg)
            break
        else:
            print(msg)
@common.login_auth
def check_flow():
    print('欢迎来到查看流水界面')
    flow_list = bank.check_flow_interface(user_info['user'])

    if flow_list:
        for flow in flow_list:
            print(flow)

@common.login_auth
def shopping():
    print('欢迎来到购物界面')
    goods_list = [
        ['电脑',5000],
        ['手机',2388],
        ['手表',13888],
        ['沙茶面',20],
        ['冰红茶',3.5]
    ]

    shop_car = {}
    cost = 0

    balance = bank.check_balance_interface(user_info['user'])

    while True:
        for index, goods in enumerate(goods_list):
            print(index, goods)

        choice = input('请输入商品编号，输入q退出：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入商品编号')
            continue

        choice = int(choice)

        goods_name, goods_price = goods_list[choice]

        if balance >= goods_price:
            if goods_name in shop_car:
                shop_car[goods_name] += 1
            else:
                shop_car[goods_name] = 1

            cost += goods_price
        else:
            print('账户余额不足')

    if not cost:
        print('未选择商品')
        return

    sure = input('购买输入y，存入购物车输入n:').strip()
    if sure == 'y':
        flag, msg = shop.shop_pay_interface(user_info['user'], shop_car, cost)
        if flag:
            print(msg)
        else:
            print(msg)
    elif  sure == 'n':
        flag, msg = shop.shopping_car_interface(user_info['user'], shop_car)
        if flag:
            print(msg)
        else:
            print(msg)


@common.login_auth
def check_shop_car():
    print('欢迎来到购物车界面')
    shop_car = shop.check_shop_car_interface(user_info['user'])
    print(shop_car)

def logout():
    if user_info.get('user'):
        msg = user.logout_interface()
        print(msg)

func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': logout
}


def run():
    while True:
        print('''
        1.注册
        2.登录
        3.查看余额
        4.取款
        5.还款
        6.转账
        7.查看流水
        8.购物
        9.查看购物车
        10.注销
        q.退出
        ''')
        choice = input('请输入功能编号：').strip()

        if choice == 'q':
            break



        if choice not in func_dic:
            print('请输入正确的功能编号！！')
            continue
        func_dic.get(choice)()