from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

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

#This function removes all text aceepts the temp value
def clean_text(text):
  """Extracts only the temperature from tex"""
  output = float(text.split(": ")[1]) #this will create an erray and the temp number is the 2nd element
  return output

#This functions creates a text file that stores the temperatured captured at a specific date and time
def write_file(text):
  """Write input text into a text file"""
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, 'w') as file:
    file.write(text)
    
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
  time.sleep(2)
  
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  #time.sleep(1)
  text = str(clean_text(element.text))
  
  write_file(text)

print(main())
