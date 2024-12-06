from lib2to3.pgen2 import driver
from posixpath import dirname
import pandas as pd
import numpy as np
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.safari.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import lxml
import os
import sys

def lista_eventos_scrapper(url):
    # Look for latest version of Chrome Driver
    # try:
    # service = Service()
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_experimental_option("detach", False)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install(), options=chrome_options)
    # service = Service()
    # safari_options = Options()
    # # driver = webdriver.Chrome(service=service,options=chrome_options)
    # driver = webdriver.Safari(options=safari_options)
    # except WebDriverException:
    #     print("Exception Encontrada")

    #Get URL
    driver.get(url)
    driver.maximize_window()

    #Creating lists
    event_name =[]
    event_index = []
    event_link = []
    headers = ['INDEX','EVENT', 'EVENT_LINK']


    #Getting Event Information Column
    event_list =driver.find_elements(by='xpath', value='//tbody/tr/td/i/a')
    for idx, row in enumerate(event_list):
        event_name_output = row.text
        event_index_output = idx
        event_link_output = row.get_attribute('href')
        event_name.append(event_name_output)
        event_index.append(event_index_output)
        event_link.append(event_link_output)

    driver.quit()
    
    #ADDING DATA TO COLUMNS
    df =pd.DataFrame(columns=headers)
    df['INDEX'] = event_index
    df['EVENT'] = event_name
    df['EVENT_LINK'] = event_link

    return(df)

