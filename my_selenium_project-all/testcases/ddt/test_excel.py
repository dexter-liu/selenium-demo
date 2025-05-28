import pytest
# import xlrd
import openpyxl


def get_data():
    filename = 'data.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    lst = []
    for row in sheet.iter_rows(values_only=True):  # 遍历所有行
        for cell in row:  # 遍历行中的单元格
            lst.append(cell)
    return lst

@pytest.mark.parametrize('name', get_data())
def test1(name):
    print(name)

if __name__ == '__main__':
    pytest.main(['-sv', 'test_excel.py'])


