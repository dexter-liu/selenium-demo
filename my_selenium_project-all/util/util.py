import pickle
import random
import string
import time
import logging
import logging.handlers
import datetime
from lib.chaojiying import Chaojiying_Client

from PIL import Image
import os

from selenium.webdriver.common.by import By


def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    path =os.path.dirname(os.path.dirname(__file__))+'/logs'
    log_path = path + '/all.log'

    rf_handler = logging.handlers.TimedRotatingFileHandler(log_path, when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


def get_code(driver, id):
    # 获取验证码图片
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots'
    picture_name1 = path + '/' + str(t) + '.png'

    driver.save_screenshot(picture_name1)

    ce = driver.find_element(By.ID, id)

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    dpr = driver.execute_script('return window.devicePixelRatio')

    print(dpr)
    im = Image.open(picture_name1)
    img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))

    t = time.time()

    picture_name2 = path + '/' + str(t) + '.png'
    img.save(picture_name2)  # 这里就是截取到的验证码图片

    chaojiying = Chaojiying_Client('dexterliu', '2019Sep!', '969807')
    im_d = open(picture_name2, 'rb').read()
    # print(chaojiying.PostPic(im_d, 8001))
    verify_code = chaojiying.PostPic(im_d, 8001)['pic_str']
    # print(verify_code)
    return verify_code

# 生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
