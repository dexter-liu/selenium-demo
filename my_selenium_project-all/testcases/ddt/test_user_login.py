from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
import pytest



class TestUserLogin(object):
    login_data = [
        ('', 'jpress', '账号不能为空'),
        ('admin', 'jpress', '用户中心')
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8080/user/login')
        self.driver.maximize_window()
        self.logger = util.get_logger()
        self.logger.info('测试用户登录')

    @pytest.mark.parametrize('username, pwd, expected', login_data)
    def test_user_login(self, username, pwd, expected):
        # 输入用户名
        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.logger.debug('输入用户名称: %s', username)

        # 输入密码
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.logger.debug('输入用户密码: %s', pwd)

        # 点击登录
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        # 等待提示框
        if username == '':
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            sleep(3)
            try:
                assert alert.text == expected
            except AssertionError as ae:
                self.logger.error("hi, dexter：%s", "报错了", exc_info=1)

            alert.accept()

        else:
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            sleep(3)
            try:
                assert self.driver.title == expected
            except AssertionError as ae:
                self.logger.error("hi, dexter：%s", "报错了", exc_info=1)

    def teardown_class(self):
        self.driver.quit()
        self.logger.info('测试用户登录结束')
            

if __name__ == '__main__':
    pytest.main(['-sv', 'test_user_login.py'])