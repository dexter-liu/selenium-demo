from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest


class TestCategory(unittest.TestCase):
    def __init__(self, method, login):
        super().__init__(method)
        self.login = login

    # 测试文章分类失败，名称为空
    def test_add_category_error(self):
        name = ''
        # 前置条件 后置条件
        parent = 'python'
        slug = 'test'
        expected = '分类名称不能为空'

        # 点击文章
        #
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击分类
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        sleep(1)

        # 输入分类名称
        self.login.driver.find_element(By.NAME, 'category.title').send_keys(name)

        # 选择父分类
        parent_category_elem = self.login.driver.find_element(By.NAME, 'category.pid')
        # Select()将普通WebElement转换为可操作的选择框对象，select_by_visible_text()通过选项的可见文本选择。
        # 同时支持select_by_value()通过选项的value属性选择或者select_by_index()通过选项的索引选择。
        Select(parent_category_elem).select_by_visible_text(parent)

        # 输入slug
        self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)

        # 点击添加
        self.login.driver.find_element(By.XPATH,
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        # assert msg == expected
        self.assertEqual(msg, expected)

    # 测试文章分类成功
    def test_add_category_ok(self):
        name = 'test'
        parent = 'python'
        slug = 'test'
        expected = None

        # 点击文章
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击分类
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        sleep(1)

        # 输入分类名称
        self.login.driver.find_element(By.NAME, 'category.title').clear()
        self.login.driver.find_element(By.NAME, 'category.title').send_keys(name)

        # 选择父分类
        parent_category_elem = self.login.driver.find_element(By.NAME, 'category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        # 输入slug
        self.login.driver.find_element(By.NAME, 'category.slug').clear()
        self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)

        # 点击添加
        self.login.driver.find_element(By.XPATH,
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        # 没有异常就添加成功，没有提示信息
        # assert 1 == 1
        self.assertEqual(1, 1)

    def runTest(self):
        self.test_add_category_error()
        self.test_add_category_ok()

if __name__ == '__main__':
    unittest.main()

