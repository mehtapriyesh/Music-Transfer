#This is the playlist created using the songs imported in importer file. 
#Here's a link to the file finally created: https://open.spotify.com/user/5iy98ghl127jum98em5mheygd/playlist/0apU7PxpFpLJlAqXToNJ2I?si=ppxFEoFnS1CqK5P1ZZru8g
"""
Created on Tue Nov 19 11:30:54 2019

@author: user
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from pandas import DataFrame
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from time import sleep

ignored_exceptions=(StaleElementReferenceException)
   
def wdwfind(path):
    return WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH,(path))))

def wdwclick(path):
    return WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable((By.XPATH,(path))))

email=str(input('Enter your Email'))
psw=str(input('Enter your Password'))



#Opening Spotify
driver=webdriver.Chrome()    
driver.maximize_window()
driver.get("https://open.spotify.com")
actionChain = ActionChains(driver)
    

#login procedure
wdwclick("//*[text()='Log in']").click()
wdwfind("//input[@id='login-username']").send_keys(email)
wdwfind("//input[@id='login-password']").send_keys(psw)
wdwclick("//button[@id='login-button']").click()

#songs is a list containing list of all the songs. Shown in importer file of same repsoitory.
    
sleep(1.5) #Break    

#Beginning the Search


for song in songs:
    try:
        wdwclick("//li[2]/div/a/div/span").click()
        wdwfind("//input").send_keys(song) #sending elements to navigation bar
        item = wdwfind("//div[@class='react-contextmenu-wrapper']/div/div/a")
        print (item.text)
        actionChains = ActionChains(driver)
        actionChains.context_click(item).perform()
        element = wdwclick("//*[text()='Add to Playlist']")
        element.click()
        wdwclick("//div[@class='mo-coverArt-hoverContainer']").click() #clicking on the playlist to add the song to
        clear=wdwclick("//input[@class='_2f8ed265fb69fb70c0c9afef329ae0b6-scss']").send_keys(Keys.SHIFT,Keys.ARROW_UP,Keys.BACKSPACE) #clearing the search box
        sleep(1)
    except:
        sleep(1)
        clear=wdwclick("//input[@class='_2f8ed265fb69fb70c0c9afef329ae0b6-scss']").send_keys(Keys.SHIFT,Keys.ARROW_UP,Keys.BACKSPACE) #clearing the search box
        print(song)
        pass
    
driver.quit()        
    
 
    
    
    
    
    
    
    
    
    
