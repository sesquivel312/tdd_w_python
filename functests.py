from selenium import webdriver
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

        # user will notice page title is 'To Do'

        self.assertIn('To-Do', self.browser.title)
        print('Got To-Do')
        self.fail('Finish writing the test!')

        # user is asked to enter a to-do item immediately

        # user types 'learn more python' into text box

        # when enter is pressed, page udpates and displays
        # 1: learn more python

        # text box for adding items is visible, user enters
        # 'buy crayons'

        # page updates again, showing both items

        # page displays some info about a URL from which to retrieve the 2do list

        # user visits that URL

if __name__ == '__main__':
    unittest.main()