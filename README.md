## Admetricks Challenge.
Capture and extract data from Internet (:

# The implemented solution
***
After analyzing the proposed problem I decided that this challenge will be solved with **Python** using **Selenium and Firefox** headless browser to navigate into the 
content of the **instructions pages**. With this technologies we **capture data requested.**

After this, with the help of some libraries we **extract data by exporting this into a CSV file and taking screenshots.**

In the first challenge (**songs.py**) I captured messy data, i.e. raw data obtained from the web, so the next step of the implementation is based on an extracting process. It need to sort and extract data following this example order:

    Song_data: 'This is a song for Miss Hedy Lamarr\nJeffBeck, Johnny Depp'

Then, the process sort author and song data by this way:

    data_sorted = song_data.split("\n")
    song_dict = {
        'song': data_sorted[0],
        'author':data_sorted[1],
        'lyrics':lyrics
    }

The same situation with the lyrics of the songs. The extracting process append each paragraph of the lyrics song in a string.

    for paragraph in lyrics_data:
        lyrics = lyrics + (paragraph.text).replace("<br>", "").replace("\n"," ").replace(".",". ")
 
 To take a **clean screenshot**  the extracting process remove trash content. So, it select ads, menu and others junk elements. (Removed with **javascript executor.** )
    
    driver.execute_script("""
    var ads = document.querySelectorAll(".bnn");
    function trasher(element){
        element.parentNode.removeChild(element);
    }
    ads.forEach(function(ad){
        trasher(ad)
    });
    """)
    
In the second challenge (**stories.py**) the DOM content (of instructions url) **never** loaded the elements that contain the data requested. The **capture process** need to visit the iframe's href to get the elements that contain the stories data.

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

.


