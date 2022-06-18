from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
#
# Config Selenium Options.
options = FirefoxOptions()
options.headless = True
service = Service(executable_path="/home/pin/.local/bin/geckodriver", log_path="/dev/null") ### DOCKER PATH
#service = Service(executable_path="./deps/geckodriver.exe") ### WINDOWS PATH
driver = webdriver.Firefox(options=options, service=service)
# Go to instructions URL.
driver.get('https://www.musica.com/letras.asp?letras=novedades')
all_songs_list = driver.find_elements(by=By.CSS_SELECTOR, value='article ul.listado-letras li > a')
links_lyrics = [song.get_attribute('href') for song in all_songs_list]
# Access to all songs content to extract song, author and lyrics and take ss.
songs = []
for link in links_lyrics:
    driver.get(link)
    # Get song and author.   
    song_data = driver.find_element(by=By.CSS_SELECTOR, value='.letra .info').text
    data_sorted = song_data.split("\n")
    # Get lyrics.
    lyrics_data =driver.find_elements(by=By.CSS_SELECTOR, value='.letra #letra > p')
    lyrics=''
    for paragraph in lyrics_data:
        lyrics = lyrics + (paragraph.text).replace("<br>", "").replace("\n"," ").replace(".",". ")
    # Delete trash content with JavaScript Executor.
    driver.execute_script("""
    var ads = document.querySelectorAll(".bnn");
    function trasher(element){
        element.parentNode.removeChild(element);
    }
    ads.forEach(function(ad){
        trasher(ad)
        });        
    trasher((document.querySelector(".opciones")));
    trasher((document.querySelector(".links1")));
    trasher((document.querySelector(".bocata")));
    trasher((document.querySelector("#header")));
    trasher((document.querySelector("#avisoinferior2")));
    trasher((document.querySelector("article .letra #letra aside a img")));
    trasher((document.querySelector("article .letra #letra div div img")));
    """)
    # Take ss (/home/pin/app/assets/screenshots/data_sorted[0].png).
    driver.find_element(by=By.ID, value='letra').screenshot('/home/pin/app/assets/screenshots/'+data_sorted[0]+'.png') ### DOCKER PATH
    #driver.find_element(by=By.ID, value='letra').screenshot('assets/screenshots/'+data_sorted[0]+'.png') ### WINDOWS PATH
    # Save songs data.
    song_dict = {
        'song': data_sorted[0],
        'author':data_sorted[1],
        'lyrics':lyrics
    }
    songs.append(song_dict)
# Export songs[] to CSV (songs.csv)
df = pd.DataFrame(songs)
df.to_csv('/home/pin/app/assets/songs.csv', index=False) ### DOCKER PATH
#df.to_csv('assets/songs.csv', index=False) ### WINDOWS PATH
driver.close()
    


