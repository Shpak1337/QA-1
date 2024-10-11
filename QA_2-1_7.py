from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = chest.get_attribute('valuex')
    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)

    capcha = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    capcha.click()

    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
