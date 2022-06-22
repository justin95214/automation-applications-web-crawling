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
import inspect
import schedule
import send__email as s_email
def send_alert_email(string):
    title_string = "입문증 출력 오류"
    s_email.send_email(title_string, string)


def autolog():
    "Automatically log the current function details."
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logger.debug("%s: %s in %s:%i" % (
        "SUCCESS",
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))

def autolog_info():
    "Automatically log the current function details."
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logger.info("%s: %s in %s:%i" % (
        "SUCCESS",
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))

def error_autolog():
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logger.error("%s: %s in %s:%i" % (
        "ERROR",
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))
    send_alert_email(func.co_name)

def error_autolog_big_alert():
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logger.error("%s: %s in %s:%i" % (
        "ERROR",
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))

#log 설정
logger = lp.log_setting(logging)

class Samsung_W:
    def __init__(self, driver: mf.webdriver, url) -> None:
        self.driver = driver
        self.url = url
        logger.info(f'driver : {mf.webdriver} | url : {url} ')
        autolog()

    def run(self):
        self.driver.get(self.url)
        autolog()

    def clicked_button1(self,address, string):

        btn = self.driver.find_element_by_xpath(address)
        try:
            autolog()

            self.driver.execute_script("arguments[0].click();", btn)
            logger.warning(f'func : ({string}) >> clicked_button <1> | arguments[0].click() ')

        except:
            error_autolog()

            btn.click()
            logger.warning(f'func : ({string}) >> clicked_button <1> |click() ')


    def clicked_button2(self,address, string):

        btn = self.driver.find_element_by_xpath(address)
        try:
            autolog()
            btn.click()
            logger.warning(f'func : ({string}) >> clicked_button <1> |click() ')


        except:
            error_autolog()

            self.driver.execute_script("arguments[0].click();", btn)
            logger.warning(f'func : ({string}) >> clicked_button <1> | arguments[0].click() ')

    def clicked_button3(self,address, string):

        btn = self.driver.find_element_by_xpath(address)
        try:
            autolog()

            self.driver.execute_script("arguments[0].click();", btn)
            logger.warning(f'func : ({string}) >> clicked_button <1> | arguments[0].click() ')

        except:
            autolog()

            btn.click()
            logger.warning(f'func : ({string}) >> clicked_button <1> |click() ')




    def login(self, time):
        try:
            self.driver.find_element_by_name('username').send_keys(xpath.id)
            # pwd
            self.driver.find_element_by_name('password').send_keys(xpath.pwd)
            # login button
            login_button = xpath.login_button
            self.clicked_button1(login_button, "login")
            autolog()
            mf.time.sleep(time)
        except:
            error_autolog()

    def small_pop_alert_window(self, address, time):
        self.clicked_button1(address, "small_pop_alert_window")
        # 팝업창1 닫기
        mf.time.sleep(time)
        #화면 창 최대로
        self.driver.maximize_window()


    def big_pop_alert_window(self):
        # 큰 팝업창 여러개 닫기
        first_new_box = xpath.first_new_box
        front = '/html/body/sc-window['
        count = first_new_box[len(front):len(front) + 1]

        for i in range(int(count) * 10, 0, -1):
            try:
                name = '/html/body/sc-window[' + str(i) + ']/sc-toolbar/sc-button[3]'

                self.small_pop_alert_window(name,0)
                logger.info(f'func : big >> small alert notice pages index :, {i}')
                autolog()
            except:
                error_autolog_big_alert()


    def order_manage(self):
        try:
            # 발주 납품관리
            self.clicked_button2(xpath.report_manage, "order_manage")
            mf.time.sleep(0.5)

            # 발주 관리
            btn_manage = xpath.order_manage
            self.clicked_button2(btn_manage, "order_manage")
        except:
            error_autolog()

    def center_data(self):
        li_element = ""
        try:
            receive_button = xpath.receive_button
            self.clicked_button2(receive_button,"center_data")
            # center selection
            receive_center = xpath.receive_center
            self.clicked_button2(receive_center,"center_data")

            ## center_get_list
            center_address = xpath.center_address
            dropdown = self.driver.find_element_by_xpath(center_address)
            li_element = dropdown.find_elements_by_tag_name('div')

        except:
            error_autolog()

        return li_element

    def change_date_time(self, tomorrow):
        try:
            # datetime select
            date_checkbox = xpath.date_checkbox
            input_date = self.driver.find_element_by_xpath(date_checkbox)
            input_date.click()
            # driver.execute_script("arguments[0].click();", input_date)
            for k in range(0, 8):
                input_date.send_keys(mf.Keys.BACKSPACE)

            input_date.send_keys(tomorrow)
        except:
            error_autolog()


    def firm_info(self):
        firm_element= ""
        try:
            ## firm select
            firm_address = xpath.firm_address
            self.clicked_button2(firm_address, "firm_info")
            firm_list_address = xpath.firm_list_address
            dropdown_firm = self.driver.find_element_by_xpath(firm_list_address)
            firm_element = dropdown_firm.find_elements_by_tag_name('div')
        except:
            error_autolog()

        return firm_element

    def search_button(self):
        try:
            search_button_address = xpath.search_button_address
            self.clicked_button2(search_button_address, "search_button")
        except:
            error_autolog()

    def nothing_check_order(self):
        value = 0
        try:
            address_alert = xpath.address_alert
            value = self.driver.find_element_by_xpath(address_alert).text
        except:
            error_autolog()

        return value

    def order_button(self):
        order_button_address = xpath.order_button_address
        k = self.driver.find_element_by_xpath(order_button_address) #.click()
        self.driver.execute_script("arguments[0].click();", k)

    def close_windows(self):
        self.driver.close()
