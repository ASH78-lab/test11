




asd2=[
'AC Milan',
'AFC Bournemouth',
'Arsenal',
'AS Roma',
'Aston Villa',
'Atalanta',
'Atletico Madrid',
'Bayer Leverkusen',
'Bayern Munchen',
'Borussia Dortmund',
'Brighton Hove Albion',
'Celta Vigo',
'Como',
'Crystal Palace',
'FC Barcelona',
'Getafe',
'Inter Milan',
'Juventus',
'Lens',
'Lille',
'Liverpool',
'Lyon',
'Manchester City',
'Manchester United',
'Marseille',
'Monaco',
'Napoli',
'Paris Saint Germain (PSG)',
'RB Leipzig',
'Real Betis',
'Real Madrid',
'Real Sociedad',
'Rennes',
'SC Freiburg',
'Sunderland A.F.C',
'TSG Hoffenheim',
'VfB Stuttgart',
'Villarreal',


]
from datetime import datetime
import time
date_new53 = str(datetime.now())
print(date_new53)
a123=time.time()




import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

driver.set_window_size(1800, 800) 




   
data2=[]
data3=[]



asd=[
'https://football.nowgoal.net/league/103',
'https://football.nowgoal.net/league/113',
'https://football.nowgoal.net/league/2187'
]

