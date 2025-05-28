from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util
import pytest


class TestAdminLogin(object):

    admin_login_data = [
        # ('admin', 'jpress', '666', '验证码不正确，请重新输入'),
        ('admin', 'jpress', '111', 'JPress后台')
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8080/admin/login')
        self.driver.maximize_window()

    @pytest.mark.dependency(name="admin_login")
    @pytest.mark.parametrize('username, pwd, captcha, expected', admin_login_data)
    def test_admin_login(self, username, pwd, captcha, expected):
        # 输入用户名
        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)

        # 输入密码
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)

        # 清除，然后获取验证码
        self.driver.find_element(By.NAME, 'captcha').clear()
        if captcha != '666':
            captcha = util.get_code(self.driver, 'captchaImg')

        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        if captcha == '666':
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            try:
                assert alert.text == expected
                alert.accept()
            except AssertionError as ae:
                print(f'hi, dexter, login failed, error message is {ae}')
            sleep(5)
        else:
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            assert expected == self.driver.title
            sleep(5)

    # def teardown_class(self):
    #     self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-sv','test_admin_login.py'])