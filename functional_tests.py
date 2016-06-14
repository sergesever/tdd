from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# pdb
# import pdb


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_and_retrieve_a_list(self):
        # open url
        self.browser.get('http://localhost:8000')

        # check title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # enter a to-do item invitation
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # type 'first' to-do
        inputbox.send_keys('Buy peacock feathers')

        # update page, with to-do item in the list
# pdb
#        pdb.set_trace()
        inputbox.send_keys(Keys.ENTER)

# debug
        import time
        time.sleep(3)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # add another to-do item

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

# debug
        time.sleep(3)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # update page showing both items in the list
        self.fail('Finish the test')

        # generate unique URL for user

        # visit hte URL - to-do list is here

        # quit app

if __name__ == '__main__':
    unittest.main(warnings='ignore')
