from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_elem.text
    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)

    capcha = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    capcha.click()

    browser.execute_script("window.scrollBy(0, 200);")

    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()