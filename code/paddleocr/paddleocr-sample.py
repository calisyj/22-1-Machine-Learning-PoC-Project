from paddleocr import PaddleOCR, draw_ocr
import os
import pandas as pd
import urllib.request as req
import random
from PIL import Image
ocr = PaddleOCR(use_angle_cls = True, lang = 'korean')

# 열어볼 csv파일 위치 설정
df = pd.read_csv('C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/category_video_url.csv')

def downImage(img_url, img_name):
    req.urlretrieve(img_url, img_name + '.jpg')

# 파일 다운로드 받을 dir경로 설정
dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/category/'
n = 1
category_list = df['Main_Topic'].unique()
i = 0
for topic in category_list:
    data = df[df['Main_Topic']==topic]
    hifen_list = data['thumbnails_url'].tolist()
    os.mkdir(dir + topic) # 다운로드받을 폴더 생성
    dir = dir + topic  # 다운로드받을 폴더 경로
    os.chdir(dir) # 경로 지정
    while n<500:
        try:
            # 복원 추출(중복 허용)
            downImage(hifen_list[random.randint(0,len(hifen_list))],str(n))
            print(topic, '분야 다운로드 개수: ', n)
            n = n+1
            i += 1

        except:
            i += 1
            pass
    # 파일 다운로드 받을 dir경로 설정
    dir = 'C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/paddleocr/category/'
    n = 1
    for i in range(1,500):
        os.chdir(dir+topic)
        img_path = str(i)+'.jpg'
        result = ocr.ocr(img_path, cls=True)

        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='malgun.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save('sample'+str(i)+'.jpg')





