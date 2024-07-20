from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_user_name(self):
        try:
            self.find_element(locator='#user-name.input_error.form_input')
        except NoSuchElementException:
            return False
        return True

    def exist_password(self):
        try:
            self.find_element(locator='#password.input_error.form_input')
        except NoSuchElementException:
            return False
        return True
