from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
### pdb
import pdb

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
### pdb
        # pdb.set_trace()
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
        expected_html= render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
