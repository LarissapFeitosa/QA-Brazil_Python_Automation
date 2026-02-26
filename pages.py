from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.to, 'to')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location (self, from_text):
        self.driver.find_element (*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_location (self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def test_order_2_ice_creams(self):
        numbers_of_icre_creams = 2
        for count in range(numbers_of_icre_creams):

    def get_to_location_value (self):
        return WebDriverWait(self.driver, 3).until(
    EC.visibility_of_element_located(self.to_field)
    ).get_attribute('value'):

