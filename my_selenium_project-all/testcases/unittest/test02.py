import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')

    @classmethod
    def setUpClass(cls):
        # print('setUpClass')
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com')
        cls.driver.maximize_window()

    def test1(self):
        print('test1')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()

    def test2(self):
        print('test2')

    @classmethod
    def tearDownClass(cls):
        # print('tearDownClass')
        sleep(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
