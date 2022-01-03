'''
逻辑接口
'''
# 注册接口
import os
import sys
from db import db_handler
from lib import common
user_logger = common.get_logger('user')

# 注册接口
def register_interface(username, password, balance=15000):
    # 判断用户名是否存在
    # 调用数据处理层的select函数，会返回字典或者None
    user_dic = db_handler.select(username)
    # 若用户存在，告诉用户重新输入
    if user_dic:
        print('用户名已存在，请重新输入！')
        return False

    # 密码加密
    password = common.get_pwd_md5(password)

    # 数据格式字典化
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],
        'shopping_car': {},
        'locked': False  # 用于记录用户是否被冻结
    }

    # 保存数据，并返回
    db_handler.save(user_dic)
    # 添加日志功能
    msg = f'{username}注册成功'
    user_logger.info(msg)
    print(msg)
    return True


# 登录接口
def login_interface(username, password):
    # 判断当前用户数据是否存在
    user_dic = db_handler.select(username)

    if user_dic:
        # 判断用户是否被锁定
        if user_dic['locked']:
            print('用户已被锁定')
            return False

        password = common.get_pwd_md5(password)
        # 校验密码
        if password == user_dic.get('password'):
            msg = f'{username}登录成功'
            user_logger.info(msg)
            print(msg)
            return True
        else:
            msg = f'{username}密码错误'
            user_logger.warn(msg)
            print(msg)
            return False
    else:
        msg = f'{username}不存在，请重新输入'
        user_logger.warn(msg)
        print(msg)
        return False


# 查看余额接口
def check_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('balance')

# 查看用户购物车
def check_shopping_car_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['shopping_car']