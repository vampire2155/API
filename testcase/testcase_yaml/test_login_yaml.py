import yaml,json,pytest,allure
from config import yamlDir
from Lib.Lib_yaml.Api_login_yaml import login_class_yaml

List = []
with open(yamlDir, 'r', encoding='utf-8') as fo:
    res = yaml.load_all(fo, Loader=yaml.FullLoader)
    for one in res:
        username = one[0]['username']
        password = one[0]['password']
        expexcted_result = one[1]["retcode"]
        List.append((username,password,expexcted_result))

@allure.feature('登录模块')
@pytest.mark.LoginClass
class Test_login_yaml():
    @allure.title('登录接口')
    @allure.story('登录接口用例')
    @pytest.mark.parametrize('usrname,psd,expexcted_result',List)
    def test_login_yaml(self,usrname,psd,expexcted_result):
        with allure.step('第一步、获取执行结果'):
            ExeResult = json.loads(login_class_yaml().login_yaml_api(usrname,psd))["retcode"]
        with allure.step('第二步、获取用例的预期结果'):
            exp_result = expexcted_result
        with allure.step('第三步、判断执行结果是否与预期结果相同'):
            assert ExeResult == exp_result

if __name__ == '__main__':
    pytest.main(['-s'])




