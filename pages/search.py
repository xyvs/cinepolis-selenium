from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random

class CinepolisSearch:
    RANGE_OPTION = (By.CSS_SELECTOR, '#slider-range .ui-slider-handle:nth-child(3)')
    MOVIES_CONTAINER = (By.CSS_SELECTOR, '.listaCarteleraHorario .divComplejo')
    MOVIES_LINKS = (By.CSS_SELECTOR, '.tituloPelicula[data-oculto="0"] .datalayer-movie')
    HOURS_CONTAINER = (By.CSS_SELECTOR, '.btnhorario')

    def __init__(self, driver):
        self.driver = driver

    def change_hours(self):
        self.driver.execute_script('$("#slider-range").slider("values", [9, 15])')
        self.driver.find_element(*self.RANGE_OPTION).click()

    def wait_for_movies(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".listaCarteleraHorario .divComplejo")))

    def check_hours(self):
        hours = self.driver.find_elements(*self.HOURS_CONTAINER)
        hours = set([hour.text for hour in hours if hour.text])
        print(hours)

    def choose_random_movie(self):
        movies_container = self.driver.find_element(*self.MOVIES_CONTAINER)
        movies = movies_container.find_elements(*self.MOVIES_LINKS)
        random.choice(movies).click()

