import unittest

class MyTestCase05(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass...')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass...')

    def test05(self):
        print('test05...')

    def test06(self):
        print('test06...')
