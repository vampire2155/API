import yaml,requests
from config import HOST

class login_class_yaml():
    def login_yaml_api(self,username,password):
        url = f'{HOST}/api/mgr/loginReq'
        form_data = {'username':username,
                     'password':password
                    }
        res = requests.post(url,data=form_data)
        res.encoding = 'unicode-escape'
        return res.text

if __name__ == '__main__':
    print (login_class_yaml().login_yaml_api('auto','sdfsdfsdf'))
    print (type(login_class_yaml().login_yaml_api('auto','sdfsdfsdf')))


