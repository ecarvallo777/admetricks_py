from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
#
# Config Selenium Options.
options = FirefoxOptions()
options.headless = True
service = Service(executable_path="/home/pin/.local/bin/geckodriver")
#service = Service(executable_path="./deps/geckodriver.exe")
driver = webdriver.Firefox(options=options, service=service)
#Go to instructions URL.
driver.get('https://www.musica.com/letras.asp?letras=novedades')
all_songs_list = driver.find_elements(by=By.CSS_SELECTOR, value='article ul.listado-letras li > a')
links_hrefs = [song.get_attribute('href') for song in all_songs_list]
# def to sort data.
# Data extract example:
# THIS IS A SONG FOR MISS HEDY LAMARR\nJeff Beck ft. Johnny Depp
def separateData(song_data):
    x = song_data.split("\n")
    return print(x)
# Access to all songs content to extract song, author and lyrics and take ss.
songs = []
for link in links_hrefs:
    driver.get(link)   
    song_data = driver.find_element(by=By.CSS_SELECTOR, value='.letra .info').text
    separateData(song_data)
    #author = driver.find_element(by=By.CSS_SELECTOR, value='.letra .info h1').text
    song_dict = {
        'song': song_data,
        'author':'sda',
        'lyrics':'s'
    }
    songs.append(song_dict)
    #print(songs)
