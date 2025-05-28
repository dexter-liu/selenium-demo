import pytest


@pytest.mark.do
def test1():
    print('test1')


@pytest.mark.do
def test2():
    print('test2')


# @pytest.mark.undo
@pytest.mark.undo
def test3():
    print('test333333')


# @pytest.mark.undo
@pytest.mark.undo
def test4():
    print('test444444')


if __name__ == '__main__':
    pytest.main(['-vs', '-m', 'do', 'test2.py'])
    # pytest.main(['-vs', '-m', '(do) and not (un)', 'test2.py'])
