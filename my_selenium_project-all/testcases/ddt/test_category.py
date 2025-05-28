from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from testcases.ddt.test_admin_login import TestAdminLogin
import pytest


class TestCategory(object):
    def setup_class(self):
        self.login = TestAdminLogin()

    category_data = [
        ('', 'python', 'test', '分类名称不能为空'),
        ('test', 'python', 'test', '')
    ]

    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('name, parent, slug, expected', category_data)
    def test_add_category(self, name, parent, slug, expected):
        if name == '':
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

        if name == '':
            loc = (By.CLASS_NAME, 'toast-message')
            WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
            msg = self.login.driver.find_element(*loc).text
            assert msg == expected
        else:
            assert 1 == 1

    def teardown_class(self):
        self.login.driver.quit()

if __name__ == '__main__':
    pytest.main(['-sv', 'test_category.py'])

