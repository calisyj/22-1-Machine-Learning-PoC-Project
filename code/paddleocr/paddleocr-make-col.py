#'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/category/'
#'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/hifen-image/'
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
new_df = df
def downImage(img_url, img_name):
    req.urlretrieve(img_url, img_name + '.jpg')

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ", "
    return result.strip()

# 파일 다운로드 받을 dir경로 설정
dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/image/'
n = 1


hifen_list = df['thumbnails_url'].tolist()
os.mkdir(dir) # 다운로드받을 폴더 생성
os.chdir(dir) # 경로 지정
new_df['text'] = 0 # text detection 결과 넣을 열 추가

i = 0
while n<101:
    try:
        # 복원 추출(중복 허용)
        downImage(hifen_list[i],str(n))
        print('다운로드 개수: ', n)
        n += 1
        i += 1

    except:
        i += 1
        pass

    # 파일 다운로드 받을 dir경로 설정
dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/image/'
n = 1
for i in range(1,10):
    high_txts = []
    img_path = str(i)+'.jpg'
    result = ocr.ocr(img_path, cls=True)
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    for j in range(len(txts)):
        if scores[j]>=0.95:
            high_txts.append(txts[j])
    new_df['text'][i] = listToString(high_txts)

dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/'
os.chdir(dir) # 경로 지정
new_df.to_csv('sample.csv', header = False, index = False, encoding='utf-8-sig')
