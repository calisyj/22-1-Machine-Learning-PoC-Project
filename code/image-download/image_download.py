'''
Name: image-download
작성자: calisyj
Description: 

'''
import pandas as pd
import os
import time
import urllib.request as req

# 열어 csv파일 위치 설정
df = pd.read_csv('C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/Hifen project test.csv')

hifen_list = df['thumbnails_url'].tolist()

def downImage(img_url, img_name):
    # 다운받을 파일 위치 설정
    dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/hifen-image/'
    req.urlretrieve(img_url, dir + img_name + '.jpg')

n = 1
na = 0
for i in range(0,10001):
    try:
        downImage(hifen_list[i],str(n))
        print('저장된 이미지 수: ', n)
        n = n+1
    except:
        na = na+1
        pass
print('url문제로 누락된 image 수: ', na)




