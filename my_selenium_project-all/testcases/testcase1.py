from selenium.webdriver.common.by import By


def test1():
    print('test1----dexter is debugging')

from selenium import webdriver
from time import sleep
import pyautogui

def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')  # 该网址已经不可用
    driver.maximize_window()
    sleep(2)
    elem = driver.find_element(By.ID, 'agree')
    rect = elem.rect
    pyautogui.click(rect['x']+10, rect['y']+130)
    # pyautogui.click()

    sleep(3)

    # elem.click()


