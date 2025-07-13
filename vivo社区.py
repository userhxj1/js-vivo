import requests
import execjs
import json
import time
from queue import Queue


with open('vivo.js', 'r', encoding='utf-8') as f:
    data = f.read()

ctx = execjs.compile(data)
result = ctx.call('get_nonce')
print(result)

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Origin': 'https://bbs.vivo.com.cn',
    'Referer': 'https://bbs.vivo.com.cn/newbbs/',
}


data = {"lastId": "", "pageNum": 1, "pageSize": 10, "imgSpecs": ["t577x324", "t577x4096"],"timestamp": int(time.time() * 1000), "nonce": result}
response = requests.post('https://bbs.vivo.com.cn/api/community/index', headers=headers, data=json.dumps(data))
print(response.text)