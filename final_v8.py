#-*- coding: utf-8 -*-
import os
import subprocess
import sys
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import send__email as s_email

warnings.filterwarnings('ignore')
import log_package as lp
import logging
import module_file as mf
import func_file as ff
import xpath_data as xpath
import sel_option as s_option
import samsung_well as sw

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

# 날짜
today_date = ff.today_input_format()
tomorrow = ff.other_day_input_format(2)


def send_alert_email(string):
    title_string = "입고예약 오류"
    s_email.send_email(title_string, string)



def chrome_intro():
    samsung_w.run()
    # 로그인
    samsung_w.login()
    # 첫번째 팝업창 닫기
    samsung_w.closed_alert_window(xpath.btn, 0.5, "첫번째 팝업창 닫기")
    # 첫번째 큰 여러개 팝업창 닫기
    samsung_w.closed_big_alert_window(xpath.first_new_box)

    # 발주 납품 관리
    samsung_w.clicked_button1(xpath.report_manage, 0.2, "발주 납품 관리")
    # 발주 납품 관리 >  발주 관리
    samsung_w.clicked_button1(xpath.btn_manage, 0.2, "발주 납품 관리 >  발주 관리")
    # 발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행
    samsung_w.clicked_button1(xpath.box_manage, 0.2, "발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행")
    logger.debug(
        f'fuc >>  chrome_intro :  # 로그인 > # 첫번째 팝업창 닫기  > # 첫번째 큰 여러개 팝업창 > # 발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행')


def center_part(center_list, count, btn_c, date_select):
    list_element_name = '/html/body/sc-dropdown/sc-listbox/div[' + str(count) + ']'
    # 해당 되는 물류센터 요소 선택
    samsung_w.clicked_button2(btn_c, 0.5, "센터 박스 선택하기")
    samsung_w.clicked_button1(list_element_name, 0, "해당 되는 물류센터 요소 선택")

    # 특정 센터 날짜 변경
    if center_list[count - 1] == center_list[4] or center_list[count - 1] == center_list[1]:
        samsung_w.chanage_datetime(date_select, 0.2, tomorrow)
        logger.debug(
            f'fuc : 특정 센터 날짜 변경 >> {tomorrow} | 센터 : {center_list[count - 1]} | 기준 : {center_list[4]}')

    else:
        logger.debug(
            f'fuc : 나머지센터 날짜 유지 >> {today_date} | 센터 : {center_list[count - 1]} | 기준 : {center_list[4]}')

    logger.warning(
        f'fuc >>  center_part :  # 해당 되는 물류센터 요소 선택 > # 특정 센터 날짜 변경 ')

    # driver list setting
    driver_list = []

    if center_list[count - 1] == center_list[0]:
        driver_list = [ 'jeong_driver','kim_driver' ]

    elif center_list[count - 1] == center_list[5]:
        driver_list = ['jeong_driver', 'song_driver']

    logger.debug(
        f'fuc : 나머지센터 날짜 유지 >> {today_date} | 센터 : {center_list[count - 1]} | 기준 : {center_list[4]} driver list : {driver_list}')

    return driver_list


def client_setting_part(d):
    # "협력회사 리스트 박스 선택"
    samsung_w.clicked_button2(d, 0, "협력회사 리스트 박스 선택")
    list_box = xpath.list_box

    # 협력회사 리스트 가져오기
    li_element_client, client_list = samsung_w.get_tag_list(list_box, 'div', "협력회사 리스트 > 협력회사 선택")
    get_list = ff.get_list_value(li_element)
    CJ_food = client_list[8]
    logger.debug(
        f'fuc >>  client_setting_part :  # "협력회사 리스트 박스 선택" >  # 협력회사 리스트 가져오기 ')

    return li_element_client, client_list, get_list



