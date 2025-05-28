from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from testcases.pytest.test_admin_login import TestAdminLogin
import pytest

class TestArticle(object):
    def setup_class(self):
        self.login = TestAdminLogin()

    # 测试添加文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_add_ok(self):
        title = '我的文章'
        content = '我的文章内容'
        expected = '文章保存成功。'

        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(3)
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        sleep(3)

        # self.login.driver.find_element(By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a').click()
        # sleep(1)

        self.login.driver.find_element(By.ID, 'article-title').send_keys(title)
        sleep(3)

        # 切入iframe
        frame1 = self.login.driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(frame1)
        sleep(1)
        self.login.driver.find_element(By.XPATH, '/html/body').send_keys(content)

        # 切出iframe
        self.login.driver.switch_to.default_content()
        self.login.driver.find_element(By.XPATH, '//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

    # 测试删除单个文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_delete_one_article_ok(self):
        # 点击文章
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击文章管理
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)
        link = self.login.driver.find_element(By.XPATH,
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')
        ActionChains(self.login.driver).move_to_element(link).perform()

        sleep(3)
        # 删除前文章数
        article_num = len(self.login.driver.find_elements(By.CLASS_NAME, 'jp-actiontr'))

        # 找到垃圾箱WebElement,然后点击
        del_elem = self.login.driver.find_element(By.XPATH,
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]')
        del_elem.click()

        sleep(3)

        # 删除后文章数
        article_num2 = len(self.login.driver.find_elements(By.CLASS_NAME, 'jp-actiontr'))

        assert article_num == article_num2 + 1

    # 测试删除所有文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_delete_all_article_ok(self):
        # 点击文章
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击文章管理
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        link = self.login.driver.find_element(By.XPATH,
            '/html/body/div[1]/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input')
        # /html/body/div[1]/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input
        # 原始的/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input
        link.click()

        self.login.driver.find_element(By.ID, 'batchDel').click()

        WebDriverWait(self.login.driver, 5).until(EC.alert_is_present())
        alert = self.login.driver.switch_to.alert
        alert.accept()
        sleep(1)

        # 删除后文章数
        artile_num = self.login.driver.find_elements(By.CLASS_NAME, 'jp-actiontr')
        assert len(artile_num) == 0


if __name__ == '__main__':
    pytest.main(['-sv', 'test_article.py'])
