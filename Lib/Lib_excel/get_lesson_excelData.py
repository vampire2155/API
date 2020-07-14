from openpyxl import load_workbook
from config import *
import json

def get_lesson_excelData(sheet_name):
    DataList = []
    workBook = load_workbook(excelDir)
    workSheet = workBook[f'{sheet_name}']
    numofRows = workSheet.max_row  # 获取表格中有效数据的长度，即有多少行是有数据的。
    for row in range(2,numofRows+1):
        lessonData = json.loads(workSheet.cell(row=int(row), column=7).value)
        expected_result = json.loads(workSheet.cell(row=row, column=9).value)['retcode']
        DataList.append((lessonData,expected_result))
    return DataList

if __name__ == '__main__':
    # print (get_lesson_excelData('5-修改课程'))
    print (type(get_lesson_excelData('3-列出课程')))
    # print (get_resultData('2-增加课程'))
    # pprint(type(get_resultData('2-增加课程')[0]))
    # print (type(json.dumps(get_lesson_excelData('2-增加课程')[0]['data'])))