def client_part(client_list, count_client, reserve_time):

    time = reserve_time
    if client_list[count_client - 1] != CJ_food:
        logger.info(
            f'fuc : >> 협력회사 :  {client_list[count_client - 1]} | 기준 : {CJ_food}')

        samsung_w.clicked_button2(d, 0, "협력회사 리스트 박스 선택")
        # 협력회사 중 요소 선택
        count_client_name = '/html/body/sc-dropdown[2]/sc-listbox/div[' + str(count_client) + ']'
        samsung_w.clicked_button2(count_client_name, 0.3, "협력회사 중 요소 선택")

        time = 'a_1730'


    else:
        logger.warning(
            f'fuc : >> 협력회사 :  {client_list[count_client - 1]} | 기준 : {CJ_food}')
        time = 'a_2100'

    logger.debug(
        f'fuc >>  client_part :  # 협력업체 조건문 >  # 협력회사 중 요소 선택 ')

    return time


def checkbox_part_input_place_setting(check_box_i):
    logger.info(
        f'fuc : for3 문 >> | 체크박스 No. {check_box_i[6:8]} 번째 ')

    # 체크박스 선택
    samsung_w.css_clicked_button1(check_box_i, 0, str(check_box_i[6:8]) + "  체크박스 선택")

    # 입고장
    samsung_w.clicked_button2(e, 0, "입고장 박스 선택 > 입고장 리스트")
    li_element_place, place_list = samsung_w.get_tag_list(xpath.input_center, 'div', "입고장 리스트")

    logger.debug(
        f'fuc >>  checkbox_part_input_place_setting :  # 체크박스 선택 >  # 입고장 ')
    return li_element_place, place_list


def input_place_part_search_click(e, place_list, a):
    # 입고장 요소 선택
    samsung_w.clicked_button2(e, 0, "입고장 박스 선택 ")

    count_place_name = '/html/body/sc-dropdown[3]/sc-listbox/div[' + str(place_list[check_p]) + ']'
    samsung_w.clicked_button2(count_place_name, 0, "입고장 " + place_list[check_p] + " 요소 선택")

    # 조회 버튼 클릭
    samsung_w.clicked_button2(a, 3, "조회 버튼 클릭")
    logger.debug(
        f'fuc >>  input_place_part_search_click :  # 입고장 요소 선택 >  # 조회 버튼 클릭 ')


def reserve_canvase_check_first_button():
    # 입고예약 체크 박스가 미리 체크 되어있을때
    # 미리 체크된 이미지 찾기
    #mf.pyautogui.locateOnScreen(source_url + xpath.checked_image)
    samsung_w.find_image(source_url + xpath.checked_image, 1, xpath.checked_image)
    # mf.pyautogui.click(img_capture1_1)

    # 입고 예약 캠버스 버튼

    samsung_w.find_image(source_url + xpath.input_reserve_image, 1, xpath.input_reserve_image)

    #상세 항목 선택을 위한 입고예약 버튼
    samsung_w.clicked_button2(xpath.c2, 1, "상세 항목 선택을 위한 입고예약 버튼")

    # 마우스 위치 임의로 설정
    mf.pyautogui.moveTo(50, 50)
    mf.time.sleep(0.5)

    # 입고예약 캠버스 버튼 누룬 후 알림 확인 버튼
    state = True
    state = samsung_w.clicked_button3(xpath.alert_exc, 1, "입고예약 캠버스 버튼 누룬 후 알림 확인 버튼", state)
    logger.debug(
        f'fuc >>  reserve_canvase_check_first_button :  # 미리 체크된 이미지 찾기 > # 입고 예약 캠버스 버튼 >  #상세 항목 선택을 위한 입고예약 버튼 > # 입고예약 캠버스 버튼 누룬 후 알림 확인 버튼 | state : {state}')

    return state



