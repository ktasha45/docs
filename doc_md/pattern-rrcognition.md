# pattern recognition
패턴 인식

## 결정 트리 (DT)
이전의 결정 방법
* 베이지안 (Naive Bayes classifier): 가우시안이란 전제를 두고 분포를 추정한 후에 오차 함수를 설정하고 그걸 최소로 만들게 하는 식으로 분류할 것임
* kNN, PW classifier: non paramatic. 입력 데이터의 주변에 있는 데이터를 보고 판별
* Linear Discrimination: 일차함수(직선)를 긋고 나눈다
* etc...

dt는? tree를 이용해서 분류하는 방식이다.
분류를 위한 트리를 만든다. 바이너리 트리의 발란스 문제?
dt에서는 오분류가 최소가 되어야 함
오분류가 가장 작도록 dt를 만드는 것이 목적임
소규모 분류기를 만들 때 dt를 쓰는게 가장 많음. ㅏnn이랑 같이
데이터가 수천 수만 정도 간단한 분류기는 대개로 kmeans, knn, dt를 잘 결합해서 쓰는 걸 많이 사용함
 


ml은 데이터로부터 분류기를 문들고
패턴인식은 확률론 등의 다양한 것들을 활용함

feature vector