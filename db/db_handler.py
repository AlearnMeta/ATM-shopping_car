'''
数据处理层
'''
import json
import os
from conf import settings


def select(username):
    # 用户数据人手一份，直接用用户名命名
    # 拼接用户数据得json文件路径
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    # 接受到注册后的结果，并打印
    # 如果用户已存在
    if os.path.exists(user_path):
        # with open(user_path,'r',encoding='utf-8') as f:
        #     user_dic = json.load(f)
        # if user_dic:
        # print('用户已存在,请重新输入')
        # 若用户不存在则保存数据
        # 若用户存在，则让用户重新输入
        # 格式化用户输入信息
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)  # 将json文件的数据取出，转化为字典类型，并返回结果
            return user_dic

    # 注册用户不存在，返回None，可以不用写
    else:
        return None


# 保存数据
def save(user_dic):
    # 拼接用户字典
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    # 保存数据
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
















