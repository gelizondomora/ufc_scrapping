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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import requests
import lxml
import os
import sys

def peleador_scrapper(url):

    # Look for latest version of Chrome Driver
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_experimental_option("detach", False)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install(), options=chrome_options)


    #Get URL
    driver.get(url)
    driver.maximize_window()

    #Creating lists
    height = []
    weight = []
    reach = []
    stance = []
    dob = []
    slpm = []
    str_acc = []
    sapm= []
    str_def = []
    td_avg = []
    td_acc = []
    td_def = []
    sub_avg =[]
    headers = []



    # # Getting Header names
    # headers_row = driver.find_elements(by='xpath', value='//div/div/div/ul/li/i')
    # for header in headers_row:
    #     head_value = header.text.replace('.:','').replace(':','')
    #     headers.append(head_value)

    #Getting height Column
    height_col=driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    if len(height_col) > 0:
        height_result = height_col[0].text.split(" ", 1)[1]
        height.append(height_result)
    else:
        height_result = 0
        height.append(height_result)
    

    # #Getting WEIGHT Column
    weight_col=driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    if len(weight_col) > 0:
        weight_result = weight_col[1].text.split(" ", 1)[1]
        weight.append(weight_result)
    else:
        weight_result = 0
        weight.append(weight_result)

    # #Getting REACH Column
    reach_col=driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    reach_result = reach_col[2].text.split(" ", 1)[1]
    reach.append(reach_result)


    # #Getting STANCE Column
    stance_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    stance_result = stance_col[3].text.replace('STANCE:', '')
    stance.append(stance_result)

    # #Getting DOB Column
    dob_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    dob_result = dob_col[4].text.split(": ", 1)[1]
    dob.append(dob_result)


    # #Getting SLpM Column
    slpm_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    slpm_result = slpm_col[5].text.split(": ", 1)[1]
    slpm.append(slpm_result)

    # #Getting Str. Acc Column
    str_acc_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    str_acc_result = str_acc_col[6].text.split(": ", 1)[1]
    str_acc.append(str_acc_result)

    # #Getting SApM Column
    sapm_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    sapm_result = sapm_col[7].text.split(": ", 1)[1]
    sapm.append(sapm_result)

    # #Getting Str. Def Column
    str_def_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    str_def_result = str_def_col[8].text.split(": ", 1)[1]
    str_def.append(str_def_result)

    # #Getting TD Avg Column
    td_avg_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    td_avg_result = td_avg_col[10].text.split(": ", 1)[1]
    td_avg.append(td_avg_result)

    # #Getting TD Acc Column
    td_acc_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    td_acc_result = td_acc_col[11].text.split(": ", 1)[1]
    td_acc.append(td_acc_result)

    # #Getting TD Def Column
    td_def_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    td_def_result = td_def_col[12].text.split(": ", 1)[1]
    td_def.append(td_def_result)

    # #Getting Sub. Avg Column
    sub_avg_col =driver.find_elements(by='xpath', value='//div/div/div/ul/li')
    sub_avg_result = sub_avg_col[13].text.split(": ", 1)[1]
    sub_avg.append(sub_avg_result)

    driver.quit()

    #ADDING DATA TO COLUMNS
    df =pd.DataFrame()
    df['HEIGHT'] = height
    df['WEIGHT'] = weight
    df['REACH'] = reach
    df['STANCE'] = stance
    df['DOB'] = dob
    df['SLpM'] = slpm
    df['Str. Acc'] = str_acc
    df['SApM'] = sapm
    df['Str. Def'] = str_def
    df['TD Avg'] = td_avg
    df['TD Acc'] = td_acc
    df['TD Def'] = td_def
    df['Sub. Avg'] =  sub_avg

    return(df)