def detailed_reserve_complated(driver_check, driver_list, reserve_time):
    # 상세 입고 예약 차량 번호 선택
    time.sleep(0.5)

    # 운전기사 선택
    if driver_check == 0 :

        if driver_list[0] == 'jeong_driver':
            samsung_w.find_image(source_url + xpath.reserve_truck_driver_jeong, 0.5,  "# 상세 입고 예약 차량 번호 선택 jeong")
            samsung_w.find_image(source_url + xpath.reserve_truck_driver_jeong1, 0.5, "# 상세 입고 예약 차량 번호 선택 jeong1")
            samsung_w.find_image(source_url + xpath.reserve_truck_driver_jeong2, 0.5, "# 상세 입고 예약 차량 번호 선택 jeong2")

        elif driver_list[0] != 'jeong_driver':
            samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim, 1, "# 상세 입고 예약 차량 번호 선택")

        else:
            samsung_w.find_image(source_url + xpath.reserve_truck_driver_other, 0.5, "# 상세 입고 예약 차량 번호 선택 other")


        logger.debug(
            f'fuc >>  detailed_reserve_complated |  driver name : {driver_list[0]}  |  driver_check : {driver_check} ')

    else:
        if driver_list[1] == 'song_driver':
            samsung_w.find_image(source_url + xpath.reserve_truck_driver_song, 0.5,  "# 상세 입고 예약 차량 번호 선택")
        elif driver_list[1] == 'kim_driver':


            samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim, 0.5, "# 상세 입고 예약 차량 번호 선택 kim")

            #samsung_w.find_image(source_url + xpath.reserve_truck_driver_kim1, 0.5, "# 상세 입고 예약 차량 번호 선택 kim1")
        else:
            samsung_w.find_image(source_url + xpath.reserve_truck_driver_other, 0.5, "# 상세 입고 예약 차량 번호 선택 other")


        logger.debug(f'fuc >>  detailed_reserve_complated |  driver name : {driver_list[1]}  |  driver_check : {driver_check} ')


        #samsung_w.find_image(source_url + xpath.reserve_truck_driver, 0, "# 상세 입고 예약 차량 번호 선택")

    # 상세 입고 예약 시간 선택
    if reserve_time =='a_1730':
        samsung_w.find_image(source_url + xpath.reserve_time_set_1730, 0, "# 상세 입고 예약 시간 선택")
        mf.time.sleep(0.5)
    elif reserve_time == 'a_2100':
        samsung_w.find_image(source_url + xpath.reserve_time_set_2100, 0, "# 상세 입고 예약 시간 선택")
        mf.time.sleep(0.5)
    else:
        pass

    logger.warning(f" fuc >>  detailed_reserve_complated |  reserve time : - {reserve_time}")

    # 최종 입고예약 버튼
    samsung_w.clicked_button1(xpath.c4, 0.5, "# 최종 입고예약 버튼")
    mf.time.sleep(0.5)

    # 최종 입고예약 확인 취소 버튼
    samsung_w.clicked_button1(xpath.c5, 0.5, "# 최종 입고예약 확인 취소 버튼")
    mf.time.sleep(0.5)

    # 최종 입고예약 다음창 넘어가는 버튼
    samsung_w.clicked_button2(xpath.c5, 0.5, "# 최종 입고예약 다음창 넘어가는 버튼")

    logger.debug(
        f'fuc >>  detailed_reserve_complated :  # 상세 입고 예약 차량 번호 선택 > # 상세 입고 예약 시간 선택 >  # 최종 입고예약 버튼 > # 최종 입고예약 다음창 넘어가는 버튼')
    mf.time.sleep(3)




#################################################################################################################

