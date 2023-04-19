from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

def generatebrowser(chromedriver_url):
    options = webdriver.ChromeOptions();
    driver = webdriver.Chrome(service_log_path=chromedriver_url, chrome_options=options)
    driver.get("https://www.cores.es/en/estadisticas")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "a[title='gas-imports.xlsx']").send_keys(Keys.ENTER)
    time.sleep(5)

def generate_file():
    path=os.path.abspath('gas-imports.xlsx')
    df=pd.read_excel(path,sheet_name='Africa',usecols='A:Q',header=5)
    df=df.loc[:248]
    print(df)




generatebrowser("D:/selenium/chromedriver.exe")
generate_file()
