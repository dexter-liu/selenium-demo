import pytest
import json


# json_str = '{"key": "value", "a": 1}'
# json_str2= '["key", "value", "a"]'
#
# print(json.loads(json_str))
# print(json.loads(json_str2))
#
# import json
# data = {"name": "张三", "age": 25}
# json_str = json.dumps(data, ensure_ascii=False, indent=2)  # 保留中文，美化输出
# print(type(json_str))
# print(json_str)


def get_data():
    with open('test.json') as f:
        lst = []
        data = json.load(f)
        lst.extend(data['keys'])
    return lst
@pytest.mark.parametrize('name', get_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv','test_json.py'])