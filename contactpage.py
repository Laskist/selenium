from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class ContactLocators:
    LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_US_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')


class OperationsContact(BasePage):
    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(ContactLocators.LOCATOR_CONTACT_BTN).click()

    def enter_name_contact_us(self, text):
        logging.info(f"Send '{text}' to element {ContactLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(ContactLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(text)

    def enter_email_contact_us(self, text):
        logging.info(f"Send '{text}' to element {ContactLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(ContactLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(text)

    def enter_contact_us(self, text):
        logging.info(f"Send '{text}' to element {ContactLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}")
        contact_field = self.find_element(ContactLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        contact_field.clear()
        contact_field.send_keys(text)

    def click_contact_us_button(self):
        logging.info("Click contact_us button")
        self.find_element(ContactLocators.LOCATOR_CONTACT_US_BTN).click()


    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert().text
        logging.info(text)
        return text

