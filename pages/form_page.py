import os.path

from locators.form_page import FormPageLocators


class FormPage:

    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = 'index.html'
    LOCATION = os.path.join(file_dir, file_name)

    def __init__(self, browser):
        self.browser = browser

    @property
    def firstname_input(self):
        return self.browser.find_element(*FormPageLocators.FIRST_INPUT)

    @property
    def lastname_input(self):
        return self.browser.find_element(*FormPageLocators.LAST_INPUT)

    @property
    def submit_button(self):
        return self.browser.find_element(*FormPageLocators.SUBMIT_BUTTON)

    def load(self):
        self.browser.get(self.LOCATION)

    def clear_form(self):
        self.firstname_input.clear()
        self.lastname_input.clear()

    def enter_firstname(self, firstname):
        self.firstname_input.clear()
        self.firstname_input.send_keys(firstname)

    def enter_lastname(self, lastname):
        self.lastname_input.clear()
        self.lastname_input.send_keys(lastname)

    def submit(self):
        self.submit_button.click()

    def firstname_input_value(self):
        return self.firstname_input.get_attribute('value')

    def lastname_input_value(self):
        return self.lastname_input.get_attribute('value')