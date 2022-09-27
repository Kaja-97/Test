#!/usr/bin/env python
# coding: utf-8

# In[2]:
from telebot import types
from selenium.webdriver.common.keys import Keys
import platform
import threading
#
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
                soup=BeautifulSoup(driver.page_source,'html.parser')
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
    urlrk='http://www.epaper.thinakkural.lk/yarl-thinakkural/'
    pag=driver.get(urlrk)
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
#     bot.send_message(mychat_id, 'User Name-'+str(userUSERNAME)+'\n First Name -'+userFIRSTNAME)
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
    bot.send_message(mychat_id, f'User Name- {userUSERNAME}\n First Name -{userFIRSTNAME}\n Last Name -{userLASTNAME}\n User Id -{userID}')
    
    mychat_id=os.getenv('MY_CHAT_ID')
    
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
    
    print('01')
    ######################################################################################
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
    print('1')
    # driver =webdriver.Chrome(executable_path=r"C:\Users\kajan\Desktop\Python\Web Scraping\chromedriver.exe",chrome_options=options)
    url5='https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule'
    pag=driver.get(url=url5)
    print('2')
    driver.implicitly_wait(3)
    pagg=driver.page_source
    soup=BeautifulSoup(pagg,'html.parser')
    soup1=soup.find('div',class_="fc-scroller fc-time-grid-container")
    #soup1=BeautifulSoup(ss,'html.parser')
    a=soup1.find_all('a')
    print(a)
    global A
    A=[]
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
        bot.reply_to(message,Zone)
        print(Zone)
        dic={'Zone':Zone,'Time':Time}

        if x not in Zone:
            A=['Please Type Correct Zone']
        else:
            table=pd.DataFrame(dic)
            AA=table[table['Zone']==x]
            code_html='*👇👇👇        👇👇👇*' 
            if AA.empty == False:
                for i in range(len(AA)):
                    B=code_html=code_html + '\n\n Zone:' + str((AA['Zone'].iloc[i])) +' - '+' Time: ' + str((AA['Time'].iloc[i]))
                A=[B]
                bot.reply_to(message,'fun runed')
                

def Uni_crap():
    country_time_zone = pytz.timezone('Asia/Kolkata')
    country_time = datetime.now(country_time_zone)
    todayD=country_time.strftime('%Y-%m-%d')
    todayT=country_time.strftime('%H-%M-%S')
    url1='https://learnousl.ou.ac.lk/login/index.php'
    username=os.getenv('USER_NAME')
    password=os.getenv('PASSWORDS')
    subject_url=[]
    subject=[]
    anounce_url=[]
    Course_Coude=[]
    # def login():
    
#     options=webdriver.ChromeOptions()
#     options.headless = True
#     driver =webdriver.Chrome(executable_path=r"C:\Users\kajan\Desktop\Python\Web Scraping\chromedriver",options=options)
    options=webdriver.ChromeOptions()
    options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-sh-usage")
    driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    driver.get(url=url1)
    driver.implicitly_wait(3)
    ### login() .
    driver.find_element('id','username').clear()
    driver.find_element('id','username').send_keys(username)
    driver.find_element('id','password').clear()
    driver.find_element('id','password').send_keys(password)
    driver.find_element('id','loginbtn').click()
    driver.get('https://learnousl.ou.ac.lk/my/')
    driver.implicitly_wait(5)
    global page
    page=driver.page_source
    #return page
    soup=BeautifulSoup(page,'html')
    course=soup.find_all('li',class_='type_course depth_3 contains_branch')
    course=course[1:]
    # get all subject's Url in subject_url list
    for sub in course:
        s=sub.find('p').a['href']
        subject_url.append(s)

    for an in subject_url:
        urd=an
        global page1
        driver.get(url=urd)
        driver.implicitly_wait(5)
        page1=driver.page_source
        soup1=BeautifulSoup(page1,'html.parser')
        sub_name=soup1.find('header').h1.text
        CCode=sub_name.split(' ')[0]
        Course_Coude.append(CCode)
        Name=sub_name[8:]
        subject.append(Name)
        try:
            an=soup1.find('li',{'id':'section-1'}).find('li').find_next('li').find('a',class_='aalink')['href']  #.find('a',class_='aalink')['href']#.find('div',class_='mod-indent-outer w-100').find('a',class_='aalink')['href']  #activityinstance
            #print(an)
            anounce_url.append(an)
        except Exception :
            print('link not found ,need to change code')

    dict={'Course Code':Course_Coude,'Subject Name':subject,'subject':subject_url,'Announcement':anounce_url}  

    
    for i,an in enumerate(anounce_url, start=0):
        driver.get(an)
        ll=driver.page_source
        name_sub=Course_Coude[i]
        try:
            df=pd.read_html(ll)[1].head(2)
        except:
            df=pd.read_html(ll)[0].head(2)
        F=str(list(df.loc[0]))
        F1=list(df.loc[0])
        mess=F1[1]
#         global UNI
        SS=str(str(name_sub)+' '+F)
        #date check
        dsa=df['Started by'][0].split()[-3:]
        a=dsa[0]+dsa[1]+dsa[2]
        post_date=pd.to_datetime(a).strftime('%Y-%m-%d')
        mychat_id=os.getenv('MY_CHAT_ID')
        if post_date==todayD:
            bot.send_message(mychat_id,name_sub+'\n '+mess.replace('Locked','.'))
        bot.send_message(mychat_id,'Uni_scrap fun end')
       
def allfun():
    while True:
        Uni_crap()
        mychat_id=os.getenv('MY_CHAT_ID')
        bot.send_message(mychat_id,'Uni Function thread ended ')
        #print('thread sleep')
        time.sleep(60*30)

##############################################################################

    
@bot.message_handler(commands=['UUni'])
def scrap(message):
    Uni_crap()
    mychat_id=os.getenv('MY_CHAT_ID')
    bot.send_message(mychat_id,'start fun sep ')
    
thred=threading.Thread(target=allfun)
thred.start()

                
                
                
bot.polling()
