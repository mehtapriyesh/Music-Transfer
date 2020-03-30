#In this, I have used Beautiful to import a list of songs from Saavn.
#I have used the playlist shown in the code for this Project.
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:13:14 2019

@author: user
"""

from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

songs=[] #List to store name of the song
driver=urlopen("https://www.jiosaavn.com/s/playlist/4ba60ea5f92f9a23420dd219a7ea3914/Hindi_%F0%9F%96%A4/zt02fyOlt3Uwkg5tVhI3fw__")
soup = BeautifulSoup(driver.read())


for a in soup.findAll("p", {"class":"song-name ellip"}):
    for n in a:
        songs.append(n)
   

