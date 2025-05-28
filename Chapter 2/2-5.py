from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form1.html'
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys('admin')
        pwd = self.driver.find_element(By.ID,'pwd')
        pwd.send_keys('123')

        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))


        self.driver.find_element(By.ID,'submit').click()
        self.driver.switch_to.alert.accept()

        sleep(2)

        username.clear()
        pwd.clear()

        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_login()
