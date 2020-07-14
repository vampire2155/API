@echo off
echo 教管系统接口自动化运行准备开始......
@echo on

del /f /s /q  G:\Python_autoAPI\testcase\report\report_yaml\tmp_yaml\*.json
del /f /s /q  G:\Python_autoAPI\testcase\report\report_yaml\tmp_yaml\*.jpg
del /f /s /q  G:\Python_autoAPI\testcase\report\report_yaml\report_yaml

@echo off
echo 环境文件删除工作完成，开始运行脚本......
@echo on

cd G:\Python_autoAPI\testcase\testcase_yaml
pytest  -sq  --alluredir=../report/report_yaml/tmp_yaml
allure generate ../report/report_yaml/tmp_yaml -o ../report/report_yaml/report_yaml --clean

@echo off
echo 接口自动化运行成功
pause