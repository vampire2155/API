@echo off
echo �̹�ϵͳ�ӿ��Զ�������׼����ʼ......
@echo on

del /f /s /q  G:\Python_autoAPI\report\tmp\*.json
del /f /s /q  G:\Python_autoAPI\report\report

@echo off
echo �����ļ�ɾ��������ɣ���ʼ���нű�......
@echo on

cd G:\Python_autoAPI\testcase
pytest  -sq  --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean

@echo off
echo �ӿ��Զ������гɹ�
pause