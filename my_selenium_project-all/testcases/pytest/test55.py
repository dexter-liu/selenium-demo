import pytest

def setup_module():
    print('setup module')

def teardown_module():
    print('teardown_module')

def setup_function():
    print('setup_function')

def teardown_function():
    print('teardown_function')

def test1():
    print('test1')

def test2():
    print('test2')

if __name__ == "__main__":
    pytest.main(['sv', 'test55.py'])