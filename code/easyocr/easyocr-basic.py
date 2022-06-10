import easyocr
import numpy as np
import random
import cv2

reader = easyocr.Reader(['ko','en'], gpu=False) # need to run only once to load model into memory
result = reader.readtext('C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/easyocr/2.jpg')
img = cv2.imread('C:/Users/user/Desktop/22-1/Machine Learning For Etrepreneurship/Hifen/code/easyocr/2.jpg')

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(255, 3), dtype="uint8")

for i in result:
    x = i[0][0][0]
    y = i[0][0][1]
    w = i[0][1][0] - i[0][0][0]
    h = i[0][2][1] - i[0][1][1]

    color_idx = random.randint(0, 255)
    color = [int(c) for c in COLORS[color_idx]]

    cv2.putText(img, str(i[1]), (int((x + x + w) / 2), y - 2), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

cv2.imshow("2", img)
cv2.waitKey(0)