for a in asd:
    driver.get(a)
    time.sleep(7)
    for i in range(2,12):
        try:
            c1 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[2]').text
            c2 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[4]/span').text
            c3 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[6]/span').text
            c4 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[5]')

            a99=c4.get_attribute('onclick')
            a2=a99.split('(')
            a3=a2[1].split(',')
            a40 = a3[0].split('"')
            a41 = int(a40[0].strip("'"))
            a5=str(a41)
            c4 = ('https://www.nowgoal.net/match/h2h-'+a5)

            data3.append([c1,c2,c3,c4])
            # print(c1,c2,c3,c4)
        except:
            pass



    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException



    element9 = int(driver.find_element(By.ID, 'schedulePager').find_element(By.CLASS_NAME, 'on').get_attribute('data-page'))+1
    # element2 = driver.find_element(By.CSS_SELECTOR, f'[data-page="{element}"]')


                                                           


    wait = WebDriverWait(driver, 15)  # Увеличил таймаут, если сайт тяжелый

    # xpath_locator = "/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[4]/span[2]/span"

    try:
        # 1. Ждем, пока элемент появится и будет готов к клику
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_locator)))
        
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-page="{element9}"]')))
        try:
            # 2. Пытаемся обычный клик
            element.click()
            print("Успешный клик!")
        except ElementClickInterceptedException:
            print("Обычный клик заблокирован. Пробуем через JS...")
            # 3. Если обычный не сработал — делаем клик через JS
            driver.execute_script("arguments[0].click();", element)
            print("Клик через JS выполнен!")

    except TimeoutException:
        print("Элемент не появился за 15 секунд. Проверь XPath или загрузку страницы.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    time.sleep(7)
    start = start + 10
    end = 10 + start

    for i in range(start,end):
        try:
            c1 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[2]').text
            c2 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[4]/span').text
            c3 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[6]/span').text
            c4 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[5]')
            a99=c4.get_attribute('onclick')
            a2=a99.split('(')
            a3=a2[1].split(',')
            a40 = a3[0].split('"')
            a41 = int(a40[0].strip("'"))
            a5=str(a41)
            c4 = ('https://www.nowgoal.net/match/h2h-'+a5)
            data3.append([c1,c2,c3,c4])
        except:
            pass
#3-----------------------------------------
    element9 = element9 +1
    wait = WebDriverWait(driver, 15)  # Увеличил таймаут, если сайт тяжелый

    # xpath_locator = "/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[4]/span[2]/span"

    try:
        # 1. Ждем, пока элемент появится и будет готов к клику
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_locator)))
        
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-page="{element9}"]')))
        try:
            # 2. Пытаемся обычный клик
            element.click()
            print("Успешный клик!")
        except ElementClickInterceptedException:
            print("Обычный клик заблокирован. Пробуем через JS...")
            # 3. Если обычный не сработал — делаем клик через JS
            driver.execute_script("arguments[0].click();", element)
            print("Клик через JS выполнен!")

    except TimeoutException:
        print("Элемент не появился за 15 секунд. Проверь XPath или загрузку страницы.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    time.sleep(7)

    start = start + 10
    end = 10 + start

    for i in range(start,end):
        try:
            c1 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[2]').text
            c2 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[4]/span').text
            c3 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[6]/span').text
            c4 = driver.find_element(By.XPATH,f'/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[3]/div[{i}]/span[5]')
            a99=c4.get_attribute('onclick')
            a2=a99.split('(')
            a3=a2[1].split(',')
            a40 = a3[0].split('"')
            a41 = int(a40[0].strip("'"))
            a5=str(a41)
            c4 = ('https://www.nowgoal.net/match/h2h-'+a5)
            data3.append([c1,c2,c3,c4])
        except:
            pass

links5 = pd.DataFrame(data3)
import numpy as np
links5[2] = links5[2].replace(['', ' ', 'null', 'None', 'NaN', np.nan], np.nan)
link6=links5.dropna(subset=[2])

link6['have'] = (
    link6[1].isin(asd2) | 
    link6[2].isin(asd2)
).astype(int)

link7 = link6.loc[link6['have'] == 1]





for z in link7.values:


    driver.get(z[3])
    time.sleep(7)
    league_check = driver.find_element(By.CLASS_NAME, "LName").text
    if 'UEFA Europa League' in league_check:
        dop = 9
    else:
        dop = 10
    a1 = driver.find_elements(By.CLASS_NAME, "sclassName")[0].text
    b1 = driver.find_elements(By.CLASS_NAME, "sclassName")[1].text
    if a1 not in asd2:


        for i in range(5,7):
            try:
                a10 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[1]').text
                a2 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[2]').text
                a3 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[3]').text
                a4 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[4]').text
                a5 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[5]').text
                a6 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[7]').text
                a7 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[8]').text
                a8 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[9]').text
                a9 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[1]/table/tbody/tr[{i}]/td[12]').text
                data2.append([a1,a10,a2,a3,a4,a5,a6,a7,a8,a9])
                print(a10,a1,a2,a3,a4,a5,a6,a7,a8,a9)
            except:
                pass
    else:

        pass    


    if b1 not in asd2:


        
        for i in range(5,7):
            try:
                b10 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[1]').text
                b2 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[2]').text
                b3 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[3]').text
                b4 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[4]').text
                b5 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[5]').text
                b6 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[7]').text
                b7 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[8]').text
                b8 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[9]').text
                b9 = driver.find_element(By.XPATH,f'/html/body/div[9]/div[1]/div[2]/div[{dop}]/div[2]/table/tbody/tr[{i}]/td[12]').text
                data2.append([b1,b10,b2,b3,b4,b5,b6,b7,b8,b9])
                print(b10,b1,b2,b3,b4,b5,b6,b7,b8,b9)
            except:
                pass
    else:

        pass    


driver.quit()
links8 = pd.DataFrame(data2)
print(links8)

date_new533 = str(datetime.now())
print(date_new533)
b123=time.time()
delta1=b123-a123
print(delta1)

import os

TOKEN2 = os.getenv('TOKEN2')
TOKEN1="440d864051de61f4b6463f10f8006898192b7420"
TOKEN3="ash789@avid-stone-461407-q5.iam.gserviceaccount.com"
TOKEN4 ="116197129399001621585"
TOKEN5="https://www.googleapis.com/robot/v1/metadata/x509/ash789%40avid-stone-461407-q5.iam.gserviceaccount.com"




credentials={
  "type": "service_account",
  "project_id": "avid-stone-461407-q5",
  "private_key_id": TOKEN1,
  "private_key": TOKEN2,
  "client_email": TOKEN3,
  "client_id": TOKEN4,
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": TOKEN5,
  "universe_domain": "googleapis.com"}
import gspread
import pandas as pd
import requests
gc = gspread.service_account_from_dict(credentials)
wks9 = gc.open("Test789").get_worksheet(6)
wks9.update([links8.columns.values.tolist()]+links8.values.tolist())
