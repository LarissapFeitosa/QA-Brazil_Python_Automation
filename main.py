from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

import data
import helpers
from pages import UrbanRoutesPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time



class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        from selenium import webdriver
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes.")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page: UrbanRoutesPage(self.driver)
        routes_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO

    def test_select_plan (self):
    def test_fill_phone_number (self):
    def test_fill_card (self):
    def test_comment_for_driver(self):
    def test_order_blanket_and_handkerchiefs(self):
    def test_car_search_model_appears(self):

    @classmethod
    def teardown_class(cls):


cls.driver.quit()
