'''
银行相关业务接口
'''
from db import db_handler
import time
T = time.strftime('%Y-%m-%d %X')

# 提现接口
def withdraw_interface(username, money):
    # 获取用户字典
    user_dic = db_handler.select(username)
    # 校验用户的钱够不够
    balance = int(user_dic.get('balance'))
    money2 = money * 1.05
    if balance >= money2:
        # 修改金额
        balance -= money2
        user_dic['balance'] = balance
        # 记录流水
        flow = f'{T}用户{username}成功提现{money},余额还有{balance}'
        user_dic['flow'].append(flow)
        # 更新数据
        db_handler.save(user_dic)
        print(flow)
        return True
    print('提现金额不足')


# 还款接口
def repay_interface(username, money):
    '''
    1.获取用户金额
    2.加钱的操作
    :return:
    '''
    user_dic = db_handler.select(username)
    user_dic['balance'] += money
    # 记录流水
    flow = f'{T}用户{username}成功还款{money}'
    user_dic['flow'].append(flow)
    # 存储数据，更新
    db_handler.save(user_dic)
    print(flow)
    return True


# 转账接口
def transfer_interface(username, to_user, money):
    '''
    1.获取当前用户
    2.转账目标用户
    3.转账金额
    :return:
    '''
    user_dic = db_handler.select(username)
    to_user_dic = db_handler.select(to_user)
    if not to_user_dic:
        print('转账目标不存在')
        return False
    # 用户存在，判断当前用户金额是否足够
    if user_dic['balance'] >= money:
        # 钱足够，给当前用户数据做减钱操作，给目标用户做加钱操作
        user_dic['balance'] -= money
        to_user_dic['balance'] += money

        # 记录流水
        flow1 = f'{T}用户{username}成功转账{money}给{to_user}'
        user_dic['flow'].append(flow1)
        flow2 = f'{T}用户{to_user}收到{username}转账{money}'
        to_user_dic['flow'].append(flow2)

        db_handler.save(user_dic)
        db_handler.save(to_user_dic)
        print(flow1)
        return True
    else:
        print('余额不足')
        return False

# 查看流水接口
def check_flow_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['flow']

# 结算接口
def pay_interface(username,money):
    user_dic = db_handler.select(username)
    # 判断是否有钱
    if user_dic['balance'] >= money:
        user_dic['balance'] -= money
        user_dic['shopping_car'] = {}
        # 记录消费流水
        flow = f'{T}用户{username}消费了{money}'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        return True
    return False
