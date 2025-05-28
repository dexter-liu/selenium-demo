from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class TestUserLogin(unittest.TestCase):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://127.0.0.1:8080/user/login')
    #     self.driver.maximize_window()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://127.0.0.1:8080/user/login')
        cls.driver.maximize_window()

    # 测试用户登录，用户名错误
    def test_user_login_username_error(self):
        # 用户名为空
        username = ''
        pwd = '123456'
        expected = '账号不能为空'

        # 输入用户名
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        # 输入密码
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        # 等待提示框
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        sleep(3)
        # 验证，使用python断言
        # assert alert.text == expected

        # 重写，使用unittest的断言
        self.assertEqual(alert.text, expected)
        alert.accept()

        # self.driver.quit()


    # 测试用户登录成功
    def test_user_login_ok(self):
        # 用户名为空
        username = 'admin'
        pwd = 'jpress'
        expected = '用户中心'

        # 输入用户名
        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        # 输入密码
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        # 等待提示框
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        sleep(3)
        # 验证，使用python断言
        # assert self.driver.title == expected

        # 重写，使用unittest的断言
        self.assertEqual(self.driver.title, expected)

        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
