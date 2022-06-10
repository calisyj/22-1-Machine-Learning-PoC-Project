import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os 

# Binary image로 변환
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
    image_rm = remove_noise(image)
    image_sharp = sharpen_image(image_rm)
    return image_sharp

#이미지 저장
image = cv2.imread('C:/Users/7info/Desktop/Hifen Project/thumbnail image/72.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('C:/Users/7info/Desktop/Hifen Project/edited image/72.jpg', image)

# 저장된 이미지를 하나씩 불러와서 전처리 한다.
images = sorted(glob.glob('C:/Users/7info/Desktop/Hifen Project/thumbnail image/*.jpg'), key=os.path.getctime)
for path in images:
    i = 0
    print(i)
    i += 1
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image_processed = preprocess(image)
    cv2.imwrite(path, image)
    
