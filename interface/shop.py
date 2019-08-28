from interface import bank
from db import db_handler


def shop_pay_interface(username, shop_car, cost):
    flag = bank.pay_interface(username, cost)

    user_dic = db_handler.select(username)

    if flag:
        user_dic['shop_car'] = {}
        db_handler.save(user_dic)
        return True, '购物支付成功'
    else:
        user_dic['shop_car'] = shop_car
        db_handler.save(user_dic)
        return False, '支付失败，存入购物车中'


def shopping_car_interface(username, shop_car):
    user_dic = db_handler.select(username)
    if shop_car:
        user_dic['shop_car'] = shop_car
        db_handler.save(user_dic)
        return True, '添加购物车成功'
    else:
        return False, '购物车是空的'

def check_shop_car_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['shop_car']