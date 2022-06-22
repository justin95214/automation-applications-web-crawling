import subprocess
import sys
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
warnings.filterwarnings('ignore')
import log_package2 as lp2
import logging
import module_file as mf
import func_file as ff
import xpath_data as xpath
import sel_option as s_option
import inspect
import schedule
import send__email as s_email
from msedge.selenium_tools import EdgeOptions

#log 설정
logger = lp2.log_setting(logging)
source_url = xpath.source_url


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

#패키지 설정
mf.setting_project()


#edge = mf.webdriver.Ie(executable_path=xpath.IE_url, options=ieOptions)

# 날짜
#today_date = ff.today_input_format()
#tomorrow = ff.other_day_input_format(1)

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

    def change_date_time(self,date):
        try:
            # datetime select
            date_checkbox = xpath.date_checkbox
            input_date = self.driver.find_element_by_xpath(date_checkbox)
            input_date.click()
            # driver.execute_script("arguments[0].click();", input_date)
            for k in range(0, 8):
                input_date.send_keys(mf.Keys.BACKSPACE)

            input_date.send_keys(date)
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

def test_func():
    # 크롤링 주소
    url = xpath.url


    # 크롤링 옵션
    ieOptions = mf.webdriver.IeOptions()
    ieOptions.ignore_protected_mode_settings = True
    ieOptions.ATTACH_TO_EDGE_CHROME = True
    ieOptions.EDGE_EXECUTABLE_PATH = url
    edge = mf.webdriver.Ie(executable_path=xpath.IE_url, options=ieOptions)



    #test = Samsung_W(edge, url)

    #test.run()
    #test.login(1)
    #test.small_pop_alert_window(xpath.btn, 1)
    #mf.time.sleep(60)

    test_class = Samsung_W(edge, url)


    def first_step_get_url_login():
        try:
            autolog_info()
            test_class.run()

            img_capture1_2 = mf.pyautogui.locateOnScreen(xpath.source_url + "check_button.png")
            print("img_capture1_1", type(img_capture1_2))
            mf.time.sleep(1)



            test_class.login(1)
            mf.time.sleep(10)
            test_class.small_pop_alert_window(xpath.btn,2)
        except:
            error_autolog()

    def second_step_big_pop_alert_window():
        try:
            autolog_info()
            test_class.big_pop_alert_window()
        except:
            error_autolog()

    def third_step_order_manage_page():
        try:
            autolog_info()
            test_class.order_manage()
        except:
            error_autolog()

    def fourth_step_center_info(idx):
        try:
            autolog_info()
            test_class.clicked_button2(xpath.receive_center, "for - CENTER ")
            center_element = "/html/body/sc-dropdown[1]/sc-listbox/div[" + str(idx) + "]"
            test_class.clicked_button2(center_element, "for - CENTER ")
        except:


            error_autolog()

    def fifth_step_change_date(date):
        try:
            autolog_info()
            test_class.change_date_time(date)
        except:
            error_autolog()

    def sixth_step_select_firm(idx):
        try:
            autolog_info()
            firm_address = xpath.firm_address
            test_class.clicked_button2(firm_address, "for - FIRM ")
            firm_get_element = "/html/body/sc-dropdown[2]/sc-listbox/div[" + str(idx) + "]"
            test_class.clicked_button2(firm_get_element, "for - FIRM ")
        except:
            error_autolog()

    def seventh_step_search_and_check_result():
        value = 0
        try:
            autolog_info()
            test_class.search_button()
            value = test_class.nothing_check_order()

        except:
            error_autolog()

        return value

    def eighth_step_select_image():
        try:
            autolog_info()
            mf.time.sleep(1)

            # 미리 체크 되엉있을때
            img_capture1_1 = mf.pyautogui.locateOnScreen(xpath.source_url + "print1.png")
            print("img_capture1_1", type(img_capture1_1))

            mf.time.sleep(1)
            print("img_capture1_1", type(img_capture1_1))
            # cent_xy = mf.pyautogui.center(img_capture2)
            mf.pyautogui.click(img_capture1_1)

            mf.time.sleep(1)

            img_capture1_2 = mf.pyautogui.locateOnScreen(xpath.source_url + "check_button.png")
            print("img_capture1_1", type(img_capture1_2))
            mf.time.sleep(1)

            mf.pyautogui.click(img_capture1_2)

            mf.time.sleep(1)

            img_capture1_3 = mf.pyautogui.locateOnScreen(xpath.source_url + "xx.png")
            print("img_capture1_1", type(img_capture1_3))
            mf.time.sleep(1)

            mf.pyautogui.click(img_capture1_3)

            mf.time.sleep(1)





        except:
            error_autolog()




    first_step_get_url_login()
    second_step_big_pop_alert_window()
    third_step_order_manage_page()
    mf.time.sleep(1)
    center_li_element = test_class.center_data()


    for c_i in range(1,len(center_li_element)+1):
        if c_i in [1,6]:

            fourth_step_center_info(c_i)
            mf.time.sleep(0.5)
            # 날짜
            today_date = ff.today_input_format()
            tomorrow = ff.other_day_input_format(1)

            fifth_step_change_date(tomorrow)
            mf.time.sleep(0.5)

            fifth_step_change_date(tomorrow)

            firm_element = test_class.firm_info()

            for f_i in range(1, len(firm_element)+1):
                sixth_step_select_firm(f_i)

                value = seventh_step_search_and_check_result()
                count = int(value[10])

                if count != 0:
                    logger.info(f"seventh_step_search_and_check_result() | count : {count}")
                    test_class.order_button()

                    eighth_step_select_image()

                else:
                    logger.warning(f"seventh_step_search_and_check_result() | count : {count}")






schedule.every().day.at("14:56").do(test_func)

#schedule.every().day.at(ff.sch_input_format()).do(test_func)
#schedule.every().day.at("14:41").do(test_func)

while True:
    try:
        logger.debug(f'{mf.datetime.now()}')
        schedule.run_pending()



    except Exception as error:
        logger.debug(f' error point : {error}')
        logger.error(f'now time : {ff.today_input_format_detail()} | 오류 발생으로 자동 재실행')
        test_func()

    mf.time.sleep(1)


