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
import module_file as mf
import func_file as ff
import xpath_data as xpath
import sel_option as s_option
from bs4 import BeautifulSoup


#log 설정
logger = lp.log_setting(logging)

#패키지 설정
mf.setting_project()


# 크롤링 주소
url = xpath.url
source_url = xpath.source_url

# 크롤링 옵션
options = mf.webdriver.ChromeOptions()
profile = s_option.profile
options.add_experimental_option("prefs", profile)


class Samsung_W:
    def __init__(self, driver: mf.webdriver, url) -> None:
        self.driver = driver
        self.url = url
        logger.info(f'driver : {mf.webdriver} | url : {url} ')

    def run(self):
        self.driver.get(self.url)
        logger.info('func : run() >> driver.get  ')

    def login(self):
        ### login
        # Id
        self.driver.find_element_by_name('username').send_keys(xpath.id)
        # pwd
        self.driver.find_element_by_name('password').send_keys(xpath.pwd)
        # login button
        login_button = xpath.login_button
        self.driver.find_element_by_xpath(login_button).click()
        logger.info(f'func : login () >> | ID : {xpath.id} | pwd : {xpath.pwd} ')
        mf.time.sleep(2)

    def closed_alert_window(self, address,time, string):
        btn = self.driver.find_element_by_xpath(address)
        try:
            self.driver.execute_script("arguments[0].click();", btn)
        except:
            btn.click()


        logger.info(f'func : closed_alert_window() >> | address : {address} | message : {string}')
        #self.driver.implicitly_wait(time)
        mf.time.sleep(time)

    def closed_big_alert_window(self, address):
        # 큰 팝업창 여러개 닫기
        # ex) /html/body/sc-window[10]/sc-toolbar/sc-button[3]
        first_new_box =  address
        front = '/html/body/sc-window['
        count = first_new_box[len(front):len(front) + 1]

        for i in range(int(count) * 10, 0, -1):
            try:
                name = '/html/body/sc-window[' + str(i) + ']/sc-toolbar/sc-button[3]'

                self.closed_alert_window(name,0, "closed_big_alert_window   " +str(i)+" 번째 팝업창 닫기")

            except:
                logger.warning(f'func : closed_alert_window() >> | not notice pages index :, {i}')


    def clicked_button1(self,address, time, string):
        try:
            btn = self.driver.find_element_by_xpath(address)
            self.driver.execute_script("arguments[0].click();", btn)
            #logger.warning(f'func : clicked_button <1>({string}) >> | arguments[0].click() ')
        except:
            logger.error(f'func : clicked_button <1>({string}) >> | arguments[0].click() ')

        mf.time.sleep(time)



    def clicked_button2(self,address, time, string):
        btn = self.driver.find_element_by_xpath(address)
        btn.click()
        logger.warning(f'func : clicked_button <2>({string}) >> | click() ')

        mf.time.sleep(time)

    def clicked_button3(self,address, time, string, state):
        try :
            state = True
            btn = self.driver.find_element_by_xpath(address)
            self.driver.execute_script("arguments[0].click();", btn)

        except:
            state =False

        #logger.warning(f'func : clicked_button <1>({string}) >> | arguments[0].click() | state : {state}')
        mf.time.sleep(time)
        return state

    def css_clicked_button1(self,address, time, string):
        btn = self.driver.find_element_by_css_selector(address)
        self.driver.execute_script("arguments[0].click();", btn)
        #mf.time.sleep(1)

        #logger.error(f'checkbox stutus1 : {btn.isChecked()}')
        #logger.error(f'checkbox stutus3 : {btn.get_attribute("checked")}')

        #logger.warning(f'func : clicked_button <2>({string}) >> | click() ')

        mf.time.sleep(time)


    def check_checkbox(self, address, string):
        test0 = self.driver.find_element_by_xpath(address).get_attribute('checked')

        logger.info(f'test :{test0} | {string}')
        #class_name = self.driver.find_element_by_class_name('check-default style-scope sc-checkbox-field')
        #logger.info(f'{class_name}')

        if test0 == 'true':
            logger.debug(f'checkbox already checked')
        else:
            logger.debug(f'checkbox not checked')

        return test0

    def init_checkbox_setting(self,address1, address2, time, string):
        check_box_list = []
        check_1 = address1#xpath.check_11
        check_2 = address2#xpath.check_22
        check_box_list.append(check_1)
        check_box_list.append(check_2)

        self.css_clicked_button1(check_1, 0, "checkbox1 inited")
        self.css_clicked_button1(check_2, 0, "checkbox2 inited")

        logger.warning(f'func : init_checkbox_setting >> ({string})  ')
        mf.time.sleep(time)
        return check_box_list

    def click_checkbox(self,address, time):
        self.driver.find_element_by_xpath(address).click()
        mf.time.sleep(time)


    def get_tag_list(self, address, element, string):

        dropdown = self.driver.find_element_by_xpath(address)
        li_element = dropdown.find_elements_by_tag_name(element)

        get_list = ff.get_list_value(li_element)
        logger.info(f'func : get_tag_list() >> | {string}_list : {get_list}')

        return li_element, get_list


    def get_value(self, address, element, string):
        value = self.driver.find_element_by_xpath(address).text

        logger.debug(f'func : get_value() >> | {string} |  value : {value}')

        return value



    def make_except_list(self, list):
        execept_list = list[1:3]
        logger.info(f'func : get_tag_list() >> | execept_list : {execept_list}')
        return execept_list

    def chanage_datetime(self, address, time, change_date):
        input_date = self.driver.find_element_by_xpath(address)
        self.driver.execute_script("arguments[0].click();", input_date)
        ff.date_delete(input_date)
        mf.time.sleep(time)
        input_date.send_keys(change_date)
        logger.info(f'func : chanage_datetime() >> | date : {change_date}')


    def implic_time_sleep(self,time):
        self.driver.implicitly_wait(time)

    def finished_crawling(self):
        self.driver.close()

    def max_size_chrome_windows(self):
        self.driver.maximize_window()

    def find_image(self, address, time, string):
        state = True
        try:
            mf.time.sleep(time)
            img_capture = mf.pyautogui.locateOnScreen(address)

            mf.pyautogui.click(img_capture)
            state = isinstance(img_capture,type(None))
            if state == False :
                raise

            logger.info(f'func : find_image() >> | image : {address} | checked image varable : {state}  오류상태 | wait time : {time} | message : {string}')

        except:
            logger.error(f'func : find_image() >> | image : {address} | checked image varable : {state}  정상상태 | wait time : {time}  | message : {string}')

        return state


