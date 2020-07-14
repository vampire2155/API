import requests, json
from config import *


class LessonClass():
    #1、增加课程接口
    def addClassAPI(self,session,data):
        user_cookie = {'sessionid':session}
        # 增加课程接口
        url = f'{HOST}/api/mgr/sq_mgr/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        form_data = {
            'action': 'add_course',
            'data': json.dumps(data)   #把data数据转换成json格式，API接口文档中要求入参是json格式
        }
        res = requests.post(url, data=form_data, cookies=user_cookie)
        res.encoding = 'unicode-escape'
        return res.text  #可以写多个返回值，返回值之间用 逗号 分割，所以所有的返回值组成了一个 tuple（元组），调用的时候使用下标进行取值。

    # 2、列出课程接口
    def listClassAPI(self,session,data):
        user_cookie = {'sessionid': session}
        url = f'{HOST}/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
        res = requests.get(url, params=data,cookies=user_cookie)  # 不需要headers ，需要搞清楚为什么？ 什么情况下需要填写headers，什么情况下不需要填写headers
        res.encoding = 'unicode-escape'
        return res.json()

    #3、删除课程接口
    def deleteLessonAPI(self,session,data):
        user_cookie = {'sessionid': session}
        url = f'{HOST}/api/mgr/sq_mgr/'
        res = requests.delete(url,data=data,cookies=user_cookie)  # 不需要headers ，需要搞清楚为什么？ 什么情况下需要填写headers，什么情况下不需要填写headers
        res.encoding = 'unicode-escape'
        return res.text

    #3.1删除所有的课程
    def delete_all_lesson(self, session, inId):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        form_data = {'action': 'delete_course',
                   'id': int(inId)
                   }
        reps = requests.delete(api_url, data=form_data,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text

    #4、修改课程接口   --
    def modifyLessonAPI(self,session,data):
        user_cookie = {'sessionid': session}
        url = f'{HOST}/api/mgr/sq_mgr/'
        res = requests.put(url,data=data,cookies=user_cookie)  # 不需要headers ，需要搞清楚为什么？ 什么情况下需要填写headers，什么情况下不需要填写headers
        res.encoding = 'unicode-escape'
        return res.text


if __name__ == '__main__':
    pass
    # print (LessonClass().deleteLessonAPI('ut77jo7k6f8nqwcd9cgclu3xl8rhlcwi',{"action":"delete_course","id":"122abc"}))
    print (LessonClass().addClassAPI('ut77jo7k6f8nqwcd9cgclu3xl8rhlcwi',{"name":"大学英语010","desc":"大学英语课程","display_idx":","}))
    # res = LessonClass().listClassAPI('ut77jo7k6f8nqwcd9cgclu3xl8rhlcwi',{"action":"list_course","pagenum":"1","pagesize":"20"})
    # print (res)
    # print (res['retlist'])
    # print(type(LessonClass().listClassAPI('ut77jo7k6f8nqwcd9cgclu3xl8rhlcwi',{"action": "list_course", "pagenum": "1", "pagesize": "20"})))
    # print (type(json.loads(LessonClass().modifyLessonAPI('uefrcqtcjr957ns4n39dtxlpzcm6kl4m',{"action":"modify_course","id":"100","newdata":'{ "name":"松勤","desc":"心田老师课程","display_idx":"5"}'}))["retcode"]))
    # for one in range(1,21):
    #     data = {"name":f"大学{one}","desc":f"大学英语课程{one}","display_idx":f"{one}"}
    #     print (LessonClass().addClassAPI('y3uenicmjm76hervak063te4k3yosmll',data))
    # print (LessonClass().clear_datas())