#In this, I have used Beautiful to import a list of songs from Saavn.
#I have used the playlist shown in the code for this Project.
#Since the source code mentions the song multiple times, I have removed the duplicates using excel. This can be done in Python as well.
"""
Created on Sat Nov  2 23:13:14 2019

@author: user
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome()

songs=[] #List to store name of the song

driver.get("https://www.jiosaavn.com/s/playlist/4ba60ea5f92f9a23420dd219a7ea3914/Hindi_%F0%9F%96%A4/zt02fyOlt3Uwkg5tVhI3fw__")
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('div',href=False, attrs={'itemprop':'track'}):
    songs.append(a.find("meta", itemprop="name",content=True)["content"])

songs=list(set(songs))
df=pd.DataFrame(songs,columns=['Songs'])
df.to_excel("C:\\Users\\user\\Documents\\songs.xlsx")

