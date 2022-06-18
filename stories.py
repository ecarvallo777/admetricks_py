from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import hashlib
# Config Selenium Options.
options = FirefoxOptions()
options.headless = True
service = Service(executable_path="/home/pin/.local/bin/geckodriver", log_path="/dev/null") ### DOCKER PATH
#service = Service(executable_path="./deps/geckodriver.exe") ### WINDOWS PATH
driver = webdriver.Firefox(options=options, service=service)
# Def to encrypt the img src.
def filenameEncrypted(str):
    hash_object = hashlib.md5(str.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash+'.png'
# RUN :) .
# Go to instructions URL.
driver.get('https://as.com/diarioas/america.html')
# In this case, we need to **visit the iframe url to scrape** into the page content
# Because, the DOM content loaded never showed the selectors of the elements that
# Contain the data requestd.
#
# Go iFrame URL.
src = driver.find_element(by=By.CSS_SELECTOR, value='.mat-mix-anchor').get_attribute('src')
driver.get(src)
# Access to all stories content to extract href, description and ss w/ filename encrypted.
stories_data = driver.find_elements(by=By.CSS_SELECTOR, value='.slick-track a')
stories = []
for story in stories_data:
    href = story.get_attribute('href')
    description = story.find_element(by=By.CSS_SELECTOR, value='img').get_attribute('alt')
    filename = filenameEncrypted(story.find_element(by=By.CSS_SELECTOR, value='img').get_attribute('src'))
    story_dict = {
        'href' : href,
        'description' : description,
        'filename' : filename,
    }
    stories.append(story_dict)
    # Take SS to div content.
    story.screenshot('/home/pin/app/assets/ads/'+story_dict['filename']) ### DOCKER PATH.
    #story.screenshot('assets/ads/'+story_dict['filename']) ## WINDOWS PATH.
# Export stories[] to CSV (stories.csv)
df = pd.DataFrame(stories)
df.to_csv('/home/pin/app/assets/stories.csv', index=False) ### DOCKER PATH
#df.to_csv('assets/stories.csv', index=False) ### WINDOWS PATH
driver.close()