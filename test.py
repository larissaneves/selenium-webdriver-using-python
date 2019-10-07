import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="driver/chromedriver")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_pesquisar_sobre_teste_no_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.find_element_by_name("q").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("teste")
        driver.find_element_by_name("btnK").click()
        self.assertEqual("TESTE DE VELOCIDADE da Internet | Velocimetro | Speed Test", driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Resultados da Web'])[1]/following::h3[3]").text)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)