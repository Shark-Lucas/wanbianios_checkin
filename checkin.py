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
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
}
print("cookies:", cookies)
print("headers:", headers)
response = requests.post("https://www.wanbianios.com/wp-admin/admin-ajax.php", data="action=user_qiandao", headers=headers, cookies=cookies)
response.encoding = 'utf-8'
print(response.status_code)
print("response:", response.json())
print("response.text:", response.text)