import unittest

from selenium import webdriver
from Resources.PO.Pages import LoginPage, MainPage


class TestWLYLoginBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class TestWLYLogin(TestWLYLoginBase):
    def setUp(self):
        super().setUp();

    def test_WLY_Login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()
        self.MainPage = MainPage(self.driver)
        self.MainPage.checkloginname()

    def tearDown(self):
        super().tearDown();


if __name__ == "__main__":
    unittest.main()
