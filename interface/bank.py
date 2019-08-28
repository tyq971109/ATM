from db import db_handler



def check_balance_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']

def withdraw_interface(username, money):
    user_dic = db_handler.select(username)
    rel_money = money * 1.05
    if user_dic.get('balance') > rel_money:
        user_dic['balance'] -= rel_money

        msg = f'{username}提现{money}元成功！'
        user_dic['bank_flow'].append(msg)
        db_handler.save(user_dic)

        return True, msg
    return False, '账户余额不足'

def repay_interface(username,money):
    user_dic = db_handler.select(username)

    user_dic['balance'] += money
    msg = f'{username}还款{money}成功'
    user_dic['bank_flow'].append(msg)

    db_handler.save(user_dic)

    return msg


def transfer_interface(username, to_username, money):
    to_user_dic = db_handler.select(to_username)
    if not to_user_dic:
        return False, '该目标用户不存在'

    user_dic = db_handler.select(username)
    if user_dic['balance'] >= money:
        to_user_dic['balance'] += money
        user_dic['balance'] -= money

        msg = f'{username}成功向{to_username}转账{money}元'

        user_dic['bank_flow'].append(msg)
        to_user_flow = f'{to_username}成功收到{username}转的{money}元'
        to_user_dic['bank_flow'].append(to_user_flow)
        db_handler.save(user_dic)
        db_handler.save(to_user_dic)

        return True, msg
    return False, '账户余额不足，请输入正确金额'

def pay_interface(username, cost):
    user_dic = db_handler.select(username)
    if user_dic['balance'] > cost:
        user_dic['balance'] -= cost
        flow = f'{username}购物消费{cost}元'
        user_dic['bank_flow'].append(flow)

        db_handler.save(user_dic)

        return True

    return False


def check_flow_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('bank_flow')