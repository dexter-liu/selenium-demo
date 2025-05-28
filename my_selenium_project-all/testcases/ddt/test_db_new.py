import pymysql
import pytest


conn = pymysql.connect(
    host='localhost',
    port=33306,
    user='root',
    password='dexter',
    database='se_db',
    charset='utf8mb4'
)

def get_data():
    query_sql = 'select id,name,value from se_test'

    lst = []
    try:
        cursor = conn.cursor()
        cursor.execute(query_sql)
        r = cursor.fetchall()
        for row in r:
            u = (row[0], row[1], row[2])
            lst.append(u)
        return lst # 返回一个元素是tuple的list
    finally:
        cursor.close()
        conn.close()

@pytest.mark.parametrize('id,name,value',get_data())
def test_db(id, name, value):
    print(id, name, value)

if __name__ == '__main__':
    pytest.main(['-sv', 'test_db_new.py'])

