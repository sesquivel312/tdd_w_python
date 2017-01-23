#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/steve/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_start_and_retrieve_list(self):
        # insert "user story" verbiage in comments...
        # user wants to use this to-do list app, they will open the URL in their browser

        self.browser.get('http://localhost:8000')

        # user will notice page title is 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user is asked to enter a to-do item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # user types 'learn more python' into text box
        inputbox.send_keys('Buy peacock feathers')

        # when enter is pressed, page udpates and displays
        # 1: learn more python
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peackock feathers' for row in rows), 'New todo item not in table')

        # text box for adding items is visible, user enters
        # 'buy crayons'
        self.fail('Finish writing tests')

        # page updates again, showing both items

        # page displays some info about a URL from which to retrieve the 2do list

        # user visits that URL

if __name__ == '__main__':
    unittest.main()