# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class Alert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="driver/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_alert(self):
        driver = self.driver
        driver.get("https://hvacnhurry.com/")
        driver.find_element_by_css_selector("#menu-item-107 > a:nth-child(1)").click()
        driver.find_element_by_id("login_email").click()
        driver.find_element_by_id("login_email").clear()
        driver.find_element_by_id("login_email").send_keys("j")
        driver.find_element_by_id("login_pwd").click()
        driver.find_element_by_id("login_pwd").clear()
        driver.find_element_by_id("login_pwd").send_keys("u")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Auth Page'])[2]/following::button[1]").click()
        alert = driver.switch_to.alert
        self.assertEqual("Login Error: The email address is badly formatted.", alert.text)
        alert.accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
