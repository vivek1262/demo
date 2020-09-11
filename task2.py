from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.facebook.com")
driver.find_element_by_name("email").send_keys("9492716980")
sleep(5)
driver.find_element_by_name("pass").send_keys("Svivek123#")
sleep(5)
driver.find_element_by_name("login").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/i").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[5]/div/div[1]/div[2]/div/div/div/div/span").click()

driver.close()

print("success")