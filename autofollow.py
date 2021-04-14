from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="/Users/Public/Downloads/chromedriver.exe")
driver.get("https://www.instagram.com/")
sleep(2)
driver.find_element_by_xpath("//input[@name=\"username\"]") \
    .send_keys("r13034")  # Login
driver.find_element_by_xpath("//input[@name=\"password\"]") \
    .send_keys("14201030rr")  # Senha
driver.find_element_by_xpath('//button[@type="submit"]') \
    .click()
sleep(2)
if driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]"):
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
        .click()
    sleep(3)
if driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]"):
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
        .click()
    sleep(3)

for i in range(30):
    for c in range(25):
        driver.find_element_by_xpath('//button[text()="Follow"]') \
            .click()
        sleep(5)
    driver.refresh()
