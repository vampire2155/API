@echo off
echo 教管系统接口自动化运行准备开始......
@echo on

del /f /s /q  G:\Python_autoAPI\report\tmp\*.json
del /f /s /q  G:\Python_autoAPI\report\report

@echo off
echo 环境文件删除工作完成，开始运行脚本......
@echo on

cd G:\Python_autoAPI\testcase
pytest  -sq  --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean

@echo off
echo 接口自动化运行成功
pause