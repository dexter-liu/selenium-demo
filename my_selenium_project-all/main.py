from testcases import testcase1,testcase02
from util import util
from selenium import webdriver
import time
import unittest
# from testcases.basic.test_user_register import TestUserRegister
# from testcases.basic.test_user_login import TestUserLogin
# from testcases.basic.test_admin_login import TestAdminLogin
# from testcases.basic.test_category import TestCategory
# from testcases.basic.test_article import TestArticle
from testcases.unittest import \
    test_user_register, \
    test_user_login, \
    test_admin_login, \
    test_category,test_article_bak

if __name__ == '__main__':

    # 20-47行诗basic的测试用例
    # testcase1.test1()
    # testcase02.test2()
    # print(util.gen_random_str())

    # driver = webdriver.Chrome()
    # driver.get('http://127.0.0.1:8080/user/register')
    # driver.maximize_window()
    # # time.sleep(10)
    # print(util.get_code(driver, 'captchaimg'))

    # case01 = TestUserRegister()
    # case01.test_register_code_error()
    # case01.test_register_ok()

    # case02 = TestUserLogin()
    # case02.test_user_login_username_error()
    # case02.test_user_login_ok()

    # login = TestAdminLogin()
    # login.test_admin_login_code_ok()

    # case04 = TestCategory(login)
    # case04.test_add_category_error()
    # case04.test_add_category_ok()
    # case05 = TestArticle(login)
    # case05.test_add_ok()
    # case05.test_delete_one_article_ok()
    # case05.test_delete_all_article_ok()

    # 50-57行是unittest的测试用例
    adminLoginCase = test_admin_login.TestAdminLogin('test_admin_login_code_ok')
    categoryCase = test_category.TestCategory('test_add_category_ok', adminLoginCase)

    suite = unittest.TestSuite()
    suite.addTest(adminLoginCase)
    suite.addTest(categoryCase)
    runner = unittest.TextTestRunner()
    runner.run(suite)



