import os,requests
from bs4 import BeautifulSoup
#创建漫画文件夹
try:
    os.mkdir('./xkcd')
except Exception as e:
    print("已创建文件夹")

url = 'https://xkcd.com/'
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}


#网络请求
resp = requests.get(url,headers=headers)
#抓包
soup = BeautifulSoup(resp.text,features='html.parser')
#提取图像标签
comic_element = soup.select('#comic img') ##comic是id
comicURl = 'https:' + comic_element[0].get('src')
#提取漫画名字
comic_name = soup.select('#ctitle')[0].get_text()
#保存图片
with open(f'./xkcd/{comic_name}.jpg','wb') as f:
    f.write(requests.get(comicURl).content)
    f.close()


#获取上一张漫画地址
up_element = None
while up_element != '#':
    up_element = soup.select('a[rel="prev"]')[0].get('href')
    up_url =url + up_element
    # 网络请求
    resp = requests.get(up_url, headers=headers)
    # 抓包
    soup = BeautifulSoup(resp.text, features='html.parser')
    # 提取图像标签
    comic_element = soup.select('#comic img')  ##comic是id
    comicURl = 'https:' + comic_element[0].get('src')
    # 提取漫画名字
    comic_name = soup.select('#ctitle')[0].get_text()
    # 保存图片
    number = str(up_element).strip('/')
    with open(f'./xkcd/{comic_name}{number}.jpg', 'wb') as f:
        f.write(requests.get(comicURl).content)
        f.close()
    print(f'{comic_name}下载成功')