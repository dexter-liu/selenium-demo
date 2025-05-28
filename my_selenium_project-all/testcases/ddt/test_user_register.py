from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
import pytest


class TestUserRegister(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8080/user/register')
        self.driver.maximize_window()

    login_data = [
        ('test001', 'test001@qq.com', '123456', '123456', '666', '验证码不正确'),
        ('test200', 'test009@qq.com', '123456', '123456', '111', '注册成功，点击确定进行登录。'),
    ]

    @pytest.mark.parametrize('username, email, pwd, confirmPwd, captcha, expected', login_data)
    def test1_register(self,username, email, pwd, confirmPwd, captcha, expected):
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

        if captcha != '666':
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

            # 验证
            assert alert.text == expected
            alert.accept()

            sleep(5)

        else:
            self.driver.find_element(By.NAME, 'captcha').clear()
            self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
            self.driver.find_element(By.CLASS_NAME, 'btn').click()

            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            # python的断言
            assert alert.text == expected
            alert.accept()
            sleep(5)

    def teardown_class(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-sv', 'test_user_register.py'])
