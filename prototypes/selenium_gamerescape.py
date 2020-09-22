from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import json

with open('passwords.json', 'r') as f:
    passwords = json.load(f)

# Open blank browser
browser = webdriver.Chrome(passwords['chromedriver_location'])

# Shorthand
find_xpath = browser.find_element_by_xpath
find_css = browser.find_element_by_css_selector

# Items can be:
# 1. craftable
#    //*[@id="mw-content-text"]/div/table[2]/tbody/tr[3]/td[1]/table[4]/tbody/tr[2]/td/div/table
# 2. levequestable
#    
#    Example: https://ffxiv.gamerescape.com/wiki/Adamantite_Helm_of_Fending
# 