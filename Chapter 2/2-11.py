from selenium import webdriver
from time import sleep

# http://sahitest.com/demo
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.get('http://sahitest.com/demo/clicks.htm')

    def test_mouse(self):
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/clicks.htm')

        btn = self.driver.find_element(By.XPATH,'/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()

        sleep(2)

        btn = self.driver.find_element(By.XPATH,'/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()

        sleep(2)

        btn = self.driver.find_element(By.XPATH,'/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()

        sleep(5)

    def test_key(self):
        self.driver.get('http://www.baidu.com')
        # kw = self.driver.find_element(By.ID,'kw')
        # kw.send_keys('selenium')
        # kw.send_keys(Keys.CONTROL,'a')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'x')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'v')
        # sleep(2)

        e = self.driver.find_element(By.LINK_TEXT,'新闻')
        print(e)
        ActionChains(self.driver).move_to_element(e).click(e).perform()
        sleep(2)

if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    case.test_key()
    case.driver.quit()
