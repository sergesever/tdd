from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_and_retrieve_a_list(self):
        # open url
        self.browser.get('http://localhost:8000')

        # check title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # enter a to-do item invitation

        # type 'first' to-do

        # update page, with to-do item in the list

        # add 'another' to-do item

        # update page showing both items in the list

        # generate unique URL for user

        # visit hte URL - to-do list is here

        # quit app

if __name__ == '__main__':
    unittest.main(warnings='ignore')
