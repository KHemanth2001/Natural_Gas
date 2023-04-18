from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
path=DIR_PATH+'\_Output'
print(path)
try:
     os.mkdir(path)
except OSError as error:
     print(error)
options = webdriver.ChromeOptions();
options.add_experimental_option("prefs",{"download.default_directory" : path})

driver = webdriver.Chrome(service_log_path="D:/selenium/chromedriver.exe",chrome_options=options)
driver.get("https://www.cores.es/en/estadisticas")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a[title='gas-imports.xlsx']").send_keys(Keys.ENTER)
time.sleep(5)

p=os.path.abspath('gas-imports.xlsx')

df = pd.read_excel(p, sheet_name='Africa',usecols='A:Q',header=5)
df=df.iloc[:248]
csv_path=path+'\Gas-Imports.csv'

df.to_csv(csv_path,index=False)
driver.close()
