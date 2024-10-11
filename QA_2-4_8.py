from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(14)

    price = browser.find_element(By.XPATH, '//h5[text() = "$100"]')

    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    x_elem = browser.find_element(By.ID, 'input_value')
    x = x_elem.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(5)
    browser.quit()