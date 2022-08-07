#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import os
import time
import chromedriver_binary
import telebot
#from telebot import types
from dotenv import load_dotenv
config = load_dotenv(".env")





path="chromedriver.exe"
options=webdriver.ChromeOptions()
options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-sh-usage")

API_KEY=os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


########### telegram bot'''#########################################
@bot.message_handler
def test_start(message):
  if msg.startswith('/test'):
    bot.send_message(message.chat.id,'Hi Please enter your zone (ex : -  /W)')


@bot.message_handler(commands=['W'])
def greet(message):
    bot.reply_to(message, mmm)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() =='Hello':
        bot.send_message(message.chat.id, message.text.upper() )
    elif message.text.lower() =='Bye':
        bot.send_message(message.chat.id,'see you soom' )
    elif message.text.lower() == 'I love you':
        bot.send_sticker(message.chat.id, 'API_KEY')
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

########### telegram bot'''#########################################
driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
url='https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule'
pag=driver.get('https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule')
pagg=driver.page_source


soup=BeautifulSoup(pagg,'html.parser')
soup1=soup.find('div',class_="fc-scroller fc-time-grid-container")





gg=soup1.find_all('a')
Time=[]
Zone=[]

for a in gg:
    time=a.find('div',class_='fc-time').text
    Time.append(time)
    zone=a.find('span',class_='badge border border-light text-light fw-500').getText()
    Zone.append(zone)

dic = {'Zone': Zone, 'Time': Time}
table = pd.DataFrame(dic)
tt = table[table['Zone'] == 'W']
mmm = str(tt)

bot.polling()





