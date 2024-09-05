from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get('https://search.google.com/search-console/removals')

# Login and navigate to URL removal
driver.find_element(By.ID, 'identifierId').send_keys('your-email@example.com')
driver.find_element(By.ID, 'identifierNext').click()
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('your-password')
driver.find_element(By.ID, 'passwordNext').click()

urls_to_remove = ['url1', 'url2', 'url3']

for url in urls_to_remove:
    driver.get('https://search.google.com/search-console/removals/new-request')
    time.sleep(2)
    url_input = driver.find_element(By.XPATH, 'xpath-to-url-input-field')
    url_input.send_keys(url)
    submit_button = driver.find_element(By.XPATH, 'xpath-to-submit-button')
    submit_button.click()
    time.sleep(2)  # Allow some time for the submission to process

driver.quit()

