#!/usr/bin/env python
# coding: utf-8

# # Web Scraping Instagram with Selenium

# In[126]:


#imports here
from pathlib import Path
from Funtions import *
from tkinter import *
from root import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
import os
import wget


# ## Download ChromeDriver
# Now we need to download latest stable release of ChromeDriver from:
# <br>
# https://chromedriver.chromium.org/

# In[127]:






def Scraper(window,Target):


    #specify the path to chromedriver.exe (download and save on your computer)
    driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
    driver.get("http://www.instagram.com")

    #target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    Username = 'Jcon_Sinder'
    Password = "ea}S>`'\"4^-ETy~C"
    # Name = Jcon Sinder

    #enter username and password
    username.clear()
    username.send_keys(Username)
    password.clear()
    password.send_keys(Password)

    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    #We are logged in!


    # In[128]:


    #nadle NOT NOW
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


    # ## Search keywords

    # In[130]:



    #target the search input field
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()

    #search for the hashtag cat
    keyword = Target
    searchbox.send_keys(keyword)
     
    # Wait for 5 seconds
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)


    # In[131]:

    def GeremoveTextAndOrganized():
        el = driver.find_element_by_tag_name('body')
        text = el.text
        text = text[0:-566]
        text = text.split()
        return text



    # In[132]:
    def seveJsonFile(data):
        nameOfFile = f"{Target}\Details.json"
        with open(nameOfFile,"w") as file:
            json.dump(data, file)
            print("Saved File")

    #scroll down to scrape more images
    driver.execute_script("window.scrollTo(0, 4000);")

    #target all images on the page
    images = driver.find_elements_by_tag_name('img')
    images = [image.get_attribute('src') for image in images]
    images = images[:-2]

    print('Number of scraped images: ', len(images))


    # ## Save images to computer
    # 
    # First we'll create a new folder for our images somewhere on our computer.
    # <br>
    # Then, we'll save all the images there.

    # In[139]:




    path = os.getcwd()
    path = os.path.join(path,f'{Target}')

    #create the directory
    os.mkdir(path)

    print(path)


    # In[136]:


    text = GeremoveTextAndOrganized()
    data = [{
        "Name" : text[0]
    },
    {
        text[7] : text[6]
    },
    {
        text[3] : text[2]
    },
    {
        text[5] : text[4]
    },
    {
        "bio" : text[8:-5]
    }
]


    seveJsonFile(data)


    # In[137]:


    #download images
    counter = 0
    for image in images:
        save_as = os.path.join(path, keyword + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1

    window.destroy()
    
    
# In[ ]:




