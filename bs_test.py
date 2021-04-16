import requests
from bs4 import BeautifulSoup
import json 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time
from bs4 import BeautifulSoup
import re 
path=os.getcwd()
path=os.path.join(path,"bs_data")
os.mkdir(path)
driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
driver.get('https://www.instagram.com/')
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
#username_of_any_instagram_acount
username.send_keys("")
password.clear()
#password_of_that_acount
password.send_keys("ma99911225")
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

users=['twhiddleston','jlo','jenhawkins_','courteneycoxofficial','piawurtzbach']

#for i in range(0,len(users)):

searchbox.send_keys(users[0])
 
# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(10)
i=0
while(i<len(users)):
    data={}
    path=os.path.join(path,users[i])
    os.mkdir(path)
    path=os.path.join(path,"data.json")
    soup=BeautifulSoup(driver.page_source,'html.parser')
    value=soup.find_all('div',class_="v9tJq AAaSh VfzDr")
    name=soup.find('h1',class_="rhpdm")
    website=soup.find('a',class_="yLUwa")
    bio=soup.find('div',class_="-vDIg").span.string
    follow_section=soup.find_all('span',class_="g47SY")
    data['posts']=[]
    data['name']=name.text
    data['bio']=bio
    data['website']=website.text
    data['post_numbers']=follow_section[0].text
    data['followers']=follow_section[1].text
    data['followings']=follow_section[2].text
    post_info=soup.find('div',class_="Nnq7C weEfm")
    links=post_info.find_all('a')

    for link in links:
        driver.get('https://www.instagram.com/'+link.get('href'))
        detail=BeautifulSoup(driver.page_source,'html.parser')
        post_text=detail.find('div',class_="C7I1f X7jCj")
        like_section=detail.find('div',class_="Nm9Fw")
        likes=like_section.find('a',class_="zV_Nj").span.text
        caption=post_text.find('span',class_="").text
    #caption=re.findall(r'<span class="" title="Edited">(.*)</span>',post_text.text)
        if len(caption)=='':
            caption='no caption'
        pic=detail.find('img')
        video=detail.find('video')
        if pic==None:
            image=video.get('poster')
        else:
            image=pic.get('src')
        data['posts'].append({'image':image, 'like':likes,'caption':caption})
        time.sleep(10)
    json_object=json.dumps(data)
    with open(path,"w") as f: 
        f.write(json_object)
    path=os.getcwd()
    path=os.path.join(path,"bs_data")
    i+=1
    driver.get('https://www.instagram.com/'+users[i])
    time.sleep(10)

