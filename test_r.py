import os
import pandas as pd
import numpy as np
path = "C:/Users/그린써브(D)/Desktop/ff/Check"
file_list = os.listdir(path)
max = 0
max_file = "n"
#print("file_list: {}".format(file_list))
for fir in file_list:
    mkdir_time = os.path.getmtime(path + "/" + fir)
    if mkdir_time > max:
        max = mkdir_time
        max_file = path + "/" + fir
print(max_file)

non_df = pd.read_csv(max_file, encoding='euc-kr')
count_data = non_df["입고예약"].values.tolist()
print(count_data)
# 하나라도 미처리 ""가 아닌 다른 값이 있을 때 재 실행
for idx, c in enumerate(count_data):
    if int(c[0]) !=0 :
        print("check",int(c[0]),non_df["미처리 예약"][idx])
        if non_df["미처리 예약"][idx] == "" or non_df["미처리 예약"][idx] == 'x':
            print(27)