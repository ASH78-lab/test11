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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import requests

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def pin_tod():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
        
    headers = {
            'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Referer': 'habr.com'
            }
        
    abc5=[
        'https://www.betexplorer.com/football/england/efl-cup/fixtures/',
        'https://www.betexplorer.com/football/england/fa-cup/fixtures/',
        'https://www.betexplorer.com/football/england/premier-league/fixtures/',
        'https://www.betexplorer.com/football/england/fa-community-shield/fixtures/',
        'https://www.betexplorer.com/football/england/championship/fixtures/',
        'https://www.betexplorer.com/football/france/coupe-de-france/fixtures/',
        'https://www.betexplorer.com/football/france/ligue-1/fixtures/',
        'https://www.betexplorer.com/football/france/super-cup/fixtures/',
        'https://www.betexplorer.com/football/germany/bundesliga/fixtures/',
        'https://www.betexplorer.com/football/germany/dfb-pokal/fixtures/',
        'https://www.betexplorer.com/football/germany/super-cup/fixtures/',
        'https://www.betexplorer.com/football/germany/2-bundesliga/fixtures/',
        'https://www.betexplorer.com/football/italy/coppa-italia/fixtures/',
        'https://www.betexplorer.com/football/italy/serie-a/fixtures/',
        'https://www.betexplorer.com/football/italy/super-cup/fixtures/',
        'https://www.betexplorer.com/football/spain/copa-del-rey/fixtures/',
        'https://www.betexplorer.com/football/spain/laliga/fixtures/',
        'https://www.betexplorer.com/football/spain/super-cup/fixtures/',
        'https://www.betexplorer.com/football/russia/russian-cup/fixtures/?stage=nmUWpCn5',
        'https://www.betexplorer.com/football/russia/russian-cup/fixtures/?stage=CKtlqjHH',    
        'https://www.betexplorer.com/football/russia/premier-league/fixtures/',
        'https://www.betexplorer.com/football/russia/super-cup/fixtures/',
        'https://www.betexplorer.com/football/russia/fnl/fixtures/',
        'https://www.betexplorer.com/football/europe/champions-league/fixtures/',
        'https://www.betexplorer.com/football/europe/europa-league/fixtures/',
        'https://www.betexplorer.com/football/europe/conference-league/fixtures/',
        'https://www.betexplorer.com/football/europe/euro-2024/fixtures/?stage=Ya0Rvy04',
        'https://www.betexplorer.com/football/europe/euro-2024/fixtures/?stage=SMaVweFA',
        'https://www.betexplorer.com/football/europe/uefa-nations-league/fixtures/?stage=QgTkX5FP',
        'https://www.betexplorer.com/football/europe/uefa-nations-league/fixtures/?stage=pvAMRqwm',
        'https://www.betexplorer.com/football/europe/uefa-nations-league/fixtures/?stage=OU8QQ3hg',
        'https://www.betexplorer.com/football/europe/uefa-nations-league/fixtures/?stage=h4DUPN7a',
        'https://www.betexplorer.com/football/world/friendly-international/',
        'https://www.betexplorer.com/football/world/world-championship-2026/fixtures/?stage=QmflJo77&activecountry=8bP2bXmH',
        'https://www.betexplorer.com/football/world/world-cup-2026/fixtures/'
        
        
        # https://www.betexplorer.com/football/england/fa-cup/fixtures/
        ]
    
    abc=['England - EFL Cup', 
         'England - FA Cup', 
         'England - Premier League',
           'England - Community Shield', 
           'England - Championship',
             'France - Cup', 
             'France - Ligue 1', 
             'France - Super Cup', 
             'Germany - Bundesliga',
               'Germany - Cup', 
               'Germany - Super Cup',
               'Germany - Bundesliga 2', 
               'Italy - Cup', 
               'Italy - Serie A', 
               '-', 
               'Spain - Copa del Rey', 
               'Spain - La Liga', 
               'Spain - Super Cup',
               'Russia - Cup', 
               '-', 
               'Russia - Premier League',
                 '-', 
                 'Russia - First League', 
                 'UEFA - Champions League', 
                 'UEFA - Europa League', 
                 'UEFA - Conference League', 
                 '-', 
                 '-', 
                 '-', 
                 '-', 
                 '-', 
                 '-',
                 'UEFA - Nations League Playoffs',
                'International - Friendlies', 
                'FIFA - World Cup Qualifiers Europe',
                'FIFA - World Cup']
    epl=[
        'https://www.pinnacle.com/en/soccer/england-efl-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/england-fa-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/england-premier-league/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/england-community-shield/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/england-championship/matchups/#period:0 ',
        'https://www.pinnacle.com/en/soccer/france-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/france-ligue-1/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/france-super-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/germany-bundesliga/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/germany-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/germany-super-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/germany-bundesliga-2/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/italy-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/italy-serie-a/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/italy-super-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/spain-copa-del-rey/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/spain-la-liga/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/spain-super-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/russia-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/russia-cup-regions-path/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/russia-premier-league/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/russia-super-cup/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/russia-first-league/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-champions-league/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-europa-league/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-conference-league/matchups/',
        'https://www.pinnacle.com/en/soccer/uefa-euro-qualifiers/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-euro/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-nations-league-a/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-nations-league-b/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-nations-league-c/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-nations-league-d/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/uefa-nations-league-playoffs/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/international-friendlies/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/fifa-world-cup-qualifiers-europe/matchups/#period:0',
        'https://www.pinnacle.com/en/soccer/fifa-world-cup/matchups/#period:0'
      
        ]
    slovar2= dict(zip(abc,epl))
        
    new=[]

    from datetime import datetime
    current_datetime = str(datetime.now())
    b=current_datetime.split("-")
    c=b[0]
    d=b[1]
    e=b[2].split(" ")
    f=e[0]
    g=e[1]
    kl=g.split(".")
    io=kl[0]
    ty=io.replace(io[:2],str(int(io[:2])+3))
    date_new256=f+'.'+d+'.'+c+'  '+ty

    wks2 = gc.open("Test789").get_worksheet(0)
    list_of_lists = wks2.get_all_values()
    df50 = pd.DataFrame(list_of_lists)

    today=f+'.'+d+'.'+c
    filt_date_df5=df50[df50[0]==today]
    name_league=filt_date_df5[2]
    ert96=name_league.drop_duplicates()
    ert97=ert96.to_list()

    for i in abc:

        if i in ert97:
            new.append(slovar2[i])
        else:
            pass
        
    
    
    
    
    
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from selenium.webdriver.common.keys import Keys
    from datetime import datetime
    import requests
    from selenium.webdriver.firefox.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    
    import os
    date_new53 = str(datetime.now())
    print(date_new53)
    a123=time.time()
    now = datetime.now()
    future_time = now + timedelta(hours=3)
    par_tm = future_time.strftime('%d.%m.%Y %H:%M:%S')
    
    
    
    
    
    
    
    
    
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.set_window_size(1800, 800) 
    driver.get("https://www.pinnacle.com/en/")
    time.sleep(20)
        
    
    
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    from datetime import datetime
    current_datetime = str(datetime.now())
    b=current_datetime.split("-")
    c=b[0]
    d=b[1]
    e=b[2].split(" ")
    f=e[0]
    g=e[1]
    kl=g.split(".")
    io=kl[0]
    ty=io.replace(io[:2],str(int(io[:2])+3))
    date_new256=f+'.'+d+'.'+c+'  '+ty
        
    many=0   
        
        
    #---------------------------------------
    data=[]
    new.append('https://www.pinnacle.com/en/soccer/fifa-world-cup/matchups/#period:0')
    for i in new:
        driver.get(i)
        time.sleep(11)
            
        try:
            ttest = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div[2]/main/div/div[1]/div[3]/div/div/div/div')))
            ttest=ttest.text
            
            sd="TODAY"
            if sd in ttest:
                    
          #--------------------------------------              
                button = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/main/div/div[1]/div[3]/div/div/div/div/button[2]")
                button.click()
                        
                time.sleep(6)
                        
                try:
                    tournemebt=driver.find_elements(By.CLASS_NAME, 'textLabel-lNJMfvP1Hd')[1].text
                    if "UEFA - Nations League" in tournemebt:
                        tournemebt="UEFA - Nations League"
                    elif "Regions Path" in tournemebt:
                        tournemebt="Russia - Cup"
                    elif "Spain - Super Cup" in tournemebt:
                        tournemebt="Spain - Copa del Rey"
                    elif "Italy - Super Cup" in tournemebt:
                        tournemebt="Italy - Cup"
                    elif "England - FA Cup" in tournemebt:
                        tournemebt="England - EFL Cup"
                    elif "England - Community Shield" in tournemebt:
                        tournemebt="England - EFL Cup"
                    elif "UEFA - Super Cup" in tournemebt:
                        tournemebt="UEFA - Champions League"
                    elif "Germany - Super Cup" in tournemebt:
                        tournemebt="Germany - Cup"
                    elif "France - Super Cup" in tournemebt:
                        tournemebt="France - Cup"
                    elif "FIFA - World Cup" in tournemebt:
                        tournemebt="UEFA - Nations League"
                    elif "Russia - Super Cup" in tournemebt:
                        tournemebt="Russia - Cup"

                  
                    rd=driver.find_elements(By.XPATH,"/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div")
                    er=len(rd)+1
                    many=many+1
                        
    
                    
                
                
                
                
                
                
                
                    
                    for j in range(1,er):
                            
                        current_datetime = str(datetime.now())
                        b=current_datetime.split("-")
                        cee=b[0]
                        d=b[1]
                        e=b[2].split(" ")
                        f=e[0]
                        date_new=f+'.'+d+'.'+cee
                        
                        ert=date_new
                        
                        try:
                            ert2=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[1]/div/a/div/div/div[3]').text
                            ert209=ert2.split(":")
                            ert210=int(ert209[0])+3
                            ert211=str(ert210)+":"+ert209[1]
                        except NoSuchElementException:
                            ert211='-'
                                    
                        try:
                            ert3=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[1]/div/a/div/div/div[1]/span').text
                            ert3=ert3.split(" (")
                            ert3=ert3[0]
                                
                        except NoSuchElementException:
                            ert3='-'
                        try:
                            ert4=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[1]/div/a/div/div/div[2]/span').text
                            ert4=ert4.split(" (")
                            ert4=ert4[0]
                                
                        except NoSuchElementException:
                            ert4='-'
                                    
                        try:
                            ert5=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[2]/div[1]/button/span').text
                               
                            #ert5=float(ert5)
                        
                                
                        except NoSuchElementException:
                            ert5='-'
                        try:
                            ert6=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[2]/div[2]/button/span').text
                               
                            #ert6=float(ert6)
                                
                        except NoSuchElementException:
                            ert6='-'
                                    
                        try:
                            ert7=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[2]/div[3]/button/span').text
                                
                            #ert7=float(ert7)
                                
                        except NoSuchElementException:
                            ert7='-'
                        try:
                            ert8=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[3]/div[1]/button/span[1]').text
                               
                            #ert8=float(ert8)
                                
                        except NoSuchElementException:
                            ert8='-'
                                    
                        try:
                            ert9=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[3]/div[1]/button/span[2]').text
                                
                            #ert9=float(ert9)
                                
                        except NoSuchElementException:
                            ert9='-'
    
                        
                        try:
                            ert10=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div/div/div[{j}]/div[3]/div[2]/button/span[2]').text
                            #ert10=float(ert10)
                                
                        except NoSuchElementException:
                            ert10='-'
    
                        
                        ert11=date_new256
                        
                        data.append([ert,ert211,tournemebt,ert3,ert4,ert5,ert6,ert7,ert8,ert9,ert10,ert11])
                except IndexError:
                    pass
                
    
        except (NoSuchElementException,TimeoutException) :
            try:
                tournemebt=driver.find_elements(By.CLASS_NAME, 'textLabel-lNJMfvP1Hd')[1].text
                if "UEFA - Nations League" in tournemebt:
                    tournemebt="UEFA - Nations League"
                elif "Regions Path" in tournemebt:
                    tournemebt="Russia - Cup"
                elif "Spain - Super Cup" in tournemebt:
                    tournemebt="Spain - Copa del Rey"
                elif "Italy - Super Cup" in tournemebt:
                    tournemebt="Italy - Cup"
                elif "England - FA Cup" in tournemebt:
                    tournemebt="England - EFL Cup"
                elif "England - Community Shield" in tournemebt:
                    tournemebt="England - EFL Cup"
                elif "UEFA - Super Cup" in tournemebt:
                    tournemebt="UEFA - Champions League"
                elif "Germany - Super Cup" in tournemebt:
                    tournemebt="Germany - Cup"
                elif "France - Super Cup" in tournemebt:
                    tournemebt="France - Cup"
                elif "FIFA - World Cup" in tournemebt:
                    tournemebt="UEFA - Nations League"
                elif "Russia - Super Cup" in tournemebt:
                    tournemebt="Russia - Cup"
                  
              
                rd=driver.find_elements(By.XPATH,"/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div")
                er=len(rd)+1
                many=many+1
                             
            #except IndexError:
                #pass
                for j in range(1,er):
            
                    current_datetime = str(datetime.now())
                    b=current_datetime.split("-")
                    cee=b[0]
                    d=b[1]
                    e=b[2].split(" ")
                    f=e[0]
                    date_new=f+'.'+d+'.'+cee
                    
                    ert=date_new
                 
                    
                    
                    
                  
                    
                     
                    
                     
                    try:
                        ert2=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[1]/div/a/div/div/div[3]').text
                        ert209=ert2.split(":")
                        ert210=int(ert209[0])+3
                        ert211=str(ert210)+":"+ert209[1]
                    except NoSuchElementException:
                        ert211='-'
                
                    try:
                        ert3=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[1]/div/a/div/div/div[1]/span').text
                        ert3=ert3.split(" (")
                        ert3=ert3[0]
                            
                    except NoSuchElementException:
                        ert3='-'
                    try:
                        ert4=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[1]/div/a/div/div/div[2]/span').text
                        ert4=ert4.split(" (")
                        ert4=ert4[0]
                            
                    except NoSuchElementException:
                        ert4='-'
                
                    try:
                        ert5=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[2]/div[1]/button/span').text
                           
                        #ert5=float(ert5)
                    
                            
                    except NoSuchElementException:
                        ert5='-'
                    try:
                        ert6=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[2]/div[2]/button/span').text
                           
                        #ert6=float(ert6)
                            
                    except NoSuchElementException:
                        ert6='-'
                
                    try:
                        ert7=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[2]/div[3]/button/span').text
                            
                        #ert7=float(ert7)
                            
                    except NoSuchElementException:
                        ert7='-'
                    try:
                        ert8=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[3]/div[1]/button/span[1]').text
                           
                        #ert8=float(ert8)
                            
                    except NoSuchElementException:
                        ert8='-'
                
                    try:
                        ert9=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[3]/div[1]/button/span[2]').text
                            
                        #ert9=float(ert9)
                            
                    except NoSuchElementException:
                        ert9='-'
                
                    
                    try:
                        ert10=driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]/div[3]/div[2]/button/span[2]').text
                        #ert10=float(ert10)
                            
                    except NoSuchElementException:
                        ert10='-'
                
                    
                    ert11=date_new256
                    
                    data.append([ert,ert211,tournemebt,ert3,ert4,ert5,ert6,ert7,ert8,ert9,ert10,par_tm])
    
    
            except IndexError:
                pass
    
                    
        except(IndexError,NoSuchElementException):
            pass
                
                
                    
                    
                        
    
    
    driver.quit()
    header = ['date',
         'time',
         'league',
         'Столбец3',
         'Столбец4',
         '1',
         'X',
         '2',
         'handicap',
         'H',
         'A',
         'Столбец11']
    df = pd.DataFrame(data, columns=header)
    df = df.loc[df['X'] != '-']
    
    print(df)
    driver.quit()

    
    
    #-------------------------------------------------------------------------------------------------------------------------------
    date_new533 = str(datetime.now())
    print(date_new533)
    
    b123=time.time()
    delta1=b123-a123
    name_fun='Pinnacle_tod'
    data=[]
    data.append([date_new53,date_new533,delta1,name_fun,many])
    
    
    header = ['run',
      'end',
      'delta',
      'name','many']
    df2 = pd.DataFrame(data, columns=header)
    print(df,df2)
    
    
    
    wks2 = gc.open("Test789").sheet1
    list_of_lists = wks2.get_all_values()
    df5 = pd.DataFrame(list_of_lists)
    new_header = df5.iloc[0]
    df5 = df5[1:]
    df5.rename(columns=new_header, inplace=True)
    df7=pd.concat([df5,df])
    
    wks2.update([df7.columns.values.tolist()]+df7.values.tolist())
    
    
    
    wks2 = gc.open("Test789").get_worksheet(1)
    list_of_lists = wks2.get_all_values()
    df5 = pd.DataFrame(list_of_lists)
    new_header = df5.iloc[0]
    df5 = df5[1:]
    df5.rename(columns=new_header, inplace=True)
    df7=pd.concat([df5,df2])
    
    wks2.update([df7.columns.values.tolist()]+df7.values.tolist())

gc = gspread.service_account_from_dict(credentials)


wks2 = gc.open("Test789").get_worksheet(3)
list_of_lists = wks2.get_all_values()
df5 = pd.DataFrame(list_of_lists)

new_header = df5.iloc[0]  # берем первую строку как заголовок
df5 = df5[1:]
# переименовываем столбцы
df5.rename(columns=new_header, inplace=True) 
df5=df5[['col1','col2']]

df5=df5[df5['col2']=='pin']
znach=int(df5['col1'])

wks3 = gc.open("Test789").get_worksheet(4)
znach2 = int(wks3.acell('A1').value)

if znach==1:
    pin_tod()
elif znach2==1:
    pin_tod()
else:
    pass
