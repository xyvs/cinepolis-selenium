from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import random

def randomSelectChoice(driver, element):

    select_div = driver.find_element(*element)
    options = select_div.find_elements(By.TAG_NAME, 'option')[1:]
    random_choice = random.choice(options).text

    select = Select(select_div)
    select.select_by_visible_text(random_choice)

    print(random_choice)

    return random_choice
