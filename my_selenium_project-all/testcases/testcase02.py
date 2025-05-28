import time

from selenium import webdriver
from PIL import Image
import pytesseract
from selenium.webdriver.common.by import By


def test1():
    #打开谷歌浏览器
    browser = webdriver.Chrome()
    #打开首页
    browser.get("http://127.0.0.1:8080/user/register")
    browser.maximize_window()

    #获取验证码图片
    t = time.time()
    # print(t)
    picture_name1 = str(t)+'.png'
    browser.save_screenshot(picture_name1)

    ce = browser.find_element(By.ID, "captchaimg")
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    # 抠图
    img = im.crop((left, top, right, height))

    t = time.time()
    picture_name2 = str(t)+'.png'

    img.save(picture_name2)#这里就是截取到的验证码图片
    browser.close()


def test2():
    image1 = Image.open('test.png')
    str1 = pytesseract.image_to_string(image1)
    print(str1)
    print(f'验证码是：{str1}')