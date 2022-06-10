from paddleocr import PaddleOCR, draw_ocr
import os
import pandas as pd
import urllib.request as req
import random
from PIL import Image


ocr = PaddleOCR(use_angle_cls = True, lang = 'korean')
img_path = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/hifen-image/피트니스 & 다이어트/1.jpg'
result = ocr.ocr(img_path, cls=True)

# draw result
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]


for i in range(len(scores)):
    if scores[i]>=0.9:
        high_txts.append(txts[i])
im_show = draw_ocr(image, boxes, txts, scores, font_path='malgun.ttf')
im_show = Image.fromarray(im_show)
os.chdir('C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/category')
im_show.save('result.jpg')


print(high_txts)