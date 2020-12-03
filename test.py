import requests
import time

header = {
    'cookie': "SESSDATA=4b2c60e1%2C1621746718%2Cd7ea0*b1;'user-agent':'fakeone'"
}

for i in range(100):
    req = requests.get('https://api.bilibili.com/x/web-interface/nav', headers=header)
    print(req.json())
    print(req.headers)
    print('=' * 100, time.time(), '=' * 100,)
