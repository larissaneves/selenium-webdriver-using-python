# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

class PesquisarCEP(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="driver/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_pesquisar_c_e_p(self):
        driver = self.driver
        wait = WebDriverWait(driver,40)
        driver.get("http://www.buscacep.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.tituloimagem > h3:nth-child(1)')))
        driver.find_element_by_name("relaxation").click()
        driver.find_element_by_name("relaxation").clear()
        driver.find_element_by_name("relaxation").send_keys("69050750")
        driver.find_element_by_name("tipoCEP").click()
        Select(driver.find_element_by_name("tipoCEP")).select_by_visible_text("Localidade/Logradouro")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Não utilize nº de casa/apto/lote/prédio ou abreviação'])[1]/following::option[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sim'])[1]/following::input[1]").click()
        self.assertEqual("Conjunto Jussara ", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CEP:'])[1]/following::td[1]").text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
