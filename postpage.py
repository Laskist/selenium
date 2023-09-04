from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class PostSearchLocators:
    LOCATOR_CREATE_NEW_POST_BTN = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_ENTER_TITLE_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_ENTER_DESCRIPTION_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_ENTER_CONTENT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_CREATE_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_CHECK_CREATE_POST_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')

class OperationsAddPost(BasePage):
    def click_create_new_post_button(self):
        logging.info("Click create new post button")
        self.find_element(PostSearchLocators.LOCATOR_CREATE_NEW_POST_BTN).click()

    def enter_title(self, text):
        logging.info(f"Send '{text}' to element {PostSearchLocators.LOCATOR_ENTER_TITLE_FIELD[1]}")
        login_field = self.find_element(PostSearchLocators.LOCATOR_ENTER_TITLE_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def enter_description(self, text):
        logging.info(f"Send '{text}' to element {PostSearchLocators.LOCATOR_ENTER_DESCRIPTION_FIELD[1]}")
        login_field = self.find_element(PostSearchLocators.LOCATOR_ENTER_DESCRIPTION_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def enter_contest(self, text):
        logging.info(f"Send '{text}' to element {PostSearchLocators.LOCATOR_ENTER_CONTENT_FIELD[1]}")
        login_field = self.find_element(PostSearchLocators.LOCATOR_ENTER_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def click_create_post_button(self):
        logging.info("Click create post button")
        self.find_element(PostSearchLocators.LOCATOR_CREATE_BTN).click()

    def check_title_new_post(self):
        check_title_new_post = self.find_element(PostSearchLocators.LOCATOR_CHECK_CREATE_POST_FIELD, time=3)
        return check_title_new_post.text
