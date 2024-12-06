from lib2to3.pgen2 import driver
from posixpath import dirname
from unittest import result
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
import time
from peleador_scrapper import peleador_scrapper



def historial_peleas_scrapper(url, fight_index):

    # Look for latest version of Chrome Driver
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_experimental_option("detach", False)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install(), options=chrome_options)
    #     print("Exception Encontrada")


    #Get URL
    driver.get(url)

    #Creating lists
    opponent_info_height = []
    opponent_info_weight = []
    opponent_info_reach = []
    opponent_info_stance = []
    opponent_info_dob = []
    opponent_info_slpm = []
    opponent_info_str_acc = []
    opponent_info_sapm = []
    opponent_info_str_def = []
    opponent_info_td_avg = []
    opponent_info_td_acc = []
    opponent_info_td_def = []
    opponent_info_sub_avg = []

    headers_figther = []
    fighter_info_height = []
    fighter_info_weight = []
    fighter_info_reach = []
    fighter_info_stance = []
    fighter_info_dob = []
    fighter_info_slpm = []
    fighter_info_str_acc = []
    fighter_info_sapm = []
    fighter_info_str_def = []
    fighter_info_td_avg = []
    fighter_info_td_acc = []
    fighter_info_td_def = []
    fighter_info_sub_avg = []

    def is_not_next_match(idx):
        if win_lose[idx] == 'NEXT':
            return True
        else:
            return False

    def loop_get_values(column):
        value = [row.text for idx, row in enumerate(fighter_col) if is_not_next_match(idx)]
        return value

 # Getting Header names
    headers_row = driver.find_elements(by='xpath', value='//th')

    #Getting W/L Column
    wl_col=driver.find_elements(by='xpath', value='//tr/td[1]/p/a/i/i')

    #Getting FIGHTER Column
    fighter_col=driver.find_elements(by='xpath', value='//tr/td[2]/p[1]')

    #Getting OPPONENT Column
    opponent_col=driver.find_elements(by='xpath', value='//tr/td[2]/p[2]')

    #Getting OPPONENT LINK Column
    opponent_link_col=driver.find_elements(by='xpath', value='//tr/td[2]/p[2]/a')

    #Getting KD Column
    kd_col=driver.find_elements(by='xpath', value='//tr/td[3]/p[1]')

    #Getting OPPONENT_KD Column
    opp_kd_col=driver.find_elements(by='xpath', value='//tr/td[3]/p[2]')

    #Getting STRIKES Column
    strikes_col=driver.find_elements(by='xpath', value='//tr/td[4]/p[1]')

    #Getting OPPONENT STRIKES Column
    opp_strikes_col=driver.find_elements(by='xpath', value='//tr/td[4]/p[2]')

    #Getting TD Column
    td_col=driver.find_elements(by='xpath', value='//tr/td[5]/p[1]')

    #Getting OPPONENT TD Column
    opp_td_col=driver.find_elements(by='xpath', value='//tr/td[5]/p[2]')

    #Getting SUB Column
    sub_col=driver.find_elements(by='xpath', value='//tr/td[6]/p[1]')

    #Getting OPPONENT SUB Column
    opp_sub_col=driver.find_elements(by='xpath', value='//tr/td[6]/p[2]')

    #Getting EVENT Column
    event_col =driver.find_elements(by='xpath', value='//tr/td[7]/p[1]')

    #Getting FIGHT_DATE Column
    fight_date_col =driver.find_elements(by='xpath', value='//tr/td[7]/p[2]')

    #Getting METHOD Column
    method_col =driver.find_elements(by='xpath', value='//tr/td[8]/p[1]')

    #Getting ROUND Column
    round_col =driver.find_elements(by='xpath', value='//tr/td[9]/p[1]')

    #Getting TIME Column
    time_col =driver.find_elements(by='xpath', value='//tr/td[10]/p[1]')


