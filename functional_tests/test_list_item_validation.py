from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empy_list_items(self):
        # accidentally hit ENTER on empty box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # refresh home page and show an error message
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You can\'t have an empty list item')

        # try again with some text, it works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # try to submit second blank item
        self.get_item_input_box().send_keys('\n')

        # show similar warning
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You can\'t have an empty list item')

        # correct it by filling some text in
        self.get_item_input_box().send_keys('Buy tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Buy tea')

    def test_can_not_add_duplicate_items(self):
        # start a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # try to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # show error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You\'ve already got this in your list')
