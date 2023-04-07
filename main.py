from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
  #Set options to make Browsing easier
  options =webdriver.ChromeOptions()
  options.add_argument("disable-infobars") #disbaled popup bars to prevent confusion
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disbale-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver
  
def main():
  driver = get_driver()
  #Here I tell the script to find the user name field and enter the username
  driver.find_element(by="id",value="id_username").send_keys("automated")
  time.sleep(1)
  #Here I tell the script to find the password field and enter the password and hit enter when done to log in
  driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+Keys.RETURN)
  time.sleep(1)
  #after logging in we click the home button
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  print(driver.current_url)

print(main())
