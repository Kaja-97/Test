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
from telebot import types
from dotenv import load_dotenv
import selenium 
from datetime import datetime
import pytz
from selenium.webdriver.chrome.service import Service

config = load_dotenv(".env")

API_KEY=os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

########### telegram bot'''#########################################

## paper sending Function
@bot.message_handler(commands=['Paper'])
def paper(message):
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,user + '  \n Select Here or \n type and send me like this \n /Verrakesari  \n  /Thinakural ')

@bot.message_handler(commands=['Veerakesari'])
def paper(message):
    
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    country_time_zone = pytz.timezone('Asia/Kolkata')
    country_time = datetime.now(country_time_zone)
    today=country_time.strftime('%Y-%m-%d')
    
    
    for i in range(1,11):
        try:
            path="chromedriver.exe"
            options=webdriver.ChromeOptions()
            options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
            options.add_argument("--headless")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-sh-usage")
            servicee=Srtvice(os.environ.get("CHROMEDRIVER_PATH"))
            driver =webdriver.Chrome(servicee,options=options)
            driver.implicitly_wait(3)
        ###############################################################hhhhhhhhh######################
            ur='https://epaper.virakesari.lk/newspaper/Daily/main/{}#page-{}'.format(today,i)
    #         pagelist.append(ur)
            # driver =webdriver.Chrome(executable_path=r"C:\Users\kajan\Desktop\Python\Web Scraping\chromedriver",options=options)
            driver.get(ur)
            driver.implicitly_wait(5)
            soup=BeautifulSoup(driver.page_source,'html')
            paperpg=soup.find('img',id='pageImage')['src']
            driver.implicitly_wait(3)
            bot.send_photo(chat_id, paperpg, protect_content=True ,disable_notification=True)
        except Exception:
            bot.reply_to(message,user+'  Sorry , I can''t Send now, try again later')

            
@bot.message_handler(commands=['Thinakural'])
def paper(message):
    
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    
    
    
    for i in range(1,11):
        try:
            path="chromedriver.exe"
            options=webdriver.ChromeOptions()
            options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
            options.add_argument("--headless")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-sh-usage")
            servicee=Srtvice(os.environ.get("CHROMEDRIVER_PATH"))
            driver =webdriver.Chrome(servicee,options=options)
#             driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=options)
            driver.implicitly_wait(3)
        ###############################################################hhhhhhhhh######################
            
    #         pagelist.append(ur)
            # driver =webdriver.Chrome(executable_path=r"C:\Users\kajan\Desktop\Python\Web Scraping\chromedriver",options=options)
            url='http://www.epaper.thinakkural.lk/yarl-thinakkural/'
            pag=driver.get(url)
            
#             pagg=driver.page_source
            soup=BeautifulSoup(driver.page_source,'html')
#             soup=BeautifulSoup(pagg,'html.parser')
            glink=soup.find('div',id='inner_page_tile')
            ff=glink.find_all_next('a')
            
            for a,i in enumerate(ff,start=0):
                if a<10:
                    
                    lnk='http://www.epaper.thinakkural.lk/'+i['href'][2:]
                    #####
                    imga=requests.get(lnk)
                    driver.implicitly_wait(3)
                    imgg=imga.content
                    
                    bot.send_photo(chat_id, imgg, protect_content=True ,disable_notification=True)
            #         bot.send_photo(chat_id, paperpg, protect_content=True ,disable_notification=True)
                    #####
        except Exception:
            bot.reply_to(message,user + ' Sorry , I can''t Send now, try again later')

 ### Current Cut Schdl sending Function
@bot.message_handler(commands=['start'])
def greet(message):
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)

    bot.reply_to(message, f"Hey!  \n Welcome 😍 \n Please type your zone , (ex :- A  or W)  \n Do you want to read today News paper Type /Paper ")
    
@bot.message_handler(regexp='Hello'or'hello')
def scrap(message):
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,'Hi'+' '+user)

    
@bot.message_handler(regexp='Hi'or'hi')
def scrap(message):
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,'Hi'+' '+user)
    
@bot.message_handler(regexp='I love you'or'i love you')
def scrap(message):
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,'Me too 😍'+' '+user)

@bot.message_handler()
def scrap(message):
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=1927939875
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    if message.text.isdigit() :
        bot.reply_to(message,'type Your Zone (like A or B)')
    elif len(message.text)==1:
        lttr=message.text.upper()
        zz=str(lttr)
        scraper(zz)
        for i in A:
            bot.reply_to(message,i)
    else:
        bot.reply_to(message,'Please type Your Zone (like A or B)')
        
########### telegram bot'''#########################################
def scraper(x):
    #######################################################################################
    path="chromedriver.exe"
    options=webdriver.ChromeOptions()
    options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-sh-usage")
#     driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    servicee=Srtvice(os.environ.get("CHROMEDRIVER_PATH"))
    driver =webdriver.Chrome(servicee,options=options)
    ###############################################################hhhhhhhhh######################
    
    # driver =webdriver.Chrome(executable_path=r"C:\Users\kajan\Desktop\Python\Web Scraping\chromedriver.exe",chrome_options=options)
    url='https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule'
    pag=driver.get('https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule')
    driver.implicitly_wait(3)
    pagg=driver.page_source
    soup=BeautifulSoup(pagg,'html.parser')
    soup1=soup.find('div',class_="fc-scroller fc-time-grid-container")
    #soup1=BeautifulSoup(ss,'html.parser')
    a=soup1.find_all('a')
    global A
    if len(a)==0:
        A=['No Power Cut Today 🤔']
    else:

        Time=[]
        Zone=[]
        for a in a:
            time=a.find('div',class_='fc-time').text
            Time.append(time)
            zone=a.find('span',class_='badge border border-light text-light fw-500').getText()
            Zone.append(zone)
            
        dic={'Zone':Zone,'Time':Time}

        if x not in Zone:
            A='Please Type Correct Zone'
        else:
            table=pd.DataFrame(dic)
            AA=table[table['Zone']==x]
            code_html='*👇👇👇        👇👇👇*' 
            A=[]
            if AA.empty == False:
                for i in range(len(AA)):
                    B=code_html=code_html + '\n\n Zone:' + str((AA['Zone'].iloc[i])) +' - '+' Time: ' + str((AA['Time'].iloc[i]))
                    A.append(B)
                    

bot.polling()
