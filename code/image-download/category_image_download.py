'''
Name: category-image-download.py
작성자: calisyj
Description: 31개의 카테고리별 이미지를 50개씩 다운받는다. 

'''

import pandas as pd
import os
import urllib.request as req
import random

# 열어볼 csv파일 위치 설정
df = pd.read_csv('C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/Hifen project test.csv')

def downImage(img_url, img_name):
    req.urlretrieve(img_url, img_name + '.jpg')

# 파일 다운로드 받을 dir경로 설정
dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/hifen-image/'
n = 1
category_list = df['Main_Topic'].unique()

for topic in category_list:
    data = df[df['Main_Topic']==topic]
    hifen_list = data['thumbnails_url'].tolist()
    os.mkdir(dir + topic) # 다운로드받을 폴더 생성
    dir = dir + topic  # 다운로드받을 폴더 경로
    os.chdir(dir) # 경로 지정
    while n<51:
        try:
            # 복원 추출(중복 허용)
            downImage(hifen_list[random.randint(0,len(hifen_list))],str(n))           
            print(topic, '분야 다운로드 개수: ', n)
            n = n+1
        except:
            pass
    # 파일 다운로드 받을 dir경로 설정    
    dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/hifen-image/'
    n = 1


