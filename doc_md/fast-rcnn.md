# fast r-cnn

* r-cnn의 한계
    * roi마다 cnn을 하기 때문에 느림 (both inference and train)
    * 이미지를 (224, 224)로 warping하면서 정보 손실 발생
    * gpu를 사용하기에 적합하지 않음 (svm, selective search)


## 정리
---
## **external document**
* [paper](https://arxiv.org/abs/1504.08083)
## **related document**  
* [object detection](../doc/object-detection.html)