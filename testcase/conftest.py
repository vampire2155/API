#用例初始化模块   包括  用例执行前数据初始化  以及   用例执行完成以后的数据清除。
import pytest
from random import randint
from Lib.Lib_excel.Api_lesson import LessonClass
from Lib.Lib_excel.Api_login import LoginClass
from config import *

# 删除所有的课程
def clear_datas():
    # 这些代码是用来获取 总共的 课程条数的。
    inData = {'action': 'list_course',
              'pagenum': '1',
              'pagesize': '20'
              }
    session = LoginClass().login_Api(username, password)[0]['sessionid']
    res = LessonClass().listClassAPI(session, inData)
    totalLesson = res['total']  # 获取总共的 课程条数
    # 如果课程总条数 除以 20 有余数，则总页数需要加 1 。比如总共有 21条数据，则是 2 页。（因为一页显示20条）个位数因为除以 20 除不开，所以余数就是个位数本身。
    if totalLesson % 20 > 0:
        pageNum = int(totalLesson // 20) + 1
    elif totalLesson % 20 <= 0:
        pageNum = int(totalLesson // 20)
    elif totalLesson == 0:  # 需要判断没有课程数据时，页数 是 0
        pageNum = 0
    LessonList = []
    for num in range(1, pageNum + 1):
        Data = {'action': 'list_course',
                'pagenum': f'{num}',
                'pagesize': '20'
                }
        LessonList.append(LessonClass().listClassAPI(session, Data)['retlist'])
    while LessonList != []:
        for lesson in LessonList:
            for one in lesson:
                lessonId = one['id']
                LessonClass().delete_all_lesson(session, lessonId)
        break  # 如果不执行 break语句，经验证会一直执行while 循环。

@pytest.fixture(scope='module',autouse=True)  #环境初始化 、数据清除
def setup(request):
    clear_datas()

    #创建课程测试数据 ---如果单独执行删除课程用例时，因为执行了setup，所以会导致没有课程可供删除，所以需要增加。
    max_lesson_num = randint(1,51)  #因为创建的课程总数不同，可能会导致页数不同，所以在删除所有数据时，判断页数时会走不同的代码逻辑。
    for one in range(1,max_lesson_num):
        data = {"name":f"大学{one}","desc":f"大学英语课程{one}","display_idx":f"{one}"}
        print (LessonClass().addClassAPI('y3uenicmjm76hervak063te4k3yosmll',data))

    # 环境、数据清除----teardown
    def fin():  #为什么要命名为 fin() 函数，因为 fixture.html 文档中是这样写的。 其他名称应该也是可以的。
        clear_datas()
    request.addfinalizer(fin)  #函数名作为实参进行传递

if __name__ == '__main__':
    print (setup())






















