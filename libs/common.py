from functools import wraps

def login_auth(func):
    from core import src
    @wraps(func)
    def inner(*args, **kwargs):
        if src.user_info.get('user'):
            res = func(*args, **kwargs)
            return res
        else:
            print('请先登录！')
            src.login()
    return inner