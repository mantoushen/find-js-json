import requests

def get_js_text(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE','Referer':\
        'https://www.16df.xyz/home.html'}
    data = requests.get(url,headers=headers).text
    return data

# get_js_text('https://www.huanghuai.edu.cn/')
