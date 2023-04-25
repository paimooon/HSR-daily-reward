import requests
import os

ltuid = os.environ.get('LTUID')
ltoken = os.environ.get('LTOKEN')

url = "https://sg-public-api.hoyolab.com/event/luna/os/sign?act_id=e202303301540311&lang=ko-kr"

cookies = {'ltuid': ltuid, 'ltoken': ltoken}

r = requests.post(url, cookies=cookies)
print(r.json()['message'])
