import pytest, allure
from Lib.Lib_excel.Api_lesson import LessonClass
from Lib.Lib_excel.Api_login import LoginClass
from Lib.Lib_excel.get_lesson_excelData import *

session = LoginClass().login_Api(username, password)[0]['sessionid']
@allure.feature('课程模块')
@pytest.mark.flaky(reruns=3)  #装饰器，用例执行失败后会重新自动再执行3次
class Test_lesson():
    #增加课程用例
    @allure.story('增加课程接口')
    @allure.title('增加课程接口用例')
    # @pytest.mark.flaky(reruns=3) #装饰器，用例执行失败后会重新自动再执行3次
    @pytest.mark.parametrize('lessonData, expected_result',get_lesson_excelData('2-增加课程'))
    def test_add_lesson(self,lessonData, expected_result):
        with allure.step('第一步、获取测试结果'):
            ExeResult = int(json.loads(LessonClass().addClassAPI(session,lessonData))["retcode"])
        with allure.step('第二步、判断用例执行结果是否与预期结果相同'):
            assert ExeResult == expected_result

    #列出课程用例
    @allure.story('列出课程接口')
    @allure.title('列出课程接口用例')
    # @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('lessonData, expected_result',get_lesson_excelData('3-列出课程'))
    def test_list_lesson(self,lessonData, expected_result):
        with allure.step('第一步、获取测试结果'):
            ExeResult = LessonClass().listClassAPI(session,lessonData)["retcode"]
        with allure.step('第二步、判断用例执行结果是否与预期结果相同'):
            assert ExeResult == expected_result


    # #修改课程用例   5-修改课程   --修改接口用例目前有问题，需要调试。
    # @allure.story('修改课程接口')
    # @allure.title('修改课程接口用例')
    # @pytest.mark.parametrize('lessonData, expected_result',get_lesson_excelData('5-修改课程'))
    # def test_modify_lesson(self,lessonData, expected_result):
    #     ExeResult = json.loads(LessonClass().modifyLessonAPI(session,lessonData))["retcode"]
    #     print (ExeResult)
    #     assert ExeResult == expected_result


    #删除课程用例
    @allure.story('删除课程接口')
    @allure.title('删除课程接口用例')
    # @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('lessonData, expected_result',get_lesson_excelData('4-删除课程'))
    def test_delete_lesson(self,lessonData, expected_result):
        with allure.step('第一步、获取测试结果'):
            ExeResult = json.loads(LessonClass().deleteLessonAPI(session,lessonData))["retcode"]
        with allure.step('第二步、判断用例执行结果是否与预期结果相同'):
            assert ExeResult == expected_result

# wb.save(r'G:\测试学习资料\接口测试\接口自动化测试_6-15\APItest_result.xlsx')
if __name__ == '__main__':
    pytest.main(['-s'])













