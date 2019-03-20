import os
import re

import requests


class BaiduImage(object):
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/65.0.3325.181Safari / 537.36'
        }
        self.keyworld=input('请输入想要下载的关键字：')
        file_dir=r'J:\thread\venv\Image'
        file_name = self.keyworld + str(1) + '.jpg'
        self.file_path = os.path.join(file_dir, file_name)
        self.fp = open(self.file_path,'wb')

    def getResponse(self,url):
        response=requests.get(url=url,headers=self.headers)
        return response
    def parse_url(self,response):
        html=response.text
        result=re.compile('objURL":"(.*?)"',re.S)
        data=re.findall(result,html)
        return data

    def sava_data(self,item):
        content=item.content
        self.fp.write(content)


    def main(self):
        url='http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='+self.keyworld
        response=self.getResponse(url)
        self.Image_url=self.parse_url(response)
        for i in self.Image_url:
            res_Image=self.getResponse(i)
            self.sava_data(res_Image)
        self.fp.close()
if __name__ == '__main__':
    c=BaiduImage()
    c.main()