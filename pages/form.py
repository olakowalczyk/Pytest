from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path

class FormPage:

    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = 'index.html'
    LOCATION = os.path.join(file_dir, file_name)
    FIRST_INPUT = (By.ID, 'firstname-input')
    LAST_INPUT = (By.ID, 'lastname-input')
    SUBMIT_BUTTON = (By.ID, 'submit-button')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.LOCATION)

    def clear_form(self):
        firstname_input = self.browser.find_element(*self.FIRST_INPUT)
        firstname_input.clear()
        lastname_input = self.browser.find_element(*self.LAST_INPUT)
        lastname_input.clear()

    def enter_firstname(self, firstname):
        firstname_input = self.browser.find_element(*self.FIRST_INPUT)
        firstname_input.clear()
        firstname_input.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_input = self.browser.find_element(*self.LAST_INPUT)
        lastname_input.clear()
        lastname_input.send_keys(lastname)

    def submit(self):
        submit_click = self.browser.find_element(*self.SUBMIT_BUTTON)
        submit_click.click()

    def firstname_input_value(self):
        firstname_input = self.browser.find_element(*self.FIRST_INPUT)
        return firstname_input.get_attribute('value')

    def lastname_input_value(self):
        lastname_input = self.browser.find_element(*self.LAST_INPUT)
        return lastname_input.get_attribute('value')