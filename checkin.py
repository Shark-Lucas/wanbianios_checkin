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

cookies = os.environ.get('COOKIES')
cookies = str_to_dict(cookies)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0"
}
print("cookies:", cookies)
print("headers:", headers)
response = requests.post("https://www.wanbianios.com/wp-admin/admin-ajax.php", data="action=user_qiandao", cookies=cookies, headers=headers)
response.encoding = 'utf-8'
print(response.status_code)
print("response:", response.text)
