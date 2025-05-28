from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
from lib.HTMLTestRunner import HTMLTestRunner

import unittest


class TestUserRegister(unittest.TestCase):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://127.0.0.1:8080/user/register')
    #     self.driver.maximize_window()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://127.0.0.1:8080/user/register')
        cls.driver.maximize_window()

    # 测试登录验证码错误
    def test_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确'

        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'email').send_keys(email)

        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME,'confirmPwd').send_keys(confirmPwd)

        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python 的断言
        # assert alert.text == expected

        # 重写，使用unittest的断言
        self.assertEqual(alert.text, expected)
        alert.accept()
        sleep(5)

    # 测试成功
    def test_register_ok(self):
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        # 自动获取
        captcha = ''
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        # email
        self.driver.find_element(By.NAME, 'email').clear()
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        # 密码
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element(By.NAME, 'confirmPwd').clear()
        self.driver.find_element(By.NAME, 'confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, 'captchaimg')

        # 输入验证码
        self.driver.find_element(By.NAME, 'captcha').clear()
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)

        # 点击注册
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证，python断言
        # assert alert.text == expected

        # 重写为unittest的断言
        self.assertEqual(alert.text, expected)
        alert.accept()

        self.driver.close() # 关闭当前浏览器窗口
        self.driver.quit() # 完全退出WebDriver并释放资源

    def runTest(self):
        self.test_register_code_error()
        self.test_register_ok()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestUserRegister))

    with open(r"./result.html", "wb") as fp:
        runner = HTMLTestRunner(stream=fp, title="test register", description="用例执行情况")
        runner.run(suite)
        runner.generateReport(suite)



