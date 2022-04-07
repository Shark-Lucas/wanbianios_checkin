import os
import requests


def str_to_dict(str):
    '''
    将字符串转换为字典
    '''
    dict = {}
    for i in str.split(';'):
        dict[i.split('=')[0].strip()] = i.split('=')[1].strip()
    return dict

cookies = ver_info_str = os.environ.get('COOKIES')
print("cookies:", str_to_dict(cookies))