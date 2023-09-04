from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_ERR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_AUTH_FIELD = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    # LOCATOR_CREATE_NEW_POST_BTN = (By.XPATH, '//*[@id="create-btn"]')
    # LOCATOR_ENTER_TITLE_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    # LOCATOR_ENTER_DESCRIPTION_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    # LOCATOR_ENTER_CONTENT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    # LOCATOR_CREATE_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    # LOCATOR_CHECK_CREATE_POST_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_PASSWORD_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASSWORD_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERR_FIELD[1]}")
        return text

    def get_auth_text(self):
        auth_check = self.find_element(TestSearchLocators.LOCATOR_AUTH_FIELD, time=3)
        return auth_check.text


