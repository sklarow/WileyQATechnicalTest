# For simplicity, I put all the 3 pages (Base, Login and Main) in one file.

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Resources.Locators import Locators
from Resources.TestData import TestData


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self):
        self.click(Locators.LOGIN_BUTTON)
        self.enter_text(Locators.LOGIN_TEXTBOX, TestData.LOGIN)
        self.click(Locators.NEXT_BUTTON)
        self.enter_text(Locators.PASSWORD_TEXTBOX, TestData.PASSWORD)
        self.click(Locators.SUBMIT_BUTTON)


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def checkloginname(self):
        self.assert_element_text(Locators.LOGIN_NAME_TEXT, TestData.LOGIN_NAME_EXPECTED)
