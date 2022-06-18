## Admetricks Challenge.
Capture and extract data from Internet (:

# The implemented solution
***
After analyzing the proposed problem I decided that this challenge will be solved with **Python** using **Selenium and Firefox headless browser** to navigate into the 
content of the **instructions url's** and then, **get elements with the data requested** (needing CSS selectors of the page content).

Finally, **export data and take screenshots.**

In the first challenge (**songs.py**) I found messy data, i.e. raw data obtained from the web, so my implementation is based on an extracting process. It gets elements with the data requested (song and author) following this example order:

    Song_data: 'This is a song for Miss Hedy Lamarr\nJeffBeck, Johnny Depp'

Then, the process access to author and song data by this way:

    data_sorted = song_data.split("\n")
    author = data_sorted[0]
    song = data_sorted[1]

The same situation with the lyrics of the songs. The extracting process append each paragraph of the lyrics song in a string.

    for paragraph in lyrics_data:
        lyrics = lyrics + (paragraph.text).replace("<br>", "").replace("\n"," ").replace(".",". ")
 
 To take a **clean screenshot**  the extracting process remove trash content. So, it selected ads, menu and others junk elements. (Removed with **javascript executor.** )
    
    driver.execute_script("""
    var ads = document.querySelectorAll(".bnn");
    function trasher(element){
        element.parentNode.removeChild(element);
    }
    ads.forEach(function(ad){
        trasher(ad)
    });
    """)
    
In the second challenge (**stories.py**) the DOM content (of instructions url) **never** loaded the elements that contain the data requested. The scrapping algorithms need to visit the iframe's href to get the elements that contain the stories data.

So, when the DOM content was loaded. Its get the iFrame HREF.

    # Go iFrame URL.
    src = driver.find_element(by=By.CSS_SELECTOR, value='.mat-mix-anchor').get_attribute('src')
    driver.get(src)

**Hashlib library:** To convert the img src into MD5<br>
**Pandas library:** To export data to CSV.

# Base project modifications:
***
In **DOCKERFILE:**

    Add to COPY command:
        songs.py stories.py
    
    Add to MKDIR command:
         # Add assets dirs.
         (...)
         mkdir /home/pin/app/assets/ && \
         mkdir /home/pin/app/assets/ads/ && \
         mkdir /home/pin/app/assets/screenshots/
         
    Add to RUN command:
        pip install pandas
        
# How to run?
***

    Workdir folder: /home/pin/app/ (Default folder when you open shell in the docker container.)

**To run the first challenge,** please stay in the **workdir folder** and type this command:

    python3 songs.py

**To run the second challenge,** please stay in the **workdir folder** and type this command:

    python3 stories.py



