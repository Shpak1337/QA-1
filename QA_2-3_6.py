from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, 'button')
    button1.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_elem = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_elem.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
