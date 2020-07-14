from openpyxl import load_workbook
from config import *
import json

def get_login_excelData(sheet_name):
    DataList = []
    workBook = load_workbook(excelDir)
    workSheet = workBook[f'{sheet_name}']
    numofRows = workSheet.max_row  # 获取表格中有效数据的长度，即有多少行是有数据的。
    for row in range(2,numofRows+1):  #第一行是标题，所以用例是从第二行开始。
        cellData = json.loads(workSheet.cell(row=int(row), column=7).value)
        expected_result = json.loads(workSheet.cell(row=row, column=9).value)['retcode']
        usrName = cellData['username']
        psd = cellData['password']
        if cellData not in DataList:
            DataList.append((usrName,psd,expected_result))
    return DataList

if __name__ == '__main__':
    print (get_login_excelData('2-增加课程'))
    print(type(get_login_excelData('2-增加课程')))
    # for one in get_login_excelData():
    #     print (f'one---{one}')
    #     print (one[1])
    #     print (type(one[1]))
    #     usrName = one[0]['username']
    #     psd = one[0]['password']
    #     print(usrName, psd)






