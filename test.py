from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.common.exceptions import ElementNotInteractableException

import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://qa-mesto.praktikum-services.ru/signin')


driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys('deleteme@yandexxx.ru')
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys('1')
driver.find_element(By.CSS_SELECTOR, 'button[class="auth-form__button"]').click()


wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="profile__image"]'))).click()
userpic_url = 'https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png'
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="avatar"]'))).send_keys(userpic_url)
time.sleep(5) # специально поставил что бы было видно что элемент есть на странице, виден и кликабелен
try:
    driver.find_element(By.CSS_SELECTOR, 'button[class="button popup__button"]').click()
except ElementNotInteractableException:
    print('class - not work')
    try:
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    except ElementNotInteractableException:
        print('type not work')
        driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div/form/button[2]').click()



time.sleep(3)
driver.quit()