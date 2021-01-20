from selenium.webdriver.common.by import By

class CinepolisMovieDetail:
    VIDEO_CONTAINER = (By.CSS_SELECTOR, 'video')
    DESCRIPTION_CONTAINER = (By.CSS_SELECTOR, '#ContentPlaceHolder1_ctl_sinopsis_ctl_sinopsis')

    def __init__(self, driver):
        self.driver = driver

    def get_video(self):
        video = driver.find_element(*RANGE_OPTION)
        print(video)

    def get_description(self):
        description = driver.find_element(*RANGE_OPTION)
        print(description.text)

