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
data={}
url='https://www.instagram.com/twhiddleston/'
driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
driver.get('https://www.instagram.com/twhiddleston')
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
username.send_keys("mahdis_abd78")
password.clear()
password.send_keys("ma99911225")
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

users=['twhiddleston','missmayim','juventus','courtneycoxofficial','piawurtzbach','johnlegend','davidbeckham']
data={}
#for i in range(0,len(users)):

searchbox.send_keys(users[0])
 
# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(10)
soup=BeautifulSoup(driver.page_source,'html.parser')
value=soup.find_all('div',class_="v9tJq AAaSh VfzDr")
name=soup.find('h1',class_="rhpdm")
website=soup.find('a',class_="yLUwa")
bio=soup.find('div',class_="-vDIg").span.string
follow_section=soup.find_all('ul',class_="k9MGp")
follow_info=follow_section.find_all('span',class_="g47SY")
data['posts']=[]
data['name']=name.text
data['bio']=bio
data['website']=website.text
data['post_numbers']=follow_info[0].text
data['followers']=follow_info[1].text
data['followings']=follow_info[2].text
post_info=soup.find('ul',class_="Nnq7C weEfm")
links=post_info.find_all('a')
for link in links:
    driver.get('https://www.instagram.com/twhiddleston'+link.get('href'))
    detail=BeautifulSoup(driver.page_source,'html.parser')
    post_text=detail.find('div',class_="C4VMK")
    like_section=detail.find('div',class_="Nm9Fw")
    likes=like_section.find('a').text
    caption=re.findall(r'<span class="" title="Edited">(.*)</span',post_text.text)
    if len(caption)==0:
        caption.append('no caption')
    image=detail.find('img').get('src')
    data['posts'].append({'image':image, 'like':likes,'caption':caption[0]})
    time.sleep(10)

#soup=BeautifulSoup(r.text,'html.parser')
#info=soup.find_all('div',class_="v9tJq AAaSh VfzDr")

#fname=info.find('h1',class_="rhpdm")
#print(fname.get_text())