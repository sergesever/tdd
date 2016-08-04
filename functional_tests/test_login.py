from .base import FunctionalTest
import time
from selenium.webdriver.support.ui import WebDriverWait


class LoginTest(FunctionalTest):
    def test_login_with_persona(self):
        # go to site, check 'sign in' link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('login').click()

        # Persona login box
        self.switch_to_new_window('Mozilla Persona')

        # log in with email
        # use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
            ).send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # close Persona window
        self.switch_to_new_window('To-Do')

        # check if user is logged in
        self.wait_for_element_with_id('logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )
