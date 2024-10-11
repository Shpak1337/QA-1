from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    input1.send_keys('Timofey')

    input2 = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    input2.send_keys('Grigoriev')

    input3 = browser.find_element(By.CSS_SELECTOR, '[class="form-control city"]')
    input3.send_keys('Saint-Peterburg')

    input4 = browser.find_element(By.CSS_SELECTOR, '#country')
    input4.send_keys('Russian Federation')

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    sleep(5)
    browser.quit()