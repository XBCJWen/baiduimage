import requests

class BaiduImage(object):
    # //分析百度网页结构
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

   def get_response(self,url,data):
       response=requests.post(url=url,data=data,headers=self.headers)
       return  response


if __name__ == '__main__':
    c=thread