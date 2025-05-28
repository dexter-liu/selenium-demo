from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    sleep(1)
    # driver.find_element_by_id('kw').send_keys('selenium')
    # old "find_element_by_id" is obsoleted
    driver.find_element(by='kw').send_keys('selenium')
    sleep(1)
    # driver.find_element_by_id('su').click()
    driver.find_element(by='su').click()
    sleep(3)
    driver.quit()


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()


    def test(self):
        self.driver.get('http://www.baidu.com')
        sleep(1)
        # self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(1)
        # self.driver.find_element_by_id('su').click()
        self.driver.find_element(By.ID, 'su').click()

        sleep(3)
        self.driver.quit()


# def test():
#     import subprocess
#     p = subprocess.Popen("chromedriver")
#     p.communicate()


if __name__ == '__main__':
    # test()
    case = TestCase()
    case.test()