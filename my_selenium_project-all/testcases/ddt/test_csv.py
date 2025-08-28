import pytest
import csv



def get_data():
    with open('test.csv') as f:
        lst = csv.reader(f)  # lst是一个迭代器
        my_data = []
        for row in lst:  # 每次迭代会返回一行数据，row是一个列表
            my_data.extend(row)
    return my_data

@pytest.mark.parametrize('name', get_data())
def test01(name):
    print(name)





if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv', 'test_csv.py'])

