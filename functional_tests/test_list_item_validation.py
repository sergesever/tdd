from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empy_list_items(self):
        # accidentally hit ENTER on empty box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # refresh home page and show an error message
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You can\'t have an empty list item')

        # try again with some text, it works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # try to submit second blank item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # show similar warning
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'you cannot have an empty list item')

        # correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Buy tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('1: Buy tea')
