from selenium import webdriver
import os
os.environ["DISPLAY"] = ":0"
driver_path = "/var/www/html/proxy/proxy_login/geckodriver"
driver = webdriver.Firefox()

#driver = webdriver.Chrome('./chrome_rasp',chrome_options=options)
site = "http://msftconnecttest.com/redirect"
driver.get(site)
user = driver.find_element_by_name("user")
user.send_keys("luiz")
password = driver.find_element_by_name("password")
password.send_keys("luiz123")
agree = driver.find_element_by_name("agree")
agree.click();	
login=driver.find_element_by_xpath("//input[@value='Login']")
login.click()
driver.close()
