import pytest,json,allure
from Lib.Lib_excel.Api_login import LoginClass
from Lib.Lib_excel.get_login_excelData import get_login_excelData
@allure.feature('登录模块')
# @pytest.mark.login(order=1)  #标签，用来 单独执行这个用例时使用。
@pytest.mark.flaky(reruns=3)
class Test_login():
    #get_login_excelData() 的返回值是一个 列表类型的值。结果为 [('auto', 'sdfsdfsdf', 0), ('', 'sdfsdfsdf', 1), ('auto', '', 1), ('', '', 1)]
    @allure.story('登录接口')
    @allure.title('登录接口用例')
    # @pytest.mark.flaky(reruns=3)  #装饰器，用例执行失败后会重新自动再执行3次，经验证失败用例会自动重新执行3次。
    @pytest.mark.parametrize('username,password,expected_result', get_login_excelData('1-登录接口'))   #装饰器  如果有多个参数，参数值一定是列表中 以元组的形式存储
    def testlogin(self,username,password,expected_result):
        ExeResult = json.loads(LoginClass().login_Api(username,password)[1])['retcode']  #用例执行的返回结果
        assert ExeResult == expected_result

# wb.save(r'G:\测试学习资料\接口测试\接口自动化测试_6-15\APItest_result.xlsx')   #目前结果都是 allure生成了图形化的测试报告，所以没有必要把测试结果写入到excel中。
if __name__ == '__main__':
    pytest.main(['-s'])
