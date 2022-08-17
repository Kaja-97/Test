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
    chat_id=message.from_user.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,user + '  \n Select Here or \n type and send me like this \n /Veerakesari  \n ')
@bot.message_handler(commands=['TT'])
def paper(message):
    country_time_zone = pytz.timezone('Asia/Kolkata')
    country_time = datetime.now(country_time_zone)
    today=country_time.strftime('%Y-%m-%d %H-%M-%S')
    Dayname=country_time.strftime('%A %T')
    bot.reply_to(message,Dayname )
    bot.reply_to(message,today )
    
@bot.message_handler(commands=['Veerakesari'])
def Veerakesari(message):
    chat_id=message.from_user.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
   
    country_time_zone = pytz.timezone('Asia/Kolkata')
    country_time = datetime.now(country_time_zone)
    today=country_time.strftime('%Y-%m-%d')
    Dayname=country_time.strftime('%A')
    if Dayname!='Sunday':
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
                driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
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
    else:
        bot.reply_to(message,user+'  Sorry , Sunday Not available')
            
@bot.message_handler(commands=['Thinakural'])
def thinakural(message):
    chat_id=message.chat.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)

    path="chromedriver.exe"
    options=webdriver.ChromeOptions()
    options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-sh-usage")
    driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    driver.implicitly_wait(3)
###############################################################hhhhhhhhh######################
    url='http://www.epaper.thinakkural.lk/yarl-thinakkural/'
    pag=driver.get(url)
    driver.implicitly_wait(5)
    pagg=driver.page_source
    driver.implicitly_wait(5)
    soup=BeautifulSoup(pagg,'html')
    glink=soup.find('div',id='inner_page_tile')
    ff=glink.find_all_next('a')
    for a,i in enumerate(ff,start=0):
        try:
            if a<10:
                lnk=str('http://www.epaper.thinakkural.lk'+i['href'][2:])
                #####
                imga=requests.get(lnk)
                driver.implicitly_wait(5)
                imgg=imga.content

                bot.send_photo(chat_id, imgg, protect_content=True ,disable_notification=True)
                driver.implicitly_wait(3)
        except Exception:
            bot.reply_to(message,user + ' Sorry , I can''t Send now, try again later')
    #         bot.send_photo(chat_id, paperpg, protect_content=True ,disable_notification=True)
            #####
            


 ### Current Cut Schdl sending Function
@bot.message_handler(commands=['start'])
def greet(message):
    userID=message.from_user.id
    try:
        userFIRSTNAME=message.from_user.first_name
    except:
        userFIRSTNAME='nan'
    try:
        userLASTNAME=message.from_user.last_name
    except:
        userLASTNAME='nan'
    userUSERNAME=message.from_user.username
    chat_id=message.chat.id
   
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.reply_to(message, f"Hey!  \n Welcome 😍 \n Please type your zone , (ex :- A  or W)  \n Do you want to read today News paper Type /Paper ")
    
    #bot.send_message(mychat_id, 'User name -'+str(userUSERNAME)+ '\nFirst Name -'+userFIRSTNAME'\n Last Name -'+userLASTNAME'\n User Id -'+str(userID))
    bot.send_message(mychat_id, 'User Name-'+str(userUSERNAME)+'\n First Name -'+userFIRSTNAME)
    bot.send_message(mychat_id, f'User Name- {userUSERNAME}\n First Name -{userFIRSTNAME}\n Last Name -{userLASTNAME}\n User Id -{userID}')
    
    
@bot.message_handler(regexp='Hello'or'hello')
def scrap(message):
    chat_id=message.from_user.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,'Hi'+' '+user)

    
@bot.message_handler(regexp='Hi'or'hi')
def scrap(message):
    chat_id=message.from_user.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,'Hi'+' '+user)
    
@bot.message_handler(regexp='I love you'or'i love you')
def scrap(message):
    chat_id=message.from_user.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    
    bot.reply_to(message,'Me too 😍'+' '+user)

    
@bot.message_handler(func=lambda message:False, content_types=['audio', 'photo', 'voice', 'video', 'document','location', 'contact', 'sticker'])
def scrap(message):
    chat_id=message.from_user.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User Id - '+str(chat_id)+'\n name - '+user)
    
    bot.reply_to(message,user+"\nI don't understand, try with /start   ")
    
@bot.message_handler()
def scrap(message):
    chat_id=message.from_user.id
    user=message.from_user.first_name
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id, 'User -'+str(chat_id)+'\n name -'+user)
    if message.text.isdigit() :
        bot.reply_to(message,'type Your Zone (like A or B)')
    elif len(message.text)==1:
        try:
            lttr=message.text.upper()
            zz=str(lttr)
            scraper(zz)
            for i in A:
                bot.reply_to(message,i)
        except Exception:
            bot.reply_to(message,'Please type Your Zone (like A or B)')
    else:
        bot.reply_to(message,'Please type Your Zone (like A or B)')
        
########### telegram bot'''#########################################
def scraper(x):
    ######################################################################################
    options=webdriver.ChromeOptions()
    options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-sh-usage")
    driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
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
            A=['Please Type Correct Zone']
        else:
            table=pd.DataFrame(dic)
            AA=table[table['Zone']==x]
            code_html='*👇👇👇        👇👇👇*' 
            global A
            A=[]
            C=[]
            if AA.empty == False:
                for i in range(len(AA)):
                    B=code_html=code_html + '\n\n Zone:' + str((AA['Zone'].iloc[i])) +' - '+' Time: ' + str((AA['Time'].iloc[i]))
                    
                    C.append(B)
                A=C
                

bot.polling()
