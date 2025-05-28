import pytest


# 不会执行，不符合命名规则
def add():
    assert (1 + 2) == 3


def test_sub():
    assert 2 - 1 == 1


class TestRegister(object):
    def test_register(self):
        assert len('admin') == 5


if __name__ == '__main__':
    # pytest.main(['-s', '-v', '01-pytest简介.py::test_sub'])
    pytest.main(['-s', '-v', 'test1.py::TestRegister::test_register']) # 标记测试函数，如果是使用pycharm运行的话，test_sub()测试方法也会执行

