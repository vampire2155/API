del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\log_excel\*
@echo off >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
echo �̹�ϵͳ�ӿ��Զ�������׼����ʼ...... >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
@echo on >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\tmp_excel\*.json >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\tmp_excel\*.jpg  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
del /f /s /q  G:\Python_autoAPI\testcase\report\report_excel\report_excel   >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

@echo off  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
echo �����ļ�ɾ��������ɣ���ʼ���нű�......  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
@echo on >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

cd G:\Python_autoAPI\testcase\testcase_excel  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
pytest  -sq  --alluredir=../report/report_excel/tmp_excel  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
allure generate ../report/report_excel/tmp_excel -o ../report/report_excel/report_excel --clean  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt

@echo off  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
echo �ӿ��Զ������гɹ�  >>G:\Python_autoAPI\testcase\report\report_excel\log_excel\Testlog.txt
pause