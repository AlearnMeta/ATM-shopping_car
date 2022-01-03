'''
购物相关接口
'''
from interface import bank_interface
from db import db_handler
# 购物结算接口
def shopping_interface(username,shopping_car):
    '''效验成功后，由银行接口来做'''
    # 计算消费总额  shopping_car={'商品名':[价格，数量]}
    cost = 0
    for price, number in shopping_car.values():
        cost += price*number
    # 调用银行结算接口
    flag = bank_interface.pay_interface(username,cost)
    if flag:
        print(f'支付成功,应收{cost},实收{cost},准备发货')
        return True
    else:
        print('支付失败，余额不足')
        return False

# 购物车添加接口
def add_shop_car_interface(username,shooping_car):
    # 获取当前用户的购物车
    user_dic = db_handler.select(username)

    # 判断当前用户选择的商品是否已经存在
    user_dic['shopping_car'] = shooping_car
    db_handler.save(user_dic)
    print('添加购物车成功')
    return True


# 查看购物车接口
def check_shop_car_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('shop')