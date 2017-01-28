from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item


# todo tests should clean up database when complete

class HomePageTest(TestCase):

    def test_root_resolves_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_homepage_saves_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_homepage_redirects_after_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_save_only_as_needed(self):  # i.e. don't save empty items to the list,e.g. by simply visiting the page
        """
        in this test, use the default method (GET) and don't send any data with it, in that case nothing should be
        added to the database
        :return: n/a
        """
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(),0)

    def test_homepage_displays_all_items(self):

        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('itemy 1', response.content.decode())
        self.assertIn('itemy 2', response.content.decode())

class ItemModelTest(TestCase):

    def test_save_retrieve(self):

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_item.text, 'Item the second')