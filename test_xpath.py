# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SiteAngular(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="driver/chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_site_angular(self):
        driver = self.driver
        driver.get("http://localhost:4200/login")
        driver.find_element_by_id("mat-input-0").click()
        driver.find_element_by_id("mat-input-0").clear()
        driver.find_element_by_id("mat-input-0").send_keys("teste")
        driver.find_element_by_id("mat-input-1").click()
        driver.find_element_by_id("mat-input-1").clear()
        driver.find_element_by_id("mat-input-1").send_keys("teste")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forget Password'])[1]/following::button[1]").click()
        self.assertEqual("SB Admin Material", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search'])[1]/preceding::div[1]").text)
        self.assertEqual("Helium", driver.find_element_by_xpath("/html/body/app-root/app-layout/div/app-dashboard/div[2]/div/table/tbody/tr[2]/td[contains(text(),'Helium')]").text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


