del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\log_excel\*
@echo off >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
echo 教管系统接口自动化运行准备开始...... >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
@echo on >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\tmp_excel\*.json >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\tmp_excel\*.jpg  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\report_excel   >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

@echo off  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
echo 环境文件删除工作完成，开始运行脚本......  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
@echo on >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

cd G:\Python_autoAPI\testcase\testcase_excel  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
pytest  -sq  --alluredir=../report/report_excel/tmp_excel  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
allure generate ../report/report_excel/tmp_excel -o ../report/report_excel/report_excel --clean  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

@echo off  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
echo 接口自动化运行成功  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
pause