from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep

# 连接到Grid Hub
hub_url = "http://localhost:4444/wd/hub"  # 默认Hub地址

firefox_options = FirefoxOptions()
# firefox_options.platform_name = 'ANY'  # 跨平台, 推荐使用set_capability方法
firefox_options.set_capability('platformName', 'ANY')


driver = webdriver.Remote(hub_url, options=firefox_options)
driver.get('https://www.baidu.com')
print(driver.title)
sleep(30)
driver.quit()

