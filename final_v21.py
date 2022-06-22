# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time
import warnings

import pyautogui
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException, ElementNotInteractableException,NoSuchWindowException, NoSuchFrameException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import send__email as s_email
import datetime
import schedule
import re
warnings.filterwarnings('ignore')
import log_package as lp
import logging
import module_file as mf
import func_file as ff
import xpath_data as xpath
import sel_option as s_option
import samsung_well as sw
from bs4 import BeautifulSoup

# log 설정
logger = lp.log_setting(logging)

# 패키지 설정
mf.setting_project()

# 크롤링 주소
url = xpath.url
source_url = xpath.source_url

# 크롤링 옵션
options = mf.webdriver.ChromeOptions()
profile = s_option.profile
options.add_experimental_option("prefs", profile)

# 크롤링 주소
url = xpath.url
folder = xpath.folder
source_url = xpath.source_url

#점검표 DataFrame
df_list = []
Center_name =[]
Client_name =[]
global test_complete
test_complete = True

def send_alert_email(string):
    title_string = "입고예약 오류"
    s_email.send_email(title_string, string)

def send_alert_email2(string):
    title_string = "입고예약 completed!!!"
    s_email.send_email(title_string, string)

def reserve__stock():
    # 날짜
    def weekday_check():
        plus = 2
        if ff.today_input_format_check() == 4:
            plus = 3
        else:
            plus = 2

        return plus

    today_date = ff.other_day_input_format(1)
    plus = weekday_check()
    tomorrow = ff.other_day_input_format(plus)



    def chrome_intro():
        try:
            samsung_w.run()
            # 로그인
            samsung_w.login()
            # 첫번째 팝업창 닫기

            samsung_w.closed_alert_window(xpath.btn, 10, "첫번째 팝업창 닫기")
            # 첫번째 큰 여러개 팝업창 닫기
            samsung_w.closed_big_alert_window(xpath.first_new_box1)
            # 크롬창 최대 크기
            samsung_w.max_size_chrome_windows()
            # 반드시 2s 건들이지 말것
            mf.time.sleep(5)
            # 발주 납품 관리
            samsung_w.clicked_button1(xpath.report_manage, 0.2, "발주 납품 관리")
            # 발주 납품 관리 >  발주 관리
            samsung_w.clicked_button1(xpath.btn_manage, 0.2, "발주 납품 관리 >  발주 관리")
            # 발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행
            samsung_w.clicked_button1(xpath.box_manage, 1.5, "발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행")
            logger.debug(
                f'fuc >>  chrome_intro :  # 로그인 > # 첫번째 팝업창 닫기  > # 첫번째 큰 여러개 팝업창 > # 발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행')

        except:
            logger.error("mid func : >> chrome_intro()")

    def center_part(center_list, count, btn_c, date_select):

        list_element_name = '/html/body/sc-dropdown/sc-listbox/div[' + str(count) + ']'
        # 해당 되는 물류센터 요소 선택

        samsung_w.clicked_button2(btn_c, 0.5, "센터 박스 선택하기")
        samsung_w.clicked_button1(list_element_name, 0, "해당 되는 물류센터 요소 선택")
        res_date = ""
        # 특정 센터 날짜 변경
        if center_list[count - 1] == center_list[4] or center_list[count - 1] == center_list[1]:
            samsung_w.chanage_datetime(date_select, 0.2, tomorrow)
            res_date = tomorrow
            logger.error(
                f'fuc : 특정 센터 날짜 변경 >> {tomorrow} | 센터 : {center_list[count - 1]} | 기준 : {center_list[4]}')

        else:
            samsung_w.chanage_datetime(date_select, 0.2, today_date)
            res_date = today_date
            logger.error(
                f'fuc : 나머지센터 날짜 유지 >> {today_date} | 센터 : {center_list[count - 1]} | 기준 : {center_list[4]}')

        logger.warning(
            f'fuc >>  center_part :  # 해당 되는 물류센터 요소 선택 > # 특정 센터 날짜 변경 ')

        # 기사 선택
        driver_list = []

        if center_list[count - 1] == center_list[0]:
            driver_list = ['jeong_driver', 'kim_driver']

        elif center_list[count - 1] == center_list[5]:
            driver_list = ['jeong_driver', 'song_driver']
        else:
            driver_list = ['jeong_driver', 'kim_driver']

        logger.debug(
            f'fuc : res date  >> {res_date} | 센터 : {center_list[count - 1]} | 기준 : {center_list[4]} driver list : {driver_list}')

        return driver_list ,res_date

    def client_setting_part(d):
        # "협력회사 리스트 박스 선택"

        try:
            samsung_w.clicked_button2(d, 0, "협력회사 리스트 박스 선택")
            list_box = xpath.list_box

            # 협력회사 리스트 가져오기
            li_element_client, client_list = samsung_w.get_tag_list(list_box, 'div', "협력회사 리스트 > 협력회사 선택")
            get_list = ff.get_list_value(li_element)
            CJ_food = client_list[8]
            logger.debug(
                f'fuc >>  client_setting_part :  # "협력회사 리스트 박스 선택" >  # 협력회사 리스트 가져오기 ')

        except:
            logger.error("mid func : >> client_setting_part()")

        return li_element_client, client_list, get_list

    def client_part(client_list, count_client, reserve_time):
        time = reserve_time
        logger.debug(f'{client_list[count_client - 1]}')
        if count_client == 26:
            samsung_w.clicked_button2(d, 0, "협력회사 리스트 박스 선택")
            # 협력회사 중 요소 선택
            logger.debug(f'index : {count_client}')

            count_client_name = '/html/body/sc-dropdown[2]/sc-listbox/div[26]'
            try:
                samsung_w.clicked_button2(count_client_name, 0.3, "협력회사 중 요소 선택")
            except:
                samsung_w.clicked_button1(count_client_name, 0.3, "협력회사 중 요소 선택")

            time = 'a_2100'
            logger.info(
                f'fuc : >> 협력회사 :  {client_list[count_client - 1]} | 기준 : {time}')


        else:

            if client_list[count_client] != CJ_food:
                # mf.time.sleep(1.5)
                samsung_w.clicked_button2(d, 0, "협력회사 리스트 박스 선택")
                # 협력회사 중 요소 선택
                logger.debug(f'index :  {client_list[count_client - 1]} - {count_client}')

                count_client_name = '/html/body/sc-dropdown[2]/sc-listbox/div[' + str(count_client) + ']'
                try:
                    samsung_w.clicked_button2(count_client_name, 0.3, "협력회사 중 요소 선택")
                except:
                    samsung_w.clicked_button1(count_client_name, 0.3, "협력회사 중 요소 선택")

                time = 'a_2100'
                logger.info(
                    f'fuc : >> 협력회사 :  {client_list[count_client - 1]} | 기준 : {time}')

            elif client_list[count_client] != GServe:

                samsung_w.clicked_button2(d, 0, "협력회사 리스트 박스 선택")
                # 협력회사 중 요소 선택
                logger.debug(f'index : {count_client}')
                count_client_name = '/html/body/sc-dropdown[2]/sc-listbox/div[' + str(count_client) + ']'
                # / html / body / sc - dropdown[2] / sc - listbox / div[26]
                try:
                    samsung_w.clicked_button2(count_client_name, 0.3, "협력회사 중 요소 선택")
                except:
                    samsung_w.clicked_button1(count_client_name, 0.3, "협력회사 중 요소 선택")
                time = 'a_1730'

                logger.info(
                    f'fuc : >> 협력회사 :  {client_list[count_client - 1]} | 기준 : {time}')

            else:
                logger.warning(
                    f'fuc : >> 협력회사 :  {client_list[count_client - 1]} | 기준 : {time}')

                samsung_w.clicked_button2(d, 0, "협력회사 리스트 박스 선택")
                # 협력회사 중 요소 선택
                logger.debug(f'index : {count_client}')

                count_client_name = '/html/body/sc-dropdown[2]/sc-listbox/div[' + str(count_client) + ']'

                try:
                    samsung_w.clicked_button2(count_client_name, 0.3, "협력회사 중 요소 선택")
                except:
                    samsung_w.clicked_button1(count_client_name, 0.3, "협력회사 중 요소 선택")

                time = 'a_2100'

                logger.info(
                    f'fuc : >> 협력회사 :  {client_list[count_client - 1]} | 기준 : {time}')

            logger.debug(
                f'fuc >>  client_part :  # 협력업체 조건문 >  # 협력회사 중 요소 선택 ')

        # logger.error("mid func : >> client_part()")
        # time = 'a_2100'

        return time

    def checkbox_part_input_place_setting(check_box_i):
        logger.info(
            f'fuc : for3 문 >> | 체크박스 No. {check_box_i[6:8]} 번째 ')

        # 체크박스 선택
        samsung_w.css_clicked_button1(check_box_i, 0, str(check_box_i[6:8]) + "  체크박스 선택")

        # 입고장
        try:
            samsung_w.clicked_button2(e, 0, "입고장 박스 선택 > 입고장 리스트")
        except:
            samsung_w.clicked_button1(e, 0, "입고장 박스 선택 > 입고장 리스트")

        li_element_place, place_list = samsung_w.get_tag_list(xpath.input_center, 'div', "입고장 리스트")

        logger.debug(
            f'fuc >>  checkbox_part_input_place_setting :  # 체크박스 선택 >  # 입고장 ')
        return li_element_place, place_list

    def input_place_part_search_click(e, place_list, check_p, a):
        # 입고장 요소 선택
        samsung_w.clicked_button2(e, 0, "입고장 박스 선택 ")

        count_place_name = '/html/body/sc-dropdown[3]/sc-listbox/div[' + str(place_list[check_p]) + ']'
        samsung_w.clicked_button2(count_place_name, 0, "입고장 " + place_list[check_p] + " 요소 선택")

        # 조회 버튼 클릭
        samsung_w.clicked_button2(a, 2.5, "조회 버튼 클릭")
        logger.debug(
            f'fuc >>  input_place_part_search_click :  # 입고장 요소 선택 >  # 조회 버튼 클릭 ')

    def reserve_canvase_check_first_button():
        # 입고예약 체크 박스가 미리 체크 되어있을때
        # 미리 체크된 이미지 찾기
        samsung_w.implic_time_sleep(1.5)
        samsung_w.find_image(source_url + xpath.checked_image, 1, "미리 체크된 전체 입고예약 v 체크")
        # mf.pyautogui.click(img_capture1_1)

        # 입고 예약 캠버스 버튼
        samsung_w.implic_time_sleep(1.5)
        samsung_w.find_image(source_url + xpath.input_reserve_image, 1, "전체 입고예약  v 체크")
        samsung_w.implic_time_sleep(1.5)
        # 상세 항목 선택을 위한 입고예약 버튼
        samsung_w.clicked_button2(xpath.c2, 1, "상세 항목 선택을 위한 입고예약 버튼")

        # 마우스 위치 임의로 설정
        # mf.pyautogui.moveTo(50, 50)
        mf.time.sleep(0.5)

        # 입고예약 캠버스 버튼 누룬 후 알림 확인 버튼
        state = True
        state = samsung_w.clicked_button3(xpath.alert_exc, 0.5, "입고예약 캠버스 버튼 누룬 후 알림 확인 버튼", state)
        logger.debug(
            f'fuc >>  reserve_canvase_check_first_button :  # 미리 체크된 이미지 찾기 > # 입고 예약 캠버스 버튼 >  #상세 항목 선택을 위한 입고예약 버튼 > # 입고예약 캠버스 버튼 누룬 후 알림 확인 버튼 | state : {state}')

        return state

    def detailed_reserve_complated(driver_check, driver_list, reserve_time, client, center):
        # 상세 입고 예약 차량 번호 선택
        ##################time.sleep(0.5)
        #samsung_w.caputure_image(ff.log_input_format_tdoay() + center + "_" + client)
        logger.debug(f' driver list :{driver_list}  | reserve time : {reserve_time} | driver check : {driver_check}')
        # 운전기사 선택
        if driver_check == 0:

            if driver_list[0] == 'jeong_driver':

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_jeong, 0.3, "# 상세 입고 예약 차량 번호 선택 jeong")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_jeong1, 0.3, "# 상세 입고 예약 차량 번호 선택 jeong1")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_jeong2, 0.3, "# 상세 입고 예약 차량 번호 선택 jeong2")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_jeong3, 0.3, "# 상세 입고 예약 차량 번호 선택 jeong3")


            elif driver_list[0] != 'cj_other_driver':
                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other_cj, 0.3, "# 상세 입고 예약 차량 번호 선택1")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other_cj1, 0.3, "# 상세 입고 예약 차량 번호 선택 cj 대체")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other_cj2, 0.3,
                                     "# 상세 입고 예약 차량 번호 선택 cj 대체")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other_cj3, 0.3,
                                     "# 상세 입고 예약 차량 번호 선택 cj 대체")


            elif driver_list[0] != 'jeong_driver':
                samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim, 0.3, "# 상세 입고 예약 차량 번호 선택1")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim1, 0.3, "# 상세 입고 예약 차량 번호 선택2")

            else:
                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other, 0.3, "# 상세 입고 예약 차량 번호 선택 other")

            logger.debug(
                f'fuc >>  detailed_reserve_complated |  driver name : {driver_list[0]}  |  driver_check : {driver_check} ')

        else:
            if driver_list[1] == 'song_driver':
                samsung_w.find_image(source_url + xpath.reserve_truck_driver_song, 0.3, "# 상세 입고 예약 차량 번호 선택")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_song1, 0.3, "# 상세 입고 예약 차량 번호 선택1")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_song2, 0.3, "# 상세 입고 예약 차량 번호 선택2")


            elif driver_list[1] == 'kim_driver':

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim, 0.3, "# 상세 입고 예약 차량 번호 선택 kim")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim1, 0.3, "# 상세 입고 예약 차량 번호 선택 kim1")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim_ch2, 0.5, "# 상세 입고 예약 차량 번호 선택 ch2")

            elif driver_list[1] == 'cj_kim_driver':

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim_cj, 0.3, "# 상세 입고 예약 차량 번호 선택 kim")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim1_cj, 0.3, "# 상세 입고 예약 차량 번호 선택 kim1")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other_cj1, 0.3, "# 상세 입고 예약 차량 번호 선택 cj 대체1")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other_cj2, 0.3, "# 상세 입고 예약 차량 번호 선택 cj 대체2")

                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other_cj3, 0.3,"# 상세 입고 예약 차량 번호 선택 cj 대체3")
            else:
                samsung_w.find_image(source_url + xpath.reserve_truck_driver_other, 0.3, "# 상세 입고 예약 차량 번호 선택 other")

            logger.debug(
                f'fuc >>  detailed_reserve_complated |  driver name : {driver_list[1]}  |  driver_check : {driver_check} ')

            # samsung_w.find_image(source_url + xpath.reserve_truck_driver, 0, "# 상세 입고 예약 차량 번호 선택")

        # 상세 입고 예약 시간 선택
        mf.time.sleep(0.5)

        if reserve_time == 'a_1730':
            samsung_w.find_image(source_url + xpath.reserve_time_set_1730, 0, "# 상세 입고 예약 시간 선택")


        elif reserve_time == 'a_2100':
            samsung_w.find_image(source_url + xpath.reserve_time_set_2100, 0.3, "# 상세 입고 예약 시간 선택")

            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_1, 0.3, "# 상세 입고 예약 시간 선택")

            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_2, 0.3, "# 상세 입고 예약 시간 선택")

            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_young, 0.3, "# 상세 입고 예약 시간 선택")



        elif reserve_time == 'kimhae_2100':
            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_kimhae, 0.3, "# 상세 입고 예약 시간 선택-김해")

        elif reserve_time == 'jeju_1900':
            samsung_w.find_image(source_url + xpath.reserve_time_set_1900_jeju, 0.3, "# 상세 입고 예약 시간 선택-제주")

        elif reserve_time == 'jeju_1730':
            samsung_w.find_image(source_url + xpath.reserve_time_set_1730_jeju, 0.3, "# 상세 입고 예약 시간 선택-제주")

        elif reserve_time == 'young_2100':
            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_young, 0.3, "# 상세 입고 예약 시간 선택-용인")

            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_young2, 0.3, "# 상세 입고 예약 시간 선택-용인")

        elif reserve_time == 'young_1730':
            samsung_w.find_image(source_url + xpath.reserve_time_set_1730_young, 0.3, "# 상세 입고 예약 시간 선택-용인")

        elif reserve_time == 'gwang_2100':
            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_gwang, 0.3, "# 상세 입고 예약 시간 선택-광주")


        else:
            samsung_w.find_image(source_url + xpath.reserve_time_set_2100, 0.3, "# 상세 입고 예약 시간 선택")

            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_1, 0.3, "# 상세 입고 예약 시간 선택")

            samsung_w.find_image(source_url + xpath.reserve_time_set_2100_2, 0.3, "# 상세 입고 예약 시간 선택")
            mf.time.sleep(0.9)

        name = ff.log_input_format_tdoay()+ ".png"
        samsung_w.caputure_image(name)
        logger.warning(f" fuc >>  detailed_reserve_complated |  reserve time : - {reserve_time}")

        # 최종 입고예약 버튼
        samsung_w.clicked_button1(xpath.c4, 0.5, "# 최종 입고예약 버튼")
        # mf.time.sleep(0.5)

        # 최종 입고예약 확인 취소 버튼
        samsung_w.clicked_button1(xpath.c5, 0, "# 최종 입고예약 확인 취소 버튼")
        samsung_w.implic_time_sleep(5)

        # 최종 입고예약 다음창 넘어가는 버튼
        samsung_w.wait_button(xpath.c5)
        mf.time.sleep(2)
        #samsung_w.clicked_button2(xpath.c5, 2, "# 최종 입고예약 다음창 넘어가는 버튼0")

        ################################
        """
        try:
            # 최종 입고예약 다음창 넘어가는 버튼
            samsung_w.clicked_button2(xpath.c5, 0.3, "# 최종 입고예약 다음창 넘어가는 버튼2_0")
        except:
            samsung_w.clicked_button2(xpath.c6, 0.3, "# 최종 입고예약 다음창 넘어가는 버튼2_0")

        try:
            # 최종 입고예약 다음창 넘어가는 버튼
            samsung_w.clicked_button1(xpath.c5, 0.3, "# 최종 입고예약 다음창 넘어가는 버튼2_0")
        except:
            samsung_w.clicked_button2(xpath.c6, 0.3, "# 최종 입고예약 다음창 넘어가는 버튼2_0")
        logger.warning("최종 입고예약 다음창 넘어가는 버튼 오류")
        """

        logger.debug(
            f'fuc >>  detailed_reserve_complated :  # 상세 입고 예약 차량 번호 선택 > # 상세 입고 예약 시간 선택 >  # 최종 입고예약 버튼 > # 최종 입고예약 다음창 넘어가는 버튼')
        # mf.time.sleep(3)

    #################################################################################################################
    global Center_name
    global df_list
    global Client_name

    def again(total_count):
        try:

            reserve__stock()


        except:

            send_alert_email(str(total_count) + "count  재실행 확인중")
            df = mf.pd.DataFrame(df_list, columns=["입고 예약 날짜", "센터", "협력회사", "입고 예약 설정 시간", "입고예약", "미처리 예약", "현재 시각"])
            today = ff.log_input_format_tdoay()
            df.to_csv("./check/" + today + ".csv", encoding='euc-kr')

            logger.error(f'error point :  {error}')
            logger.error(f'now time : {ff.today_input_format_detail()} | {total_count}-  count   오류 발생으로 자동 재실행')
            total_count += 1
            again(total_count)

    while True:

        try:

            logger.info(f'{mf.datetime.now()} | ')

            schedule.run_pending()
            #schedule.every().day.at("17:01").do(reserve__stock)
            schedule.every().day.at(ff.sch_input_format()).do(reserve__stock)





        except Exception as error:
            send_alert_email("재실행 확인중")
            df = mf.pd.DataFrame(df_list, columns=["입고 예약 날짜","센터","협력회사","입고 예약 설정 시간","입고예약","미처리 예약","현재 시각"])
            today = ff.log_input_format_tdoay()
            df.to_csv("./check/" + today + ".csv", encoding='euc-kr')


            logger.error(f'error point :  {error}')
            logger.error(f'now time : {ff.today_input_format_detail()} | 오류 발생으로 자동 재실행')
            total_count = 2


            try:

                reserve__stock()



            except:

                send_alert_email(str(total_count)+"count  재실행 확인중")
                df = mf.pd.DataFrame(df_list, columns=["입고 예약 날짜", "센터", "협력회사", "입고 예약 설정 시간", "입고예약", "미처리 예약", "현재 시각"])
                today = ff.log_input_format_tdoay()
                df.to_csv("./check/" + today + ".csv", encoding='euc-kr')

                logger.error(f'error point :  {error}')
                logger.error(f'now time : {ff.today_input_format_detail()} | {total_count}-  count   오류 발생으로 자동 재실행')
                try:
                    reserve__stock()


                except:
                    total_count += 1
                    again(total_count)



        mf.time.sleep(1)


    pyautogui.moveTo(964, 125, 0.1)
    local = 1

    if ff.sch_hour_format() == 17 or ff.sch_hour_format() == 18:
        local = 2



    start = mf.time.time()
    logger.debug(f'{ff.sch_hour_format()} local time : {local}')

    chrome = mf.webdriver.Chrome(xpath.driver_url, options=options)
    # Chrome 창 생성
    samsung_w = sw.Samsung_W(chrome, url)
    # 로그인 > # 첫번째 팝업창 닫기  > # 첫번째 큰 여러개 팝업창 > # 발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행
    chrome_intro()

    # mouse location
    #Point(x=622, y=107)


    # btn_c  센터 선택하기
    ## 센터 박스 선택
    btn_c = xpath.btn_c

    first_check = 0

    try:
        samsung_w.clicked_button2(btn_c, 3, "센터 박스 선택하기")
        first_check = 1
        # logger.debug(f'fuc : "센터 박스 선택하기" >> | first_check :  {first_check} ')
    except:
        samsung_w.clicked_button2(btn_c, 3, "센터 박스 선택하기")
        first_check = 0

        # logger.error(f'fuc : "센터 박스 선택하기" >> | first_check :  {first_check} ')

    ##center_address
    center_address = '/html/body/sc-dropdown'
    li_element, center_list = samsung_w.get_tag_list(center_address, 'div', "센터 리스트 > 센터 선택")

    ## 제외 센터 설정 - center_김해, 왜관 제외 list  >>not
    execept_list = samsung_w.make_except_list([])
    mf.time.sleep(0.5)

    # 협력회사 박스 설정
    a = xpath.a
    d = xpath.d
    e = xpath.e
    date_select = xpath.date_select

    email_check = 0
    #len(li_element) + 1 - 2
    for count in range(local, len(li_element) + 1 - 2):
        # 센터명/ 날짜/ 기사/ 협력회사/ 입고예약 / 최종 예약 미처리

        if ff.sch_hour_format() == 17 or ff.sch_hour_format() == 18:
            if count == 6:
                continue

        logger.info(
            f'fuc : 1 STEP | 센터 : {center_list[count - 1]} | {True if not center_list[count - 1] in execept_list else False}')

        # 센터 부분 & driver_list return
        driver_list, resev_date = center_part(center_list, count, btn_c, date_select)
        driver_check = 0

        logger.info(
            f'fuc : 2 STEP | 센터 : {center_list[count - 1]} | driver list :{driver_list} | driver check : {driver_check}')

        # 협력회사 설정
        li_element_client, client_list, get_list = client_setting_part(d)

        CJ_food = client_list[8]
        GServe = client_list[7]

        logger.info(
            f'fuc : 3 STEP | 센터 : {center_list[count - 1]} | 협력회사 설정 {CJ_food} / {GServe}')

        for count_client in range(1, len(li_element_client) + 1):

            pyautogui.moveTo(964, 125)
            logger.debug(f'x =964, y =125')
            Client_name = ["","","","","","x",""]
            Client_name[0] = resev_date
            Client_name[1] = center_list[count - 1]
            Client_name[2] = client_list[count_client - 1]
            print(Client_name)
            check = 1
            # default 시간
            reserve_time = 'a_2100'
            logger.info(
                f'fuc : 4 STEP | 센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} |default time : {reserve_time} | ')

            # 협력 업체 조건 및 파트
            logger.info(f'start : {count_client}')
            #새롬 제외
            if count_client == 25:
                continue;

            reserve_time = client_part(client_list, count_client, reserve_time)
            logger.info(
                f'fuc : 5 STEP | 센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} | changed reserver time : {reserve_time} | ')

            Client_name[3] = reserve_time
            # 체크박스 체크 되어있으면 바로 조회 아니면 체크되지않으면 체크 하고 조회

            if samsung_w.check_checkbox(xpath.check_box1, "1") == 'true':
                pass
            else:
                samsung_w.click_checkbox(xpath.check_1, 0.5)

            if samsung_w.check_checkbox(xpath.check_box2, "1") == 'true':
                pass
            else:
                samsung_w.click_checkbox(xpath.check_2, 0.5)

            try:
                #samsung_w.wait_button(a)

                samsung_w.clicked_button2(a, 2.5, "조회 버튼 클릭 - 1차")

                # 공문 미확인 알림
                try:
                    samsung_w.clicked_button2(xpath.directly_deliv, 0.3, "# 공문 미확인 알림")
                    send_alert_email(f"{client_list[count_client - 1]} 공문 미확인 확인부탁드립니다.")
                except:
                    logger.debug(
                        f"센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} 공문 미확인 알림 없음")

            except:
                samsung_w.clicked_button1(a, 1, "조회 버튼 클릭 - 2차")

                # 공문 미확인 알림
                try:
                    samsung_w.clicked_button2(xpath.directly_deliv, 0.3, "# 공문 미확인 알림")
                    send_alert_email(f"{client_list[count_client - 1]} 공문 미확인 확인부탁드립니다.")
                except:
                    logger.debug(
                        f"센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} 공문 미확인 알림 없음")

            mf.time.sleep(1)
            value = samsung_w.get_value(xpath.incompleted_deal, 'span', "# 입고예약 미처리를 통해 다음 협력 회사로 검색할지 결정")
            ################
            Client_name[4] = value
            mf.time.sleep(1)
            nums = re.sub(r'[^0-9]','', value)

            if nums =="":
                nums ='0'
            if int(nums) != 0:
                check_box_list = samsung_w.init_checkbox_setting(xpath.check_11, xpath.check_22, 1,
                                                                 "inited the check box 1,2")

                check = 1
                for check_box_i in check_box_list:

                    if check == 1:
                        mf.time.sleep(0.5)
                        # 체크박스 선택 파트 및 입고장 설정
                        li_element_place, place_list = checkbox_part_input_place_setting(check_box_i)
                        logger.info(
                            f'fuc : 6 STEP | place_list : {place_list}')

                        for check_p in range(0, len(place_list)):
                            try:
                                if check == 1:
                                    logger.info(
                                        f'fuc : 7 STEP | 센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} | 입고장 number : {check_p}')

                                    # 입고장 요소 선택 >  # 조회 버튼 클릭

                                    # 입고장 요소 선택
                                    samsung_w.clicked_button2(e, 0, "입고장 박스 선택 ")

                                    count_place_name = '/html/body/sc-dropdown[3]/sc-listbox/div[' + str(
                                        place_list[check_p]) + ']'
                                    samsung_w.implic_time_sleep(1)
                                    samsung_w.clicked_button2(count_place_name, 0,
                                                              "입고장 " + place_list[check_p] + " 요소 선택")

                                    samsung_w.clicked_button2(xpath.f, 0, "# 배송 방식 설정1")
                                    li_deliver, deliver_list = samsung_w.get_tag_list(xpath.deliver_list, 'div',
                                                                                      "# 배송 방식 리스트")

                                    for idx, d_way in enumerate(deliver_list[:-1]):

                                        logger.info(f' idx : {idx}  | way : {d_way} ')

                                        samsung_w.clicked_button2(xpath.f, 0.3, "# 배송 방식 설정")
                                        deli_sc = "/html/body/sc-dropdown[4]/sc-listbox/div[" + str(idx + 1) + "]"
                                        samsung_w.clicked_button1(deli_sc, 0.3, "# 배송 방식 요소 <" + str(idx + 1))

                                        if d_way == '직송':
                                            # 조회 버튼 클릭
                                            samsung_w.clicked_button2(a, 1, "조회 버튼 클릭")


                                            # 공문 미확인 알림
                                            try:
                                                samsung_w.clicked_button2(xpath.directly_deliv, 0.3,
                                                                          "# 직송 마지막 예약버튼")


                                            except:
                                                logger.debug(
                                                    f"센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} |  공문 미확인 알림 없음")

                                            mf.time.sleep(0.3)
                                            value = samsung_w.get_value(xpath.incompleted_deal, 'span',
                                                                        "# 입고예약 미처리를 통해 다음 협력 회사로 검색할지 결정 1")

                                            Client_name[5] = value
                                            nums = re.sub(r'[^0-9]', '', value)
                                            if nums == "":
                                                nums = '0'
                                            if int(nums) != 0:

                                                logger.debug(
                                                    f' 센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} |  fuc >>  input_place_part_search_click :  # 입고장 요소 선택 >  # 조회 버튼 클릭 ')

                                                reserve_canvase_check_first_button()
                                                try:
                                                    samsung_w.clicked_button2(xpath.directly_deliv, 0.5,
                                                                              "# 직송 마지막 예약버튼")
                                                except:
                                                    logger.debug(
                                                        f"센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} | 공문 미확인 알림 없음")

                                            else:
                                                check = 0


                                        else:
                                            # 조회 버튼 클릭
                                            samsung_w.clicked_button2(a, 1, "조회 버튼 클릭")

                                            # 공문 미확인 알림
                                            try:
                                                samsung_w.clicked_button2(xpath.directly_deliv, 0.3,
                                                                          "# 직송 마지막 예약버튼")
                                            except:
                                                logger.warning("직송 입고예약없음")

                                            mf.time.sleep(0.3)
                                            value = samsung_w.get_value(xpath.incompleted_deal, 'span',
                                                                        "# 입고예약 미처리를 통해 다음 협력 회사로 검색할지 결정 2")
                                            Client_name[5] = value
                                            nums = re.sub(r'[^0-9]', '', value)
                                            if nums == "":
                                                nums = '0'
                                            if int(nums) != 0 and check == 1:

                                                logger.debug(
                                                    f'센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} | fuc >>  input_place_part_search_click :  # 입고장 요소 선택 >  # 조회 버튼 클릭 ')

                                                # 크롬창 최대 크기
                                                # samsung_w.max_size_chrome_windows()
                                                # 반드시 2s 건들이지 말것
                                                # mf.time.sleep(2)
                                                ## 급 변경

                                                logger.debug(
                                                    f'{reserve_time}{center_list[1:4]} | {center_list[4]} |{center_list[5]}')
                                                #if center_list[count - 1] == CJ_food:
                                                if client_list[count_client - 1] == CJ_food:
                                                    driver_list = ['cj_other_driver', 'cj_kim_driver']

                                                if center_list[count - 1] in center_list[1:3]:
                                                    reserve_time = 'kimhae_2100'

                                                elif center_list[count - 1] in center_list[
                                                    4] and reserve_time == 'a_2100':
                                                    reserve_time = 'jeju_1900'
                                                elif center_list[count - 1] in center_list[
                                                    4] and reserve_time == 'a_1730':
                                                    reserve_time = 'jeju_1730'


                                                elif center_list[count - 1] in center_list[
                                                    5] and reserve_time == 'a_2100':
                                                    reserve_time = 'young_2100'
                                                elif center_list[count - 1] in center_list[
                                                    5] and reserve_time == 'a_1730':
                                                    reserve_time = 'young_1730'
                                                elif center_list[count - 1] == center_list[3]:
                                                    reserve_time = 'gwang_2100'

                                                # 미리 체크된 이미지 찾기 > # 입고 예약 캠버스 버튼 >  #상세 항목 선택을 위한 입고예약 버튼 > # 입고예약 캠버스 버튼 누룬 후 알림 확인 버튼
                                                state = reserve_canvase_check_first_button()

                                                # 상세 입고 예약창
                                                if state == False:
                                                    # 상세 입고 예약 차량 번호 선택 > # 상세 입고 예약 시간 선택 >  # 최종 입고예약 버튼 > # 최종 입고예약 다음창 넘어가는 버튼
                                                    detailed_reserve_complated(driver_check, driver_list,
                                                                               reserve_time, client_list[count_client - 1], center_list[count - 1])

                                                    # driver_check 카운트 +1
                                                    driver_check = driver_check + 1
                                                    logger.debug(
                                                        f' 센터 : {center_list[count - 1]} | 협력회사 상태 : {client_list[count_client - 1]} |   check update : {driver_check}')
                                                    # samsung_w.clicked_button2(a, 0.5, "조회 버튼 클릭")
                                                    #mf.time.sleep(0.5)
                                                    samsung_w.implic_time_sleep(3)
                                                    value = samsung_w.get_value(xpath.incompleted_deal, 'span',
                                                                                "# 입고예약 미처리를 통해 다음 협력 회사로 검색할지 3")

                                                    print("value :",value)
                                                    nums = re.sub(r'[^0-9]', '', value)
                                                    if nums == "":
                                                        nums = '0'
                                                    if int(nums) == 0:
                                                        Client_name[5] = value
                                                        check = 0

                                                mf.time.sleep(0.3)



                                            else:
                                                break
                                else:
                                    logger.warning(f'check1 : {check}')

                            except ElementNotInteractableException as InterruptedErrors:

                                logger.error(f'Error point : {InterruptedErrors}')
                                reserve__stock()

                    else:
                        logger.warning(f'check2 : {check}')
                    # 체크박스  해제
                    samsung_w.css_clicked_button1(check_box_i, 0, str(check_box_i[6:8]) + "  체크박스 해제")

                # 체크박스 체크 되어있으면 바로 조회 아니면 체크되지않으면 체크 하고 조회

                if samsung_w.check_checkbox(xpath.check_box1, "2") == 'true':
                    pass
                else:
                    samsung_w.click_checkbox(xpath.check_1, 0.2)

                if samsung_w.check_checkbox(xpath.check_box2, "2") == 'true':
                    pass
                else:
                    samsung_w.click_checkbox(xpath.check_2, 0.2)


            else:
                pass

            now = ff.log_input_format_tdoay()
            Client_name[6]= now
            logger.debug(f'{Client_name}')
            df_list.append(Client_name)
    #센터명/ 날짜/ 기사/ 협력회사/ 입고예약 / 최종 예약 미처리
    df = mf.pd.DataFrame(df_list, columns=["입고 예약 날짜","센터","협력회사","입고 예약 설정 시간","입고예약","미처리 예약","현재 시각"])
    today = ff.log_input_format_tdoay()
    df.to_csv("./check/" + today + ".csv",encoding='euc-kr')
    df_list= []

    result_list = str(datetime.timedelta(seconds=(mf.time.time() - start))).split(".")

    logger.error(f'now time : {ff.today_input_format_detail()} | taken time : {result_list[0]}')

    global test_complete
    test_complete= False
    samsung_w.finished_crawling()
    send_alert_email2("Finished 입고예약!!! ")

    mf.time.sleep(15)
    path = "/Check"
    file_list = os.listdir(path)
    max = 0
    max_file =""
    #print("file_list: {}".format(file_list))
    for fir in file_list:
        mkdir_time = os.path.getmtime(path + "/" + fir)
        if mkdir_time > max:
            max = mkdir_time
            max_file = path + "/" + fir

    logger.debug(f' save file name : {max_file}')
    non_df = mf.pd.read_csv(max_file, encoding='euc-kr')
    count_data = non_df["미처리 예약"].values.tolist()
    # 하나라도 미처리 ""가 아닌 다른 값이 있을 때 재 실행
    non_df = mf.pd.read_csv(max_file, encoding='euc-kr')
    count_data = non_df["입고예약"].values.tolist()
    print(count_data)
    # 하나라도 미처리 ""가 아닌 다른 값이 있을 때 재 실행
    for idx, c in enumerate(count_data):
        count_num = re.sub(r'[^0-9]', '',c)
        if int(count_num) != 0 :

            print("check", int(c[0])," / 비교 : ",str(0), non_df["미처리 예약"][idx])
            if non_df["미처리 예약"][idx] == "" or non_df["미처리 예약"][idx] == 'x' or non_df["미처리 예약"][idx] != '0 건' :
                logger.error("미처리 예약확인으로 재실행")
                Client_name =[]
                reserve__stock()


            else:
                pass









reserve__stock()
"""
# 11:00입문증 출력 >>>15:30~~~
#schedule.every().day.at("03:45").do(reserve__stock)
schedule.every().day.at("11:00").do(reserve__stock)
schedule.every().day.at("15:30").do(reserve__stock)
schedule.every().day.at("18:12").do(reserve__stock)
schedule.every().day.at("17:01").do(reserve__stock)
#17:00 / 17:30
schedule.every().day.at("17:30").do(reserve__stock)
schedule.every().day.at("17:55").do(reserve__stock)
schedule.every().day.at("19:01").do(reserve__stock)
schedule.every().day.at("20:30").do(reserve__stock)

schedule.every().day.at(ff.sch_input_format()).do(reserve__stock)
# schedule.every().day.at("14:41").do(test_func)
"""


