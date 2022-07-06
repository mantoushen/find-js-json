import re
import requests

def get_js(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE','Referer':\
        'https://www.16df.xyz/home.html'}
    #获取域名
    url_x = url+"/"
    re_url = r"//(.*?)/"
    url_main=re.findall(re_url,url_x)
    #获取源代码

    html_data = requests.get(url,headers=headers).text
    #正则查找/xxx/xxx.js
    re_js_x = r''+str(url_main[0])+'(/[^\s]*?\.js)'
    re_js_y = r'=(/[^\s]*?\.js)'
    re_js_z = r'="([^\s]*?\.js)'
    js_data_x = re.findall(re_js_x,html_data)
    js_data_y = re.findall(re_js_y,html_data)
    js_data_z = re.findall(re_js_z, html_data)

    de_js=[]
    for i in range(len(js_data_z)):
        for i2 in range(len(js_data_x)):
            if js_data_x[i2] in js_data_z[i]:
                de_js.append(js_data_z[i])
    for j in range(len(de_js)):
        js_data_z.remove(de_js[j])

    js_list = js_data_x+js_data_y+js_data_z
    js_list = list(set(js_list))
    #输出----》主域名，js，js数目
    return url_main,js_list,len(js_list)

# if __name__=='__main__':
#     url = "https://www.huanghuai.edu.cn/"
#     name,js,js_num=get_js(url)
#     print(js)