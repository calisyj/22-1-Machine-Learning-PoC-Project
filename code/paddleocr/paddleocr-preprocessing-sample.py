'''
description: 전처리 수행 후 paddle ocr text detection 수행 후 95%이상 정확도를 갖는 text데이터를 csv text열에 추가하는 코드
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

# Binary image로 변환 (흑백)
def image_threshold(image):
    result = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return result

# 노이즈 제거
def remove_noise(image, kernel_size=5):
    result = cv2.medianBlur(image, ksize=kernel_size)
    return result

# 이미지 선명하게 표현
def sharpen_image(image, kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])):

    image_sharp = cv2.filter2D(image, -1, kernel)
    return image_sharp

# 위의 함수들을 합치는 전처리 함수
def preprocess(image):
    image_bi = image_threshold(image)
    return image_bi


# 파일 다운로드 받을 dir경로 설정
dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/image/'


n=1
hifen_list = df['thumbnails_url'].tolist()
os.mkdir(dir) # 다운로드받을 폴더 생성
os.chdir(dir) # 경로 지정
df['text'] = 0 # text detection 결과 넣을 열 추가
i = 0
while n<101:
    try:
        downImage(hifen_list[i],str(i)) # 이미지 다운로드
        print('다운로드 개수: ', n)
        image = cv2.imread(dir+str(i)+'.jpg', cv2.IMREAD_GRAYSCALE) #다운받은 이미지 전처리
        image_processed = preprocess(image) #다운받은 이미지 전처리
        high_txts = []
        result = ocr.ocr(image_processed, cls=True)
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        for j in range(len(txts)): # 전처리된 이미지 text detection 정확도 95%이상인 데이터 추출
            if scores[j] >= 0.95:
                high_txts.append(txts[j])
        df['text'][i] = listToString(high_txts)
        n += 1
        i += 1

    except:
        i += 1
        pass


dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/'
os.chdir(dir) # 경로 지정
df.to_csv('sample.csv', header = True, index = False, encoding='utf-8-sig')
