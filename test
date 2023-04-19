from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

# DIR_PATH = os.path.abspath(os.path.dirname(__file__))
# # folder_name="\_Output"
# path=DIR_PATH
# # path=DIR_PATH+folder_name
# options = webdriver.ChromeOptions() ;
# prefs = {"download.default_directory" : path};
# options.add_experimental_option("prefs",prefs);

def generatebrowser(chromedriver_url):
     DIR_PATH = os.path.abspath(os.path.dirname(__file__))
     # folder_name="\_Output"
     path = DIR_PATH
     # path=DIR_PATH+folder_name
     options = webdriver.ChromeOptions();
     prefs = {"download.default_directory": path};
     options.add_experimental_option("prefs", prefs);
    # options = webdriver.ChromeOptions()
     driver = webdriver.Chrome(service_log_path=chromedriver_url, options=options)
     driver.get("https://www.cores.es/en/estadisticas")
     driver.maximize_window()
     time.sleep(5)
     driver.find_element(By.CSS_SELECTOR, "a[title='gas-imports.xlsx']").send_keys(Keys.ENTER)
     time.sleep(5)

def generate_file():
    path=os.path.abspath('gas-imports.xlsx')
    df=pd.read_excel(path,sheet_name='Africa',usecols='A:Q',header=5)
    df=df.loc[:248]
    DIR_PATH = os.path.abspath(os.path.dirname(__file__))
    folder_name = "\_Output"
    path = os.path.join(DIR_PATH, folder_name)
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    csv_path=path+"\Gas-Imports.csv"
    print(csv_path)
    df.to_csv(os.path.join('_Output', 'Gas-Imports.csv'),index=False)






generatebrowser("D:/selenium/chromedriver.exe")
generate_file()

