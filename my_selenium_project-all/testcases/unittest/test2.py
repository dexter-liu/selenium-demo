import unittest

class MyTestCase02(unittest.TestCase):

    def setUp(self) -> None:
        print('每次都运行：setUp')

    @classmethod
    def setUpClass(cls) -> None:
        print('运行一次：setUpClass')

    def test1(self):
        print('test1')
        self.assertEqual(1, 1)
        self.assertIn(1, [1, 2, 3])

    def test2(self):
        print('test2')
        self.assertLess(1, 2)
        self.assertGreater(2, 1)

    def tearDown(self) -> None:
        print('每次都运行：tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('运行一次：tearDownClass')

if __name__ == '__main__':
    unittest.main()

# unittest.main()是unittest模块提供的主要入口点，它会自动触发当前文件中所有以test开头的方法的执行。按照测试方法的名称顺序执行测试。