# Creating list of elements

    elements_list = [
        wl_col, 
        fighter_col, 
        opponent_col, 
        kd_col,
        opp_kd_col,
        strikes_col, 
        opp_strikes_col,
        td_col,
        opp_td_col,
        sub_col,
        opp_sub_col,
        event_col,
        fight_date_col,
        method_col,
        round_col,
        time_col
    ]



    # Getting Header names
    headers = [header.text.replace('\n    ','').replace('\n  ', '') for header in headers_row]

    #Getting W/L Column
    win_lose = [row.text for row in wl_col]

    #Getting FIGHTER Column
    # fighter = [row.text for idx, row in enumerate(fighter_col) if is_not_next_match(idx)]
    fighter = [row.text for row in fighter_col]
    #Getting FIGHTER INDEX Column
    # index_data = [fight_index for idx, row in enumerate(fighter_col) if is_not_next_match(idx)]
    index_data = [fight_index for idx, row in enumerate(fighter_col)]
    #Getting OPPONENT Column
    # opponent = [row.text for idx, row in enumerate(opponent_col) if is_not_next_match(idx)]
    opponent = [row.text for idx, row in enumerate(opponent_col)]

    #Getting OPPONENT LINK Column
    # opponent_link = [row.get_attribute('href') for idx, row in enumerate(opponent_link_col) if is_not_next_match(idx)]
    opponent_link = [row.get_attribute('href') for idx, row in enumerate(opponent_link_col)]

    #Getting KD Column
    kd = [row.text for idx, row in enumerate(kd_col) ]

    #Getting OPPONENT_KD Column
    opponent_kd = [row.text for idx, row in enumerate(opp_kd_col)]


    #Getting STRIKES Column
    # strikes = [row.text for idx, row in enumerate(strikes_col) if is_not_next_match(idx)]
    strikes = [row.text for idx, row in enumerate(strikes_col)]

    #Getting OPPONENT STRIKES Column
    opponent_str = [row.text for idx, row in enumerate(opp_strikes_col)]

    #Getting TD Column
    td = [row.text for idx, row in enumerate(td_col)]


    #Getting OPPONENT TD Column
    opponent_td = [row.text for idx, row in enumerate(opp_td_col)]


    #Getting SUB Column
    # sub = [row.text for idx, row in enumerate(sub_col) if is_not_next_match(idx)]
    sub = [row.text for idx, row in enumerate(sub_col)]


    #Getting OPPONENT SUB Column
    # opponent_sub = [row.text for idx, row in enumerate(opp_sub_col) if is_not_next_match(idx)]
    opponent_sub = [row.text for idx, row in enumerate(opp_sub_col)]


    #Getting EVENT Column
    event = [row.text for row in event_col]

    #Getting FIGHT_DATE Column
    fight_date = [row.text for row in fight_date_col]

    #Getting METHOD Column
    method = [row.text for idx, row in enumerate(method_col)]

    #Getting ROUND Column
    round = [row.text for idx, row in enumerate(round_col)]

    #Getting TIME Column
    time_value = [row.text for idx, row in enumerate(time_col)]


    driver.quit()
    
    #Getting Opponents Information

    for link in opponent_link:
        opponent_info = peleador_scrapper(link)
        # for i, info in opponent_info.iterrows():
        opponent_info_height.append(opponent_info.iloc[0, 0])
        opponent_info_weight.append(opponent_info.iloc[0, 1])
        opponent_info_reach.append(opponent_info.iloc[0, 2])
        opponent_info_stance.append(opponent_info.iloc[0, 3])
        opponent_info_dob.append(opponent_info.iloc[0, 4])
        opponent_info_slpm.append(opponent_info.iloc[0, 5])
        opponent_info_str_acc.append(opponent_info.iloc[0, 6])
        opponent_info_sapm.append(opponent_info.iloc[0,7])
        opponent_info_str_def.append(opponent_info.iloc[0,8])
        opponent_info_td_avg.append(opponent_info.iloc[0,9])
        opponent_info_td_acc.append(opponent_info.iloc[0 ,10])
        opponent_info_td_def.append(opponent_info.iloc[0, 11])
        opponent_info_sub_avg.append(opponent_info.iloc[0, 12])

        #Getting fighter Information
    
    fighter_info = peleador_scrapper(url)
    for i, info in fighter_info.iterrows():

        fighter_info_height.append(info[0])
        fighter_info_weight.append(info[1])
        fighter_info_reach.append(info[2])
        fighter_info_stance.append(info[3])
        fighter_info_dob.append(info[4])
        fighter_info_slpm.append(info[5])
        fighter_info_str_acc.append(info[6])
        fighter_info_sapm.append(info[7])
        fighter_info_str_def.append(info[8])
        fighter_info_td_avg.append(info[9])
        fighter_info_td_acc.append(info[10])
        fighter_info_td_def.append(info[11])
        fighter_info_sub_avg.append(info[12])



    #APPENDING OPPONENT COLUMNS

    headers.append('OPPONENT')
    headers.append('OPPONENT_KD')
    headers.append('OPPONENT_SUB')
    headers.append('OPPONENT_STR')
    headers.append('OPPONENT_TD')
    headers.append('OPPONENT_LINK')
    headers.append('FIGHT_DATE')
    headers.append('FIGHT_INDEX')
    headers.append('OPPONENT_INFO_HEIGHT')
    headers.append('OPPONENT_INFO_WEIGHT')
    headers.append('OPPONENT_INFO_REACH')
    headers.append('OPPONENT_INFO_STANCE')
    headers.append('OPPONENT_INFO_DOB')
    headers.append('OPPONENT_INFO_SLPM')
    headers.append('OPPONENT_INFO_STR_ACC')
    headers.append('OPPONENT_INFO_SAPM')
    headers.append('OPPONENT_INFO_STR_DEF')
    headers.append('OPPONENT_INFO_TD_AVG')
    headers.append('OPPONENT_INFO_TD_ACC')
    headers.append('OPPONENT_INFO_TD_DEF')
    headers.append('OPPONENT_INFO_SUB_AVG')

    headers_figther.append('FIGHTER_INFO_HEIGHT')
    headers_figther.append('FIGHTER_INFO_WEIGHT')
    headers_figther.append('FIGHTER_INFO_REACH')
    headers_figther.append('FIGHTER_INFO_STANCE')
    headers_figther.append('FIGHTER_INFO_DOB')
    headers_figther.append('FIGHTER_INFO_SLPM')
    headers_figther.append('FIGHTER_INFO_STR_ACC')
    headers_figther.append('FIGHTER_INFO_SAPM')
    headers_figther.append('FIGHTER_INFO_STR_DEF')
    headers_figther.append('FIGHTER_INFO_TD_AVG')
    headers_figther.append('FIGHTER_INFO_TD_ACC')
    headers_figther.append('FIGHTER_INFO_TD_DEF')
    headers_figther.append('FIGHTER_INFO_SUB_AVG')

    #REMOVE FIRST ELEMENT OF win_lose
    if win_lose[0] == 'NEXT':
        win_lose[0] = "NC"
        kd.insert(0, "0")
        opponent_kd.insert(0, "0")
        strikes[0]= "0"
        opponent_str.insert(0, "0")
        td.insert(0, "0")
        opponent_td.insert(0, "0")
        sub[0] = "0"
        opponent_sub[0]= "0"
        method.insert(0, "")
        round.insert(0, "0")
        time_value.insert(0, "0")
        event.insert(0,"Current Event")
        fight_date.insert(0,"Next Fight date")

    if len(index_data)> len(win_lose):
        index_data.pop(1)
        kd.pop(1)
        method.pop(1)
        fighter.pop(1)
        strikes.pop(1)
        opponent_str.pop(1)
        opponent.pop(1)
        opponent_kd.pop(1)
        td.pop(1)
        opponent_td.pop(1)
        sub.pop(1)
        opponent_sub.pop(1)
        opponent_link.pop(1)
        event.pop(1)
        fight_date.pop(1)
        method.pop(1)
        # round.pop(1)
        time_value.pop(1)
        opponent_info_height.pop(1)
        opponent_info_weight.pop(1)
        opponent_info_reach.pop(1)
        opponent_info_stance.pop(1)
        opponent_info_dob.pop(1)
        opponent_info_slpm.pop(1)
        opponent_info_str_acc.pop(1)
        opponent_info_sapm.pop(1)
        opponent_info_str_def.pop(1)
        opponent_info_td_avg.pop(1)
        opponent_info_td_acc.pop(1)
        opponent_info_td_def.pop(1)
        opponent_info_sub_avg.pop(1)


    #ADDING DATA TO COLUMNS
    df =pd.DataFrame(columns=headers)
    df["FIGHT_INDEX"] = index_data
    df['W/L'] = win_lose
    df['FIGHTER'] = fighter
    df['KD'] = kd
    df['STR'] = strikes
    df['OPPONENT_STR'] = opponent_str
    df['OPPONENT'] = opponent
    df['OPPONENT_KD'] = opponent_kd
    df['TD'] = td
    df['OPPONENT_TD'] = opponent_td
    df['SUB'] = sub
    df['OPPONENT_SUB'] = opponent_sub
    df['OPPONENT_LINK'] = opponent_link
    df['EVENT'] =  event
    df['FIGHT_DATE'] = fight_date
    # df['METHOD'] =  method
    # df['ROUND'] =  round
    df['TIME'] =  time_value

    df['OPPONENT_INFO_HEIGHT'] = opponent_info_height
    df['OPPONENT_INFO_WEIGHT'] = opponent_info_weight
    df['OPPONENT_INFO_REACH'] = opponent_info_reach
    df['OPPONENT_INFO_STANCE'] = opponent_info_stance
    df['OPPONENT_INFO_DOB'] = opponent_info_dob
    df['OPPONENT_INFO_SLPM'] = opponent_info_slpm
    df['OPPONENT_INFO_STR_ACC'] = opponent_info_str_acc
    df['OPPONENT_INFO_SAPM'] = opponent_info_sapm
    df['OPPONENT_INFO_STR_DEF'] = opponent_info_str_def
    df['OPPONENT_INFO_TD_AVG'] = opponent_info_td_avg
    df['OPPONENT_INFO_TD_ACC'] = opponent_info_td_acc
    df['OPPONENT_INFO_TD_DEF'] = opponent_info_td_def
    df['OPPONENT_INFO_SUB_AVG'] = opponent_info_sub_avg

    df_figther =pd.DataFrame(columns=headers_figther)
    df_figther["FIGHT_INDEX"] = fight_index
    df_figther['FIGHTER'] =  fighter[0]
    df_figther['FIGHTER_INFO_HEIGHT'] = fighter_info_height
    df_figther['FIGHTER_INFO_WEIGHT'] = fighter_info_weight
    df_figther['FIGHTER_INFO_REACH'] = fighter_info_reach
    df_figther['FIGHTER_INFO_STANCE'] = fighter_info_stance
    df_figther['FIGHTER_INFO_DOB'] = fighter_info_dob
    df_figther['FIGHTER_INFO_SLPM'] = fighter_info_slpm
    df_figther['FIGHTER_INFO_STR_ACC'] = fighter_info_str_acc
    df_figther['FIGHTER_INFO_SAPM'] = fighter_info_sapm
    df_figther['FIGHTER_INFO_STR_DEF'] = fighter_info_str_def
    df_figther['FIGHTER_INFO_TD_AVG'] = fighter_info_td_avg
    df_figther['FIGHTER_INFO_TD_ACC'] = fighter_info_td_acc
    df_figther['FIGHTER_INFO_TD_DEF'] = fighter_info_td_def
    df_figther['FIGHTER_INFO_SUB_AVG'] = fighter_info_sub_avg


    #FORMATING DATAFRAME

    df['FIGHT_DATE'] =pd.to_datetime(df['FIGHT_DATE'], errors='coerce')
    df['KD'] = pd.to_numeric(df['KD'], errors= 'coerce')
    df['STR'] = pd.to_numeric(df['STR'], errors= 'coerce')
    df['OPPONENT_STR'] = pd.to_numeric(df['OPPONENT_STR'], errors= 'coerce')
    df['OPPONENT_SUB'] = pd.to_numeric(df['OPPONENT_SUB'], errors= 'coerce')
    df['OPPONENT_KD'] = pd.to_numeric(df['OPPONENT_KD'], errors= 'coerce')
    df['TD'] = pd.to_numeric(df['TD'], errors= 'coerce')
    df['OPPONENT_TD'] = pd.to_numeric(df['OPPONENT_TD'], errors= 'coerce')
    df['SUB'] = pd.to_numeric(df['SUB'], errors= 'coerce')
    df['TIME'] =pd.to_datetime(df['TIME'], errors='coerce')
    df['ROUND'] = pd.to_numeric(df['ROUND'], errors= 'coerce')


    df['OPPONENT_INFO_SLPM'] = pd.to_numeric(df['OPPONENT_INFO_SLPM'])
    df['OPPONENT_INFO_STR_ACC'] = df['OPPONENT_INFO_STR_ACC'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['OPPONENT_INFO_SAPM'] = pd.to_numeric(df['OPPONENT_INFO_SAPM'])
    df['OPPONENT_INFO_STR_DEF'] = df['OPPONENT_INFO_STR_DEF'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['OPPONENT_INFO_TD_AVG'] = pd.to_numeric(df['OPPONENT_INFO_TD_AVG'])
    df['OPPONENT_INFO_TD_ACC'] = df['OPPONENT_INFO_TD_ACC'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['OPPONENT_INFO_TD_DEF'] = df['OPPONENT_INFO_TD_DEF'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['OPPONENT_INFO_SUB_AVG'] =pd.to_numeric(df['OPPONENT_INFO_SUB_AVG'])
    df['OPPONENT_INFO_DOB'] = pd.to_datetime(df['OPPONENT_INFO_DOB'], errors='coerce')

    df['FIGHTER_INFO_SLPM'] = pd.to_numeric(df_figther['FIGHTER_INFO_SLPM'])
    df['FIGHTER_INFO_STR_ACC'] = df_figther['FIGHTER_INFO_STR_ACC'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['FIGHTER_INFO_SAPM'] = pd.to_numeric(df_figther['FIGHTER_INFO_SAPM'])
    df['FIGHTER_INFO_STR_DEF'] = df_figther['FIGHTER_INFO_STR_DEF'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['FIGHTER_INFO_TD_AVG'] = pd.to_numeric(df_figther['FIGHTER_INFO_TD_AVG'])
    df['FIGHTER_INFO_TD_ACC'] = df_figther['FIGHTER_INFO_TD_ACC'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['FIGHTER_INFO_TD_DEF'] = df_figther['FIGHTER_INFO_TD_DEF'].str.replace(r'%', r'.0').astype('float') / 100.0
    df['FIGHTER_INFO_SUB_AVG'] = pd.to_numeric(df_figther['FIGHTER_INFO_SUB_AVG'])
    df['FIGHTER_INFO_DOB'] = pd.to_datetime(df_figther['FIGHTER_INFO_DOB'], errors='coerce')

    df_figther['FIGHTER_INFO_SLPM'] = pd.to_numeric(df_figther['FIGHTER_INFO_SLPM'])
    df_figther['FIGHTER_INFO_STR_ACC'] = df_figther['FIGHTER_INFO_STR_ACC'].str.replace(r'%', r'.0').astype('float') / 100.0
    df_figther['FIGHTER_INFO_SAPM'] = pd.to_numeric(df_figther['FIGHTER_INFO_SAPM'])
    df_figther['FIGHTER_INFO_STR_DEF'] = df_figther['FIGHTER_INFO_STR_DEF'].str.replace(r'%', r'.0').astype('float') / 100.0
    df_figther['FIGHTER_INFO_TD_AVG'] = pd.to_numeric(df_figther['FIGHTER_INFO_TD_AVG'])
    df_figther['FIGHTER_INFO_TD_ACC'] = df_figther['FIGHTER_INFO_TD_ACC'].str.replace(r'%', r'.0').astype('float') / 100.0
    df_figther['FIGHTER_INFO_TD_DEF'] = df_figther['FIGHTER_INFO_TD_DEF'].str.replace(r'%', r'.0').astype('float') / 100.0
    df_figther['FIGHTER_INFO_SUB_AVG'] = pd.to_numeric(df_figther['FIGHTER_INFO_SUB_AVG'])
    df_figther['FIGHTER_INFO_DOB'] = pd.to_datetime(df_figther['FIGHTER_INFO_DOB'], errors='coerce')


    return(df, df_figther)
    
# #Url: Charles Oliveira: http://www.ufcstats.com/fighter-details/07225ba28ae309b6

# link= r'http://www.ufcstats.com/fighter-details/07225ba28ae309b6'
# index = 0
# start_time = time.time()
# fighter_1_historical, fighter_1_stats = historial_peleas_scrapper(link, index)
# print(fighter_1_historical)
# print(fighter_1_stats)
# print("--- %s seconds ---" % (time.time() - start_time))