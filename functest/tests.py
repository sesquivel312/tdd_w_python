#!/usr/bin/env python

# todo adjust model such that items are associated with a specific list
# todo unique url for each list
# todo url for adding a new list (POST)
# todo url for adding a new item to a given list (POST)

import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/steve/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def helper_check_text_in_table(self, test_text):

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(test_text, [row.text for row in rows])

    def test_start_and_retrieve_list(self):
        # insert "user story" verbiage in comments...
        # alice wants to use this to-do list app, they will open the URL in their browser

        self.browser.get(self.live_server_url)

        # alice will notice page title is 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # alice is asked to enter a to-do item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # alice types 'Buy peacock feathers' into text box
        inputbox.send_keys('Buy peacock feathers')

        # when enter is pressed, alice is taken to a *NEW* page, for this list, and the page displays
        # 1: Buy peacock feathers
        inputbox.send_keys(Keys.ENTER)

        alice_url = self.browser.current_url

        self.assertRegex(alice_url, '/lists/.+')
        self.helper_check_text_in_table('1: Buy peacock feathers')

        # text box for adding items is visible, alice enters
        # 'Use feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')

        inputbox.send_keys('Use feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # page updates again, showing both items
        self.helper_check_text_in_table('1: Buy peacock feathers')
        self.helper_check_text_in_table('2: Use feathers to make a fly')

        # new user bob visits site
        ## close browser session to ensure no traces of it are left in the next (cookies, etc.)
        self.browser.quit()
        self.browser = webdriver.Chrome('/home/steve/bin/chromedriver')

        # bob doesn't see alice's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # bob starts new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Milk')
        inputbox.send_keys(Keys.ENTER)

        # bob gets his URL
        bob_url = self.browser.current_url
        self.assertRegex(bob_url, '/lists/.+')
        self.assertNotEqual(bob_url, alice_url)

        # still no items from alice's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Peacock Feathers', page_text)
        self.assertIn('Buy Milk', page_text)
