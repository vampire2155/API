from config import *
import yaml,pytest,json,allure      # pip install pyyaml  安装yaml库
from Lib.Lib_excel.Api_lesson import LessonClass
from Lib.Lib_excel.Api_login import LoginClass

session = LoginClass().login_Api(username, password)[0]['sessionid']
List = []
 # 读取yaml文件中的内容   使用yaml库    
with open(lessonYamlDir, 'r', encoding='utf-8') as fo:
    res = yaml.load_all(fo, Loader=yaml.FullLoader)
    for one in res:
        lessonInfo = one[0]
        expexcted_result = one[1]["retcode"]
        List.append((lessonInfo,expexcted_result))

@allure.feature('课程模块')
class Test_lesson_yaml():
    @allure.story('增加课程接口')
    @allure.title('增加课程接口用例')
    @pytest.mark.parametrize('lessonData,expResult',List)    # 装饰器
    def test_add_lesson_yaml(self,lessonData,expResult):
        EXEresult = json.loads(LessonClass().addClassAPI(session,lessonData))['retcode']
        assert EXEresult == expResult