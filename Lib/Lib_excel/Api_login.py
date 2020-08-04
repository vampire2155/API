#登录模块中的所有用例封装在一个 类 中。
import requests
from config import HOST
class LoginClass():
    def login_Api(self,username, password):
        url = f'{HOST}/api/mgr/loginReq'
        headers = {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
                   'Connection': 'keep-alive', 'Content-Length': '311',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        form_data = {
            'username': username,
            'password': password
        }
        res = requests.post(url, data=form_data)
        res.encoding = 'unicode-escape'
        return res.cookies,res.text
if __name__ == '__main__':
    # print (LoginClass().login_Api('auto','sdfsdfsdf'))
    print (LoginClass().login_Api('auto','sdfsdfsdf')[0]['sessionid'])
