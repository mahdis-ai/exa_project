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

users=['twhiddleston','maddenrichard','tomhardy','courtneycoxofficial','alysonhannigan','nph','davidbeckham']
#search for the hashtag cat
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
follow_info=soup.find_all('span',class_="g47SY lOXF2")
print(name.text)
print(bio)
print(website.text)
post_info=soup.find('div',class_="Nnq7C weEfm")
posts_link=post_info.find_all('a',attrs={'tabindex':'0'})
for post in posts_link:
    print(post.href)

for i in follow_info:
    print(i.text)


#soup=BeautifulSoup(r.text,'html.parser')
#info=soup.find_all('div',class_="v9tJq AAaSh VfzDr")

#fname=info.find('h1',class_="rhpdm")
#print(fname.get_text())