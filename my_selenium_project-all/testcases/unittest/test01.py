import unittest


class LoginTestCase(unittest.TestCase):

    # setUp()方法在每一个方法执行前都会被调用
    def setUp(self) -> None:
        print('准备工作')

    # tearDown()方法在每一个方法执行后都会被调用
    def tearDown(self) -> None:
        print('还原工作')

    def test_login(self):
        username = 'tom'
        pwd = '123'
        expected = 'welcome'
        self.assertEqual(expected, 'welcome')

    def test01(self):
        print('test01')
        self.assertEqual(1+2, 3)

    def test02(self):
        print('test02')
        self.assertGreaterEqual(5, 4)

    def aaa(self):
        print('aaa')
        self.assertGreaterEqual(1, 2)

if __name__ == '__main__':
    unittest.main()

