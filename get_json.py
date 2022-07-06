import re
import requests

def get_json(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE','Referer':\
        'https://www.16df.xyz/home.html'}
    #获取域名
    url_x = url+"/"
    re_url = r"//(.*?)/"
    url_main=re.findall(re_url,url_x)
    #获取源代码
    html_data = requests.get(url,headers=headers).text
    #正则查找/xxx/xxx.json
    re_json_x = r''+str(url_main[0])+'(/[^\s]*?\.json)'
    re_json_y = r'=(/[^\s]*?\.json)'
    re_json_z = r'"([^\s]*?\.json)'
    json_data_x = re.findall(re_json_x,html_data)
    json_data_y = re.findall(re_json_y,html_data)
    json_data_z = re.findall(re_json_z, html_data)

    de_json=[]
    for i in range(len(json_data_z)):
        for i2 in range(len(json_data_x)):
            if json_data_x[i2] in json_data_z[i]:
                de_json.append(json_data_z[i])
    for j in range(len(de_json)):
        json_data_z.remove(de_json[j])

    json_list = json_data_x+json_data_y+json_data_z
    json_list = list(set(json_list))
    return url_main,json_list,len(json_list)

# if __name__=='__main__':
#     url = "https://www.jxjyedu.org.cn/"
#     name,json,json_num=get_json(url)
#     print(json)