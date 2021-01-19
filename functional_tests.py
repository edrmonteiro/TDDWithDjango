import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn ('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('html')
        print('header.text=>', header.text)
        self.assertIn('To-Do', header.text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), "Enter a to-do item")
        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)



if __name__ == '__main__':
    unittest.main()

