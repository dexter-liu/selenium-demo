from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/test_alert.html'
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element(By.ID,'alert').click()
        # 切换到alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element(By.ID,'confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        # confirm.accept()
        #
        sleep(3)
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element(By.ID,'prompt').click()
        sleep(3)
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(3)
        prompt.accept()
        sleep(5)


if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
    case.driver.quit()