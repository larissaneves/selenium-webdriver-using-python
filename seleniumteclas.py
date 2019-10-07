import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="driver/chromedriver")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Test")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Results", driver.find_element_by_tag_name('h3').text)

    def tearDown(self):
        self.driver.close()