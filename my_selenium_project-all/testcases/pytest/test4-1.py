import pytest

@pytest.fixture(scope="module")
def shared_resource():
    print("\n=== 模块级fixture初始化（只执行一次）===") #只在第一次调用时执行
    resource = {"data": 100, "active": True}
    yield resource  # 返回给测试用例的值, yield是分割前置和后置的关键字
    print("\n=== 模块级fixture清理（只执行一次）===") # 会在所有测试用例执行完成后执行

def test_case11(shared_resource):
    print(f"测试1使用资源: {shared_resource}")
    shared_resource["data"] -= 10  # 修改资源

def test_case22(shared_resource):
    print(f"测试2使用资源: {shared_resource}")  # 会看到被test_case1修改后的值

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test4-1.py'])