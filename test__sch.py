import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from multiprocessing import Process, Queue, freeze_support
import multiprocessing as mp
import datetime
import time
import os
from selenium import webdriver
from PyQt5 import uic

import new_cr_1_test as cr1

import new_cr_3_test as cr3
import new_cr_4_test as cr4
import new_cr_5_test as cr5
import new_cr_6_test as cr6
import new_cr_7_test as cr7

import new_cr_9_test as cr9
import new_cr_10_test as cr10
import new_cr_12_test as cr12
import new_cr_13_test as cr13
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import schedule


###################################################################################################
def producer(q):
    proc = mp.current_process()
    print(proc.name)

    while True:
        now = datetime.datetime.now()
        data = str(now)
        q.put(data)
        time.sleep(1)

def producer2(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")

    schedule.every().day.at(update_time).do(producer3)

    while True:
        schedule.run_pending()
        time.sleep(1)

def producer2_0(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer0)
    while True:
        schedule.run_pending()
        time.sleep(1)


def producer2_1(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer3)
    while True:
        schedule.run_pending()
        time.sleep(1)


def producer2_4(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    print("update time :",update_time)
    schedule.every().day.at(update_time).do(producer4)
    while True:
        schedule.run_pending()
        time.sleep(1)

def producer2_5(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer5)
    while True:
        schedule.run_pending()
        time.sleep(1)

def producer2_6(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer6)
    while True:
        schedule.run_pending()
        time.sleep(1)

def producer2_7(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer7)
    while True:
        schedule.run_pending()
        time.sleep(1)


def producer2_9(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer9)
    while True:
        schedule.run_pending()
        time.sleep(1)


def producer2_10(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer10)
    while True:
        schedule.run_pending()
        time.sleep(1)


def producer2_12(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer12)
    while True:
        schedule.run_pending()
        time.sleep(1)


def producer2_13(q, update_time):
    proc = mp.current_process()
    print(proc.name)
    print("here")
    schedule.every().day.at(update_time).do(producer13)
    while True:
        schedule.run_pending()
        time.sleep(1)
###################################################################################################
def producer0():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "거래처별_입고현황"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }
    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr1.cr_1(driver,url,folder).run()
    print("4")



def producer1():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "구매_입고현황(누계)"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr1.cr_1(driver,url,folder).run()
    print("4")


def producer3():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "거래처별_주문상세내역_조회"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr3.cr_0(driver,url,folder).run()
    print("4")



def producer4():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "납품별센터별_출고실적"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr4.cr_4(driver,url,folder).run()
    print("4")

def producer5():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "매출실적(거래처__상품별)"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr5.cr_5(driver,url,folder).run()
    print("4")

def producer6():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "유통기한별_재고현황"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr6.cr_6(driver,url,folder).run()
    print("4")


def producer7():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "제품수불부(본사_센터)"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr7.cr_7(driver,url,folder).run()
    print("4")



def producer9():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "기초정보_거래처관리"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr9.cr_9(driver,url,folder).run()
    print("4")



def producer10():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "기초정보_납품처별_납품센터관리"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr10.cr_10(driver,url,folder).run()
    print("4")



def producer12():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder =  "기초정보_거래처_품목등록"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr12.cr_12(driver,url,folder).run()
    print("4")



def producer13():
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder =  "기초정보_품목정보관리"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    cr13.cr_13(driver,url,folder).run()
    print("4")
###################################################################################################
class Consumer(QThread):
    poped = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            if not self.q.empty():
                data = q.get()
                self.poped.emit(data)


class Consumer0(QThread):
    poped0 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped0.emit(data1)


class Consumer00(QThread):
    poped00 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped00.emit(data1)


class Consumer1(QThread):
    poped1 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped1.emit(data1)


class Consumer2(QThread):
    poped2 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped2.emit(data1)


class Consumer3(QThread):
    poped3 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped3.emit(data1)

class Consumer4(QThread):
    poped4 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped4.emit(data1)


class Consumer5(QThread):
    poped5 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped5.emit(data1)


class Consumer6(QThread):
    poped6 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped6.emit(data1)


class Consumer8(QThread):
    poped8 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped8.emit(data1)


class Consumer9(QThread):
    poped9 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped9.emit(data1)


class Consumer11(QThread):
    poped11 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped11.emit(data1)


class Consumer12(QThread):
    poped12 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped12.emit(data1)
###################################################################################################
class MyWindow(QMainWindow):
    def __init__(self, q,qq,qqq,qqqq,qqqqq,a,aa,b,bb,bbb,bbbb,c,cc):
        super().__init__()

        update_time = "mm:ss"

        self.setGeometry(200, 200, 300, 200)

        # thread for data consumer
        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.print_data)
        self.consumer.start()

        self.consumer0 = Consumer0(qq)
        self.consumer0.poped0.connect(self.print_data1)
        self.consumer0.start()


        self.consumer2 = Consumer2(qqq)
        self.consumer2.poped2.connect(self.print_data1)
        self.consumer2.start()

        self.consumer3 = Consumer3(qqqq)
        self.consumer3.poped3.connect(self.print_data1)
        self.consumer3.start()

        self.consumer4 = Consumer4(qqqqq)
        self.consumer4.poped4.connect(self.print_data1)
        self.consumer4.start()

        self.consumer5 = Consumer5(a)
        self.consumer5.poped5.connect(self.print_data1)
        self.consumer5.start()

        self.consumer6 = Consumer6(aa)
        self.consumer6.poped6.connect(self.print_data1)
        self.consumer6.start()

        self.consumer8 = Consumer8(b)
        self.consumer8.poped8.connect(self.print_data1)
        self.consumer8.start()

        self.consumer9 = Consumer9(bb)
        self.consumer9.poped9.connect(self.print_data1)
        self.consumer9.start()

        self.consumer11 = Consumer11(bbb)
        self.consumer11.poped11.connect(self.print_data1)
        self.consumer11.start()

        self.consumer12 = Consumer12(bbbb)
        self.consumer12.poped12.connect(self.print_data1)
        self.consumer12.start()

        self.consumer1 = Consumer1(c)
        self.consumer1.poped1.connect(self.print_data1)
        self.consumer1.start()

        self.consumer00 = Consumer00(cc)
        self.consumer00.poped00.connect(self.print_data1)
        self.consumer00.start()


        self.line_edit = QLineEdit(self)
        self.line_edit.move(20,60)


        self.text_label = QLabel(self)
        self.text_label.move(150,60)
        self.text_label.setText(update_time)

        self.button = QPushButton(self)
        self.button.move(20,100)
        self.button.setText('Set Time')
        self.button.clicked.connect(self.button_event)


        btn1  = QPushButton("button",self)
        btn1.move(20,20)
        btn1.clicked.connect(self.button_clicked1)

    def button_event(self):
        text = self.line_edit.text()
        self.text_label.setText(text)
        update_time = text
        # producer process
        p = Process(name="producer", target=producer, args=(q,), daemon=True)
        p3 = Process(name="producer2", target=producer2, args=(qqq, update_time), daemon=True)
        p4 = Process(name="producer4", target=producer2_4, args=(qqqq, update_time), daemon=True)
        p5 = Process(name="producer5", target=producer2_5, args=(qqqqq, update_time), daemon=True)
        p6 = Process(name="producer6", target=producer2_6, args=(a, update_time), daemon=True)
        p7 = Process(name="producer7", target=producer2_7, args=(aa, update_time), daemon=True)
        p9 = Process(name="producer9", target=producer2_9, args=(b, update_time), daemon=True)
        p10 = Process(name="producer10", target=producer2_10, args=(bb, update_time), daemon=True)
        p12 = Process(name="producer12", target=producer2_12, args=(bbb, update_time), daemon=True)
        p13 = Process(name="producer13", target=producer2_13, args=(bbbb, update_time), daemon=True)

        p1 = Process(name="producer1", target=producer2_1, args=(c, update_time), daemon=True)
        p00 = Process(name="producer00", target=producer2_0, args=(cc, update_time), daemon=True)

        p.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p9.start()
        p10.start()
        p12.start()
        p13.start()
        #p1.start()
        p00.start()

    @pyqtSlot()
    def button_clicked1(self):
        print("test")
        pp = Process(name="producer1", target=producer3, daemon=True)
        pp.start()

    @pyqtSlot(str)
    def print_data(self, data):
        self.statusBar().showMessage(data)

    @pyqtSlot(str)
    def print_data1(self, data1):
        print(data1)



if __name__ == "__main__":
    freeze_support()
    q = Queue()
    qq = Queue()
    qqq = Queue()
    qqqq = Queue()
    qqqqq = Queue()
    a = Queue()
    aa = Queue()
    b=Queue()
    bb = Queue()
    bbb = Queue()
    bbbb = Queue()
    c = Queue()
    cc = Queue()

    # Main process
    app = QApplication(sys.argv)
    mywindow = MyWindow(q,qq,qqq,qqqq,qqqqq,a,aa,b,bb,bbb,bbbb,c,cc)
    mywindow.show()
    app.exec_()