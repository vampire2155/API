@echo off
echo �̹�ϵͳ�ӿ��Զ�������׼����ʼ......
@echo on

del /f /s /q  G:\Python_autoAPI\testcase\report\report_yaml\tmp_yaml\*.json
del /f /s /q  G:\Python_autoAPI\testcase\report\report_yaml\tmp_yaml\*.jpg
del /f /s /q  G:\Python_autoAPI\testcase\report\report_yaml\report_yaml

@echo off
echo �����ļ�ɾ��������ɣ���ʼ���нű�......
@echo on

cd G:\Python_autoAPI\testcase\testcase_yaml
pytest  -sq  --alluredir=../report/report_yaml/tmp_yaml
allure generate ../report/report_yaml/tmp_yaml -o ../report/report_yaml/report_yaml --clean

@echo off
echo �ӿ��Զ������гɹ�
pause