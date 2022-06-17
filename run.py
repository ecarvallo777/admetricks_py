from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
#
# Config Selenium Options.
options = FirefoxOptions()
options.headless = True
#service = Service(executable_path="/home/pin/.local/bin/geckodriver")
service = Service(executable_path="./deps/geckodriver.exe")
driver = webdriver.Firefox(options=options, service=service)
#Go to instructions URL.
driver.get('https://www.musica.com/letras.asp?letras=novedades')
all_songs_list = driver.find_elements(by=By.CSS_SELECTOR, value='article ul.listado-letras li > a')
links_hrefs = [song.get_attribute('href') for song in all_songs_list]
# Access to all songs content to extract song, author and lyrics and take ss.
songs = []
for link in links_hrefs:
    driver.get(link)   
    song= driver.find_element(by=By.CSS_SELECTOR, value='.letra .info h1').text
    print(song)
