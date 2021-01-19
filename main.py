from selenium.webdriver import Chrome

URL = "https://cinepolis.com"

with Chrome() as driver:
    driver.get(URL)

