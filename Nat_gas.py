from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
folder_name="\_Output"
path=DIR_PATH+folder_name
options = webdriver.ChromeOptions();
options.add_experimental_option("prefs",{"download.default_directory" : path});

driver = webdriver.Chrome(service_log_path="D:/selenium/chromedriver.exe",chrome_options=options)
driver.get("https://www.cores.es/en/estadisticas")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a[title='gas-imports.xlsx']").send_keys(Keys.ENTER)
time.sleep(5)

path=DIR_PATH+"\_Output"
df = pd.read_excel(path+"\gas-imports.xlsx", sheet_name='All',usecols='A:Q',header=5)
df=df.iloc[:248]
df.to_csv('Gas-Imports.csv',index=False)
