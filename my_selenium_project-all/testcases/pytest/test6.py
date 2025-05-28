import allure
import pytest


@pytest.fixture(scope="session")
def login():
    print("用例先登录")


@allure.step("步骤1:点xxx")
def step_1():
    print("111")


@allure.step("步骤2:点xxx")
def step_2():
    print("222")


@allure.feature("编辑页面")  # 定义测试功能模块，在Allure报告中作为一级分类
class TestEditPage():
    '''编辑页面'''  # 测试类文档字符串，描述测试类的整体功能

    @allure.story("这是一个xxx的用例")  # 定义用户故事/测试场景，在报告中作为二级分类
    def test_1(self, login):
        '''用例描述：先登录，再去执行xxx'''  # 测试用例详细说明
        step_1()  # 执行测试步骤1
        step_2()  # 执行测试步骤2
        print("xxx")  # 输出测试执行结果

    @allure.story("打开a页面")  # 定义另一个用户故事/测试场景
    def test_2(self, login):
        '''用例描述：先登录，再去执行yyy'''  # 测试用例详细说明
        print("yyy")  # 输出测试执行结果


if __name__ == '__main__':
    # 注意生成测试报告 必须在命令行执行

    # pytest --alluredir reports testcase/pytest/test6.py
    # allure serve reports
    pytest.main(['--alluredir', './report', 'test6.py'])
