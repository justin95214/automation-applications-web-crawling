import selenium as html_table_parser
import  pandas as pd
import bs4


from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import time
from datetime import datetime, timedelta
import pyautogui



import os
import subprocess
import sys
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
warnings.filterwarnings('ignore')
import log_package as lp
import logging
import func_file as ff
import xpath_data as xpath
import sel_option as s_option

def setting_project():
    #log 설정
    logger = lp.log_setting(logging)
    # 패키지 설치 시도
    try:
        import selenium
        import pandas as pd
        import datetime
        import requests
        import pyautogui
        import keyboard_code
        logger.info("package installed completed!")

    except:
        libraries = ['selenium', 'bs4', 'pandas', 'datetime', 'html_table_parser', 'reguests', 'atlassian-python-api',
                     'pyautogui']
        for i in libraries:
            logger.warning(f'not installed package {i}')

            if i == 'pyautogui':
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
            else:
                logger.warning('another excepted')
                # subprocess.check_call([sys.executable, ' conda install - c conda - forge pyautogui', i])

        import keyboard_code
        import selenium
        import pandas as pd
        import datetime
        import requests
        import pyautogui
