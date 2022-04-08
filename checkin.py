import os
import requests

def send_plus_msg(msg):
    url = f"http://www.pushplus.plus/send?token=78465b494d2d494a905bfa5ff02444d2&title={msg}&content={msg}&template=html"
    requests.get(url)

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

response = requests.post("https://www.wanbianios.com/wp-admin/admin-ajax.php", data="action=user_qiandao", headers=headers, cookies=cookies)
response.encoding = 'utf-8'
print("status_code:", response.status_code)
print("response:", response.json())

if str(response.text) == "0":
    print("错误，请检查COOKIES")
    send_plus_msg("签到错误，请检查COOKIES，返回值：" + str(response.text))
elif response.json()['status'] == "1":
    print("签到成功")
    send_plus_msg("签到成功")
elif response.json()['status'] == "0":
    print("今日已签到")
