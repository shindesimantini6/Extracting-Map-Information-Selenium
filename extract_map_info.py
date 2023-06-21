#%%

# Import all required packages
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
cookielib = http.cookiejar
from config import USERNAME
from config import PASSWORD


#%%

# Open the sign in page and put in your email address and id
url = "https://www.pilze-deutschland.de/mitglied/signin/"
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome-beta"
driver = webdriver.Chrome(options=chrome_options, service = Service(ChromeDriverManager().install()))

# Ask the driver to get the url
driver.get(url)

# Add a wait variable 
wait = WebDriverWait(driver,20)

# Add a few seconds sleep till the url opens up
time.sleep(5)

# Add username and password 
search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_username"]')))
search.send_keys(USERNAME)
search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_password"]')))
search.send_keys(PASSWORD)
driver.find_element("xpath",'//*[@id="account"]/div[4]/div/div[2]/fieldset/form/div[3]/input').click()
print('Found and added the username and password location')

# Find the German map with mushroom locations and click on it
driver.find_element("xpath", '//*[@id="tree-menu-organismen"]/a').click()
driver.find_element("xpath", '//*[@id="search-results"]/h5[1]/a').click()
driver.find_element("xpath", '//*[@id="rightmap"]/a/img').click()
print('Clicked on the Map')



#%%

# el = driver.find_element("xpath", '//*[@id="findspot_info_inner"]')

# print("Element found")

# Click on the Map with an offset of 1 and extract any existing information at that point
action = webdriver.common.action_chains.ActionChains(driver)
for i in range(37, 60):
    print(i)
    action.move_by_offset(i, 33)
    action.click()
    action.perform()
    print("Action executed")
    # driver.find_element("xpath", '//*[@id="findspot_info"]/p[3]')
    time.sleep(5)

# %%
