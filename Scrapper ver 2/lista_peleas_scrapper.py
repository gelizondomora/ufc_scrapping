from lib2to3.pgen2 import driver
from posixpath import dirname
import pandas as pd
import numpy as np
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import lxml
import os
import sys

def lista_peleas_scrapper(url): 
    # Look for latest version of Chrome Driver
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_experimental_option("detach", False)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install(), options=chrome_options)
    # except WebDriverException:
    #     print("Exception Encontrada")


    #Get URL
    driver.get(url)
    driver.maximize_window()

     #Creating lists
    fighter_1 =[]
    fighter_2 = []
    fighter_1_link = []
    fighter_2_link = []
    fight_index = []
    headers = ['INDEX','FIGHTER_1','FIGHTER_2', 'FIGHTER_1_LINK', 'FIGHTER_2_LINK']

    #Getting FIGHTER_1 INFO Column
    fighter_1_list =driver.find_elements(by='xpath', value='//tbody/tr/td[2]/p[1]/a')
    for idx, row in enumerate(fighter_1_list):
        fighter_1_name = row.text
        fight_index_text = idx
        fighter_1_link_text = row.get_attribute('href')
        fighter_1.append(fighter_1_name)
        fight_index.append(fight_index_text)
        fighter_1_link.append(fighter_1_link_text)

        #Getting FIGHTER_2 INFO Column
    fighter_2_list =driver.find_elements(by='xpath', value='//tbody/tr/td[2]/p[2]/a')
    for idx, row in enumerate(fighter_2_list):
        fighter_2_name = row.text
        fighter_2_link_text = row.get_attribute('href')
        fighter_2.append(fighter_2_name)
        fighter_2_link.append(fighter_2_link_text)
      
    driver.quit()
    
    #ADDING DATA TO COLUMNS
    df =pd.DataFrame(columns=headers)
    df['INDEX'] = fight_index
    df['FIGHTER_1'] = fighter_1
    df['FIGHTER_2'] = fighter_2
    df['FIGHTER_1_LINK'] = fighter_1_link
    df['FIGHTER_2_LINK'] = fighter_2_link

    return(df)
