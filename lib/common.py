'''
存放公共方法
'''
import hashlib


# md5加密
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '20220101'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()


# 登录认证装饰器
def login_auth(func):
    from core import src

    def inner(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('用户未登录，请登录')
            src.login()

    return inner


import logging.config
from conf import settings


# 添加日志功能
# 获取日志对象
def get_logger(log_type):
    # 加载日志配置信息
    logging.config.dictConfig(settings.LOGGING_DIC)
    # 获取日志对象
    logger = logging.getLogger()
    return logger

def login_root(func):
    from core import src

    def inner(*args, **kwargs):
        if src.login_user == 'alan':
            res = func(*args, **kwargs)
            return res
        else:
            print('请登录管理ID。。')
            src.login()

    return inner