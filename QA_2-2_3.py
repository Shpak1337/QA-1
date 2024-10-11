from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = ('https://suninjuly.github.io/selects1.html')
    browser = webdriver.Chrome()
    browser.get(link)

    num1_elem = browser.find_element(By.CSS_SELECTOR, '#num1')
    num1 = num1_elem.text
    num2_elem = browser.find_element(By.CSS_SELECTOR, '#num2')
    num2 = num2_elem.text
    sum = int(num1) + int(num2)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_visible_text(str(sum))

    button = browser.find_element(By.CSS_SELECTOR, '[type = submit]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
