#  Vision AI 모델링(Hifen 협업) 
관심 기업에 컨택하여 기업에서 실행하길 희망하는 AI 프로젝트 주제를 정의하고 모델링 컨셉 증명(PoC)를 대신 해보는 프로젝트

## 현재 착수 중인 문제
- OCR 에서 텍스트를 뽑기보다 텍스트의 영역을 찾아보자 (관련 논문 정보 위에 업로드됨)  

- 자동차, 펫, 뷰티, 전자제품 위주의 Object detection 을 Rekognition 혹은 자체 모델링을 활용해서 진행해보자  
- ~documentation~
- ~object detection, text detection 우선순위 증명~

## 의뢰 내용
유튜브 비디오 썸네일의 Object detection 을 위한 효용성 높은 Vision Ai 모델 구현.

예시:
![image](https://user-images.githubusercontent.com/77192299/166172528-fb1eda93-bff0-4652-b65b-2a7205e39007.png)

## 기업 제공
백만개 이상의 유튜브 썸네일 데이터, 머신러닝 모델을 테스트할 수 있는 고성능 GPU 서버.

## 예상 결과물
썸네일에서의 텍스트 감지 및 추출,  오브젝트 감지  


## 다음 미팅

6/5 토 15:00

# 6차미팅 전 진행 상황 공유  

1. 참고하라고 보내주신 자료 MMF(Multi-Modal Framework)는 youtube와 논문을 통해서 학습한 상태입니다. 이미지에 대한 자체적인 정보에서 Question answering 할 수 있다는 점이 흥미로웠는데 내용이 조금 어려워 코드를 보며 추가적인 학습이 필요할 것 같습니다.  
2. Rossetta 로 text 영역과 정보 추출하는 거 코드 사용해서 샘플로몇 개 추출 성공했습니다. 토요일 미팅 전까지 다량의 썸네일 데이터 돌려보는 것이 목표입니다.  
3. Object detection도 현재 Yolo V3로 직접 모델링 하고 있는 상황인데, 계속 실행 중에 darknet import 과정에서 에러가 떠서 교수님께 자문을 구하고자 면담을 잡아놓은 상황입니다ㅠ 아마 이것만 해결되면 썸네일 넣고 돌릴 수 있을 것 같습니다.  
- 아래에 저희가 참고한 논문과 샘플 사진 첨부해드립니다.  
![KakaoTalk_20220602_222346538](https://user-images.githubusercontent.com/77192299/171653068-d80d1d59-ace1-4104-8121-d5785273d066.jpg)
![KakaoTalk_20220602_222346538_01](https://user-images.githubusercontent.com/77192299/171653085-62b0909d-ccc0-4fe3-b4b5-3ded70b53bff.png)




[https://paperswithcode.com/paper/rosetta-large-scale-system-for-text-detection](https://paperswithcode.com/paper/rosetta-large-scale-system-for-text-detection)

[https://youtu.be/igAF-48Pwnc](https://youtu.be/igAF-48Pwnc)

- paddle OCR  
[https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/doc/doc_en/whl_en.md](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/doc/doc_en/whl_en.md)
- paddle OCR 기본 구현  
[https://beok.tistory.com/125](https://beok.tistory.com/125)
- Easy OCR  
[https://developer-youn.tistory.com/46?category=764229](https://developer-youn.tistory.com/46?category=764229)

## 5차 미팅(2022-05-29)  
1. OCR 에서 텍스트를 뽑기보다 텍스트의 영역을 찾아보자 (관련 논문 정보 위에 업로드됨)  

관련 논문  

[https://engineering.fb.com/2018/09/11/ai-research/rosetta-understanding-text-in-images-and-videos-with-machine-learning/](https://engineering.fb.com/2018/09/11/ai-research/rosetta-understanding-text-in-images-and-videos-with-machine-learning/)

[https://github.com/facebookresearch/mmbt](https://github.com/facebookresearch/mmbt)

[https://arxiv.org/abs/2005.04790?fbclid=IwAR3yo7xJKW-wr6W-8RUMCEkU-NWVEAyoUeSi7wW_IIWxFUO3MMSCqUIWmwI](https://arxiv.org/abs/2005.04790?fbclid=IwAR3yo7xJKW-wr6W-8RUMCEkU-NWVEAyoUeSi7wW_IIWxFUO3MMSCqUIWmwI)

2. 자동차, 펫, 뷰티, 전자제품 위주의 Object detection 을 Rekognition 혹은 자체 모델링을 활용해서 진행해보자  


# 4차 미팅(2022-05-21)
4차 미팅 후 역할 분담 내용
기간: 2022-05-21~2022-05-28

1. object detection(전체)
- 예상 결과
석범: 샘플 데이터를 통해 yolov3, cascade eff 모델 결과 비교 후 동현에게 결과 공유

용준: 카테고리별로 image 50개씩 뽑아서 샘플 데이터 만들어서 석범, 주영에게 공유

동현:  현재 제목과 썸네일이 동일하게 분류된 데이터와 ocr을 통해 text detection된 데이터를 text detection sample 결과로 보고 이를 object detection sample 결과와 비교하여 우선순위 선정

주영: ocr을 통해 sample데이터를 가지고 text detection 수행하여 동현에게 결과 공유

2. documentation(main: 용준, 다같이.)
notion 워크스페이스 생성한 후
update 내용, 질문 정리하여 미팅 하루 전에 대표님께 공유

3. 논문 공유(main: 동현, 다같이.) 수시로.
4. 다음 미팅 잡기 (미정)

# 3차 미팅(2022-05-17)
<5/21 미팅 전까지 할 일>

- 공통: 금요일 Brainstorming & Study, Insight 공유
- 석범, 용준 : opencv, pytesseract, 샘플 추려서 간단한 코드 구현해보기, 채도 논문 학습.
예상 결과물: 제공받은 데이터에 새로운 컬럼 생성
- 동현 : Multi modal 스터디
예상 결과물: 만들어내는 모델링과 멀티모달 적용에 대해
- 주영 : rekognition 및 다른 사례 학습
예상 결과물: rekognition에서 얻은 insight로 썸네일 detection을 어떻게 찾으면 좋을지 고민.

- usecase 공유 수시로

 - use case 

이미지 다운로드 말고 다른 부분에서 진행사항 있는지 질문하심.

rekognition 살펴볼 것.

분업해라.

더 분발하자.


# 2차 미팅(2022-05-14)

현재 Hifen은 투자기간이라 매우 바쁘다.

## Hifen 대표님 전달사항

- Documentation을 하는 방법에 대해 고민하고 나눠주면 좋을 것이다.

→ 내가 어떤 문제를 발견했고 고민했고 느꼈는지 기록하고 쌓아가는 것이 좋다. 혼자만 똑똑하다고 해결해갈 수 있는 분야가 아니다. 

- 필요한 resource가 있으면 편하게 말해줄 것.
- update사항이 있다면 수시로 공유해줄 것.
- 필요한 데이터가 있으면 말해줄 것.
- 명확한 목표를 설정하고 준비했다가 마지막에 sprint개념으로 단기간에 서버 사용하게 될 것.

## 질문 피드백

- 썸네일 픽셀 값이 다른 부분은 url에서 조정 가능하다.
- F == 19금

→ ‘F’는 사행성 혹은 폭력적이거나 성적인 것들을 F로 분류한다. 

- rekognition과 모델링 동시에 병행하는 방향

→ rekognition 사용은 안전빵 선택지로 두고 직접 모델링을 하면서 실력을 늘리고 도전해보는 기회로 삼아보기로 하였다.

## 12주차의 목표를 정해보는 과정

1) 채도 ,폰트

채도, 폰트를 통해서 통상적으로 이용할 수 있는 mood들이 있나 논문들 살펴보기. (mood를 일일이 라벨링하기는 어려움이 있고, 특정 무드에 대한 가능성만 바라보기로 함.)

2) text detection

오타가 있더라도 정확도가 90%정도밖에 안되더라도 그 문제를 안고 갈 수 있도록 시스템을 만들어가는 것이 중요하다. 아무리 좋은 OCR 가져다 써도 한글과 폰트를 잡아내는 것, 대비가 어렵기 때문에 95%를 목표로 하기보다는 90%정도를 목표로 발전시킬 기반을 닦는 것을 목표로 하면 좋을 것이다.

받은 데이터를 통해 더 뾰족하게 접근해도 된다. 카테고리 부분만 보아서 각 카테고리들이 폰트를 어떤식으로 쓰는지, view count 등을 통해 통계 지식을 이용해서 insight를 얻는 측면으로 접근해도 된다.

hifen에서는 ocr을 통해 한번 학습을 진행해봤으나 정확도가 그리 놓지는 않았다. 

- Multi Modal (멀티모델)

t**ext들을 통해 topic을 나누면서 text정보와 image정보를 모아 묶어서 한 묶음을 거리를 측정하는 방법**.  각자 80% 80%씩 모아서 뽑아서 합쳐서 하면 시너지가 클 것이다. 

## 할일

- Documentation을 잘 한 후 Hifen과 공유
- 12주차의 목표를 정해볼 것
- update사항이 있다면 수시로 공유해줄 것.
- 뾰족하게 데이터에 접근해서 insight에 접근

팀원 미팅: 화 16:30

회사와 미팅: 토 15:00 고정


## 1차 미팅(2022-05-10)

플랫폼을 만든다.

하이픈과 우리 팀이 할 영역은 검색의 영역이다.

집중하는 부분은 카테고리 분류의 영역이다.

DB는 mySQL 사용.

썸네일의 텍스트 분류, 채도, 

<공부했으면 하는 영역>

text detection 영역. object detection영역까지는 어려울 것이다.

의뢰 내용: 유튜브 비디오 썸네일의 Object detection 을 위한 효용성 높은 Vision Ai 모델 구현.

전처리까지 희망.

## 질문

- 하이픈에서 제공해주신 의뢰 내용이 하이픈에서 이미 시도됐던 것인가요? 처음 시도되는 것을 저희 팀이 모델링해보는 것인가요?

→ 처음 시도되는 것.

- 예상 결과물이 ‘썸네일에서의 텍스트 감지 및 추출’, ‘오브젝트 감지’라고 말씀해주셨는데 저희가 제대로 이해했는지 확인 질문을 요청드리고 싶습니다. 썸네일에서 object 감지된 것을 text로 추출하는 것은 물론 텍스트 또한 감지하고 출력시키는 것이 예상 결과물 맞으신가요?

→  text dectection, 채도를 통한 썸네일의 분위기.(어느정도 분위기를 파악할 수 잇을 것이라는 가설을 탐구.)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/40206976-d6f4-4263-b644-7452df1fd784/Untitled.png)

- ~~하이픈은 **지금까지 어떤 식으로 object detection을 수행하셨는지 말씀해주실 수 있나요?**~~

- ~~하이픈에서 제공해주실 것들로 백만개 이상의 유튜브 썸네일 데이터, 머신러닝 모델을 테스트할 수 있는 고성능 GPU 서버를 말씀하셨는데 GPU서버 연결해서 모델 성능 테스트하는 법에 대해 설명해주실 수 있나요?~~

AWS고성능 GPU 제공

- ~~이 의뢰의 결과물이 어떻게 사용될지 질문드리고 싶습니다. 결과물을 통해 인플루언서들의 썸네일의 키워드를 뽑아내어 정리하시려는 것인가요?~~

미팅 마치고 오늘 할일

- 다음 미팅 날짜 정하기(수시로 미팅 최소 주 1회, 16시 이후, )

→ 수시로.

- 문제 정의
- 교수님께 방향성 질문 메일 보내기
- 3~4주의 시간까지 (썸네일 하나를 봤을 때 텍스트 영역(은 힘들 것.)분포 혹은 텍스트의 폰트, 채도 등을 뽑아낼 수 있을 것 같다에 대한 플랜) 플랜을 세우면 좋을 것이다.

11주차 목표 : 가능한 달성 목표를 세우기 

5/13(금)미팅 12:00~15:00 사이 언제든 희망합니다.

- 양샤오펑 교수님
- 아마존 Rekognition을 사용하는 것에 대해 알아볼 것
- 목표 정의, 1주차 학습 목표 세워보기
