from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]')
    input1.send_keys('Tim')

    input2 = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]')
    input2.send_keys('Gr')

    input3 = browser.find_element(By.CSS_SELECTOR, '[name = "email"]')
    input3.send_keys('FF')

    file_input = browser.find_element(By.CSS_SELECTOR, '#file')
    file_input.send_keys('C:/Users/Timofey/PycharmProjects/Project_QA_1/text.txt')

    button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button.click()



finally:
    time.sleep(5)
    browser.quit()
