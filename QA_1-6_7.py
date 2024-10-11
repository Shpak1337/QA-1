from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    link = 'http://suninjuly.github.io/huge_form.html'
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, 'input')

    for element in elements:
        element.send_keys("ff")

    button = browser.find_element(By.CSS_SELECTOR, '[type = "Submit"]')
    button.click()
finally:
    sleep(5)
    browser.quit()
