from core import src
from db import db_handler
def logout_interface():
    src.user_info['user'] = None
    return '注销成功'



def register_interface(username, password):
    user_dic = db_handler.select(username)
    if user_dic:
        return False, '用户已存在'
    else:
        user_dic = {
            'username': username,
            'password': password,
            'balance': 15000,
            'bank_flow': [],
            'shop_car': {}
        }
        db_handler.save(user_dic)
        return True, f'{username}注册成功'


def login_interface(username, password):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False, '用户不存在'
    if user_dic['password'] == password:
        return True, f'{username}登录成功'
    else:
        return False, '密码错误'