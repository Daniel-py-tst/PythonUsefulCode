import time
import random
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver") #Replace with driver filename
browser.get("Site")


user_input = browser.find_element_by_id('Username element')

time.sleep(1)

username = ""

for letter in username:
    user_input.send_keys(letter)
    wait_time = random.randint(0,1000)/1000
    time.sleep(wait_time)

password_input = browser.find_element_by_id('Password element')

time.sleep(1)

password = ""

for letter in password:
    password_input.send_keys(letter)
    wait_time = random.randint(0,1000)/1000
    time.sleep(wait_time)

signin_button = browser.find_element_by_id("Login button element")

signin_button.click()