if __name__ =="__main__":
    chrome = mf.webdriver.Chrome(xpath.driver_url, options=options)
    # Chrome 창 생성
    samsung_w = sw.Samsung_W(chrome, url)
    # 로그인 > # 첫번째 팝업창 닫기  > # 첫번째 큰 여러개 팝업창 > # 발주 납품 관리 >  발주 관리 > BOX단위 출고 라벨 발행
    chrome_intro()

    # btn_c  센터 선택하기
    ## 센터 박스 선택
    btn_c = xpath.btn_c

    first_check = 0
    while(first_check== 0):
        try:
            samsung_w.clicked_button2(btn_c, 1, "센터 박스 선택하기")
            first_check = 1
            logger.debug(f'fuc : "센터 박스 선택하기" >> | first_check :  {first_check} ')
        except:

            first_check = 0
            logger.error(f'fuc : "센터 박스 선택하기" >> | first_check :  {first_check} ')

    mf.time.sleep(1)

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
    for count in range(1, len(li_element) + 1):

        try:
            logger.info(
                f'fuc : for1 문 >> | 센터 : {center_list[count - 1]} | {True if not center_list[count - 1] in execept_list else False}')
            if not center_list[count - 1] in execept_list:

                # 센터 부분 & driver_list return
                driver_list = center_part(center_list, count, btn_c, date_select)

                #
                driver_check = 0

                # 협력회사 설정
                li_element_client, client_list, get_list = client_setting_part(d)

                CJ_food = client_list[8]

                for count_client in range(1, len(li_element_client) + 1):

                    reserve_time = 'a_0000'

                    try:
                        logger.info(
                            f'fuc : for2 문 >> | 협력회사 : {client_list[count_client - 1]} | {True if client_list[count_client - 1] != {CJ_food} else False}')

                        # 협력 업체 조건 및 파트
                        reserve_time = client_part(client_list, count_client , reserve_time)

                        #  입고예약 미처리 검색으로  체크박스 확인
                        try:
                            samsung_w.clicked_button3(xpath.alert_exc, 0.5, "입고예약 캠버스 버튼 누룬 후 알림 확인 버튼 1", state)
                            logger.error("체크 박스 미체크 상황 1")
                            samsung_w.init_checkbox_setting(xpath.check_11, xpath.check_22, 1,
                                                            "inited the check box 1,2")

                        except:
                            logger.error("이미 체크 박스 문제없음 1")

                        samsung_w.clicked_button2(a, 3, "조회 버튼 클릭")
                        # 입고예약 미처리를 통해 다음 협력 회사로 검색할지 결정
                        mf.time.sleep(1)
                        value = samsung_w.get_value(xpath.incompleted_deal, 'span', "# 입고예약 미처리를 통해 다음 협력 회사로 검색할지 결정")
                        mf.time.sleep(0.5)

                        if int(value[0]) !=0:
                            check_box_list = samsung_w.init_checkbox_setting(xpath.check_11, xpath.check_22, 1,
                                                                             "inited the check box 1,2")

                            try:
                                samsung_w.clicked_button3(xpath.alert_exc, 1, "입고예약 캠버스 버튼 누룬 후 알림 확인 버튼 2", state)
                                logger.error("체크 박스 미체크 상황 2")
                                samsung_w.init_checkbox_setting(xpath.check_11, xpath.check_22, 1,
                                                                "inited the check box 1,2")

                            except:
                                logger.error("이미 체크 박스 문제없음 2")



                            for check_box_i in check_box_list:
                                #check_box_list = samsung_w.init_checkbox_setting(xpath.check_11, xpath.check_22, 1,"inited the check box 1,2")
                                try:
                                    # 체크박스 선택 파트 및 입고장 설정
                                    li_element_place, place_list = checkbox_part_input_place_setting(check_box_i)

                                    for check_p in range(0, len(place_list)):
                                        try:



                                            logger.info(
                                                f'fuc : for4 문 >> | 입고장 : {place_list[check_p]} ')

                                            # 입고장 요소 선택 >  # 조회 버튼 클릭
                                            #input_place_part_search_click(e, place_list, a)

                                            # 입고장 요소 선택
                                            samsung_w.clicked_button2(e, 0, "입고장 박스 선택 ")

                                            count_place_name = '/html/body/sc-dropdown[3]/sc-listbox/div[' + str(
                                                place_list[check_p]) + ']'
                                            samsung_w.clicked_button2(count_place_name, 0,
                                                                      "입고장 " + place_list[check_p] + " 요소 선택")

                                            samsung_w.clicked_button2(xpath.f, 0, "# 배송 방식 설정1")
                                            li_deliver, deliver_list = samsung_w.get_tag_list(xpath.deliver_list, 'div', "# 배송 방식 리스트")

                                            for idx, d_way in enumerate(deliver_list[:-1]):
                                                logger.info(f' idx : {idx}  | way : {d_way} ')

                                                samsung_w.clicked_button2(xpath.f, 0.3, "# 배송 방식 설정")
                                                deli_sc = "/html/body/sc-dropdown[4]/sc-listbox/div[" + str(idx+1) + "]"
                                                samsung_w.clicked_button1(deli_sc, 0.3, "# 배송 방식 요소 <" + str(idx+1))


                                                if d_way == '직송':
                                                    # 조회 버튼 클릭
                                                    samsung_w.clicked_button2(a, 2, "조회 버튼 클릭")
                                                    logger.debug(
                                                        f'fuc >>  input_place_part_search_click :  # 입고장 요소 선택 >  # 조회 버튼 클릭 ')

                                                    # 크롬창 최대 크기
                                                    samsung_w.max_size_chrome_windows()
                                                    # 반드시 2s 건들이지 말것
                                                    mf.time.sleep(2)
                                                    reserve_canvase_check_first_button()
                                                    try :
                                                        samsung_w.clicked_button2(xpath.directly_deliv, 0.5, "# 직송 마지막 예약버튼")
                                                    except:
                                                        logger.warning("직송 입고예약없음")


                                                else:
                                                    # 조회 버튼 클릭
                                                    samsung_w.clicked_button2(a, 2, "조회 버튼 클릭")
                                                    logger.debug(
                                                        f'fuc >>  input_place_part_search_click :  # 입고장 요소 선택 >  # 조회 버튼 클릭 ')


                                                    # 크롬창 최대 크기
                                                    samsung_w.max_size_chrome_windows()
                                                    # 반드시 2s 건들이지 말것
                                                    mf.time.sleep(2)

                                                    # 미리 체크된 이미지 찾기 > # 입고 예약 캠버스 버튼 >  #상세 항목 선택을 위한 입고예약 버튼 > # 입고예약 캠버스 버튼 누룬 후 알림 확인 버튼
                                                    state = reserve_canvase_check_first_button()

                                                    # 상세 입고 예약창
                                                    if state == False:
                                                        # 상세 입고 예약 차량 번호 선택 > # 상세 입고 예약 시간 선택 >  # 최종 입고예약 버튼 > # 최종 입고예약 다음창 넘어가는 버튼
                                                        detailed_reserve_complated(driver_check, driver_list ,reserve_time)

                                                        # driver_check 카운트 +1
                                                        driver_check = driver_check+ 1


                                        except:
                                            if email_check == 0 :
                                                email_check = 1
                                            log_text = f'fuc : for4 문 >> | 입고장 : {place_list[check_p]} '
                                            logger.error(
                                                log_text)
                                            send_alert_email(log_text)

                                    #check box recheck = unchecked state
                                    # 체크박스 선택
                                    samsung_w.css_clicked_button1(check_box_i, 0, str(check_box_i[6:8]) + "unchecked state")

                                except:
                                    log_text = f'fuc : for3 문 >> | 체크박스 No. {check_box_i[6:8]} 번째 '
                                    logger.error(
                                        f'fuc : for3 문 >> | 체크박스 No. {check_box_i[6:8]} 번째 ')

                                    if email_check == 0:
                                        send_alert_email(log_text)
                                        email_check = 1
                                    else:
                                        pass


                        else:
                            log_text = f'fuc : for2 문 >> |  입고예약 미처리를 통해 건너뜀 :{value} | 협력 회사 : {client_list[count_client - 1]} '
                            logger.error(
                                f'fuc : for2 문 >> |  입고예약 미처리를 통해 건너뜀 :{value} | 협력 회사 : {client_list[count_client - 1]} ')

                            if email_check == 0:
                                send_alert_email(log_text)
                                email_check = 1
                            else:
                                pass


                    except:
                        log_text = f'fuc : for2 문 >> | 협력회사 {client_list[count_client - 1]}'
                        logger.error(
                            f'fuc : for2 문 >> | 협력회사 {client_list[count_client - 1]}')

                        if email_check == 0:
                            send_alert_email(log_text)
                            email_check = 1
                        else:
                            pass

        except:
            log_text = f'fuc : for1 문 >> | 센터 '
            logger.error(
                f'fuc : for1 문 >> | 센터 ')

            if email_check == 0:
                send_alert_email(log_text)
                email_check = 1
            else:
                pass


    # 크롤링 끝
    samsung_w.finished_crawling()
