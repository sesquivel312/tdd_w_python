from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item, List


class HomePageTest(TestCase):

    def test_root_resolves_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class ListAndItemModelTest(TestCase):

    def test_save_retrieve(self):

        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):

    def test_list_template_used(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' % (list_.id,))
        self.assertTemplateUsed(response, 'list.html')

    # def test_display_all_items(self):
    #     list_ = List.objects.create()
    #     Item.objects.create(text='itemy1', list=list_)
    #     Item.objects.create(text='itemy2', list=list_)
    #
    #     response = self.client.get('/lists/single-list/')
    #
    #     self.assertContains(response, 'itemy1')
    #     self.assertContains(response, 'itemy2')

    def test_display_specific_list(self):
        correct_list = List.objects.create()  # add a new list to the List model/table
        Item.objects.create(text='itemy1', list=correct_list)
        Item.objects.create(text='itemy2', list=correct_list)

        other_list = List.objects.create()  # add another list
        Item.objects.create(text='other item 1', list=other_list)
        Item.objects.create(text='other item 2', list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id,))

        self.assertContains(response, 'itemy1')
        self.assertContains(response, 'itemy2')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')

    def test_passes_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()  # create two new lists to compare when visiting a particular one

        # goto url for adding to existing list - i.e. the list to check against
        response = self.client.get('/lists/%d/' % (correct_list.id,))

        self.assertEqual(response.context['list'], correct_list, 1)


class NewListTest(TestCase):
    def test_saves_post(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_post(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))


class NewItemTest(TestCase):

    def test_save_post_to_existing_list(self):

        other_list = List.objects.create()
        correct_list = List.objects.create()  # create two new lists to compare when visiting a particular one

        # goto url for adding to existing list - i.e. the list to check against
        self.client.post('/lists/%d/add_item' % (correct_list.id,), data={'item_text': 'new item on existing list'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()  # get the item we just created
        self.assertEqual(new_item.text, 'new item on existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirect_to_list_view(self):

        other_list = List.objects.create()
        correct_list = List.objects.create()  # create two new lists to compare when visiting a particular one

        # goto the url to create a new list and capture the response for checking
        response = self.client.post('/lists/%d/add_item' % (correct_list.id,),
                                    data={'item_text': 'new item on existing list'})

        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))
