from db import db_handler
from lib import common
import time
T = time.strftime('%Y-%m-%d %X')
admin_logger = common.get_logger('admin')
# 修改额度接口
def change_balance_interface(username,money):
    user_dic = db_handler.select(username)
    if user_dic:
        user_dic['balance'] = int(money)
        db_handler.save(user_dic)
        msg = f'{T}用户{username}额度修改成功'
        admin_logger.info(msg)
        print(msg)
        return True
    print('目标用户不存在，请重新输入！')



# 冻结接口
def lock_user_interface(username):
    user_dic = db_handler.select(username)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)
        print(f'{T}用户{username}已冻结')
        return True
    print(f'用户{username}不存在')
