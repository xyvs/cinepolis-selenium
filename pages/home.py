from selenium.webdriver.common.by import By
from utils.selects import randomSelectChoice

class CinepolisHome:
    URL = 'https://cinepolis.com'
    CITIES_SELECT = (By.CSS_SELECTOR, '#cmbCiudades')
    CINEMAS_SELECT = (By.CSS_SELECTOR, '#cmbComplejos')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def change_city(self):
        randomSelectChoice(self.driver, self.CITIES_SELECT)

    def change_cinema(self):
        randomSelectChoice(self.driver, self.CINEMAS_SELECT)
