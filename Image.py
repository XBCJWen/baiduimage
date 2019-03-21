import os
import re
import time

import requests
# 暴力获取百度图片方法

class BaiduImage(object):
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/65.0.3325.181Safari / 537.36'
        }
        self.keyworld=input('请输入想要下载的关键字：')

    def getResponse(self,url):
        response=requests.post(url=url,headers=self.headers)
        return response
    def parse_url(self,response):
        html=response.text
        result=re.compile('objURL":"(.*?)"',re.S)
        data=re.findall(result,html)
        return data
    def save_img(self,img):
        img1=img.content
        return  img1


    def main(self):
        url='http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='+self.keyworld
        response=self.getResponse(url)
        Image_url=self.parse_url(response)
        j=1
        for i in Image_url:
            print(i)
            res_Image = self.getResponse(i)
            img = self.save_img(res_Image)
            time.sleep(0.01)
            file_dir = r'J:\thread\venv\Image'
            file_name = str(self.keyworld)  + '%s.jpg'%str(j)
            j=j+1
            print(j)
            print("正在保存"+file_name)
            file_path = os.path.join(file_dir, file_name)
            f=open(file_path, 'wb')
            f.write(img)
            f.closed


if __name__ == '__main__':
    c=BaiduImage()
    c.main()