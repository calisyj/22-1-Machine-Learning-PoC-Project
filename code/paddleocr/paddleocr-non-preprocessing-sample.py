'''
description: paddle ocr text detection 수행 후 95%이상 정확도를 갖는 text데이터를 csv text열에 추가하는 코드
'''

from paddleocr import PaddleOCR, draw_ocr
import os
import pandas as pd
import urllib.request as req
import numpy as np
import glob
import cv2
import random
from PIL import Image
ocr = PaddleOCR(use_angle_cls = True, lang = 'korean')



# 열어볼 csv파일 위치 설정
df = pd.read_csv('C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/category_video_url.csv')

def downImage(img_url, img_name):
    req.urlretrieve(img_url, img_name + '.jpg')

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ", "
    return result.strip()

# 파일 다운로드 받을 dir경로 설정
dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/image/'



hifen_list = df['thumbnails_url'].tolist()
os.mkdir(dir) # 다운로드받을 폴더 생성
os.chdir(dir) # 경로 지정
df['text'] = 0 # text detection 결과 넣을 열 추가
n=1
i = 0
while n<101:
    try:
        downImage(hifen_list[i],str(i)) # 이미지 다운로드 받아서 i.jpg로 저장
        high_txts = []
        img_path = str(i) + '.jpg'
        result = ocr.ocr(img_path, cls=True)
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        for j in range(len(txts)): # 정확도 높은 text값 dataframe text열에 추가
            if scores[j] >= 0.95:
                high_txts.append(txts[j])
        df['text'][i] = listToString(high_txts)
        print('다운로드 개수: ', n)
        n += 1
        i += 1
    except:
        i += 1
        pass

dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/'
os.chdir(dir) # 경로 지정
df.to_csv('sample.csv', header = True, index = False, encoding='utf-8-sig')
