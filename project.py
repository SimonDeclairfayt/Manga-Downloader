import requests;
from bs4 import BeautifulSoup
import os;
from selenium import webdriver;

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Besoin de pip install : Requests bs4 os et selenium

def extract_name(url): 
      # Getting the last value of the split string
      file_name = url.split("/")[-1]
      return file_name ;

def downloadFiles(url,chapter):
    #Changing the value of the url to the desired value
    splitUrl = url.split("-");
    splitUrl[-1] = str(chapter) + ".html"
    newUrl = '-'.join(splitUrl)
    driver.get(url);
    soup = BeautifulSoup(driver.page_source,'html.parser');
    img = soup.find_all('img');
    #In pathDir put your on own file directory
    pathDir = "";
    while len(img)>2:
        os.chdir(pathDir);
        for image in img:
            # Best way to check if it's the right image
            if "https" in image['src'] and ".png" in image['src']:
                # Getting the name and link in memory
                name = extract_name(image['src']);
                link = image['src']
                # Creating a new directory
                dirName = name.split('-')[0];
                if not os.path.exists(os.path.join(pathDir,dirName)):
                    os.makedirs(dirName);
                    os.chdir(os.path.join(os.getcwd(),dirName));
                # We now isolate each link to download them with the right name
                # The next line we save all the img individually but let's try something else
                with open(name,'wb') as f:
                    im = requests.get(link);
                    f.write(im.content)
        chapter = chapter + 1;
        downloadFiles(newUrl,chapter)
    exit()
    
# What to add
## 
downloadFiles("https://mangasee123.com/read-online/Gantz-chapter-352.html",353);