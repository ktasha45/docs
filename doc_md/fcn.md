# Fully Convolutional Networks for Semantic Segmentation
[paper](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf)

## 1. abstract
* Convolutional networks are powerful visual models that yield hierarchies of features
* pixels-to-pixels으로 훈련된 Convolutional networks는 semantic segmentation에서 기존의 sota를 능가함.
* FCN은 임의의 크기의 이볅을 받아 그에 상응하는 크기의 출력을 생성한다.
* AlexNet, VGGnet, GoogLeNet을 FCN으로 adapt시키고 segmentation으로 파인튜닝 시킴
* skip architecture를 정의하고 deep, coarse layer의 semantic information과 shallow, fine layer의 semantic information과 결합시킨다 to produce accurate and detailed segtation.
* 이 FCN은 pascal voc 2012에서 sota를 달성함. 사진 한 장당 0.2초의 시간이 걸림. 
* NYUDv2, SIFT Flow ?

## 2. introduction
* convnet은 이밎 분류에서 좋은 성능을 보이고 있지만, 이 외에도 loal tasks with structured output에서도 진전을 보이고 있음
* loal tasks with structured output에는 bounding box object detection, part and keypoint prediction, local correspondence?? 이 포함됨.
* convnet은 dense prediction을 위한 per-pixel task에서 효율적으로 학습될 수 있음. (semantic segmentation 같은 task)
* end-to-end, pixels-to-pixels로 학습된 FCN이 semantic segmentatin에서 별다른 machinery 없이 sota를 능가하는 것을 보여주는 논문임
* 첫 번쨰 작업은 pixelwisw prediction을 위해 end-to-end로  supervised pre-training 된 기존 네트워크로부터 FCN을 훈련시키는 것이다.
* 기존 CNN의 FCN 버전은 임의의 크기 입력에서 dense output을 예측한다.
* feedfoward와 backpropagation으로 추론하고 학습된다. Both learning and inference are performed whole-image-at-a-time
* 네트워크의 업샘플링 레이어는 subsampled pooling과 함께 pixelwise prediction과 learning을 가능하게 한다. ??
---
* 이 방법은 asymptotically and absolutely 효율적이다. 다른 복잡한 무언가가 필요하지 않다.
* patchsiw training은 흔하지만 FCN 학습에서의 효율성이 부족하다. 따라서 이 논문에서는 pre- and post-processing을 하지 않는다. 여기에는 superpixel, proposals, post-hoc refinement bt random fields, local classifiers 등이 포함된다.
* classification에서 tense-prediction으로의 trasfer learning이 가능함. reinterpreting classification nets as FCN and fine tuning from their learned representations.
* 대조적으로 이전 연구에선 pre-training 없이 소형 convnet을 사용했다. -> 이전 연구는 뭔지
---
* semantic segmentation은 semantics and location 사이의 inherent tension에 직면하고 있음. global information은 '무엇'을, local information은 '어디'를 해결한다.
* deep feature 계층(CNN)은 비선형 local-to-global 피라미드에서 location과 semantics를 인코딩한다. (둘을 혼합해서 수행할 수 있다는 의미인가?)
* 이런 특징을 결합하기 위해 skip 아키텍쳐를 정의함. 깊고 거친(deep and coarse, semantic) 의미 정보와 얕고 미세한(shallow and fine, appearance) 외관 정보를 결합한 이 특징 스펙트럼을 활용하기 위해서.

## 2. Ralated Work
* 이 논문의 접근 방법은 deep net의 최근 성과에 의존한다. (Our approach draws on recent successes) 
* semantic segmentation in hybrid proposal classifier models?
* Viterbi decoding
* 2-dimensional maps of detection scores for the four corners of postal address blocks
*  Fully convolutional training is rare, but used effectively
* Several recent works have applied convnets to dense prediction problems, including semantic segmentation
* 

## 3. FCN
* each layer of data in convnet은 3차원 배열이다. (h, w, d). h와 w는 sptial(공간) dimension이고 d는 channel dimension이다. 첫 번쨰 레이어는 이미지로, (h, w)의 픽셀 사이즈와 d개의 color channel을 가지고 있다.
* 상위 계층의 location은 이미지에서 경로로 연결된 위치에 해당되며, 이를 receptive fields라고 한다. (pooling까지 포함하는지는 모르겠음)
* convent은 translation inveriance를 기반으로 한다. convolution, pooling, activation의 basic components는 local input region에서 작동하고 상대적인 공간 좌표에만 의존한다. $\mathbf{x}_{ij}$를 특정 레이어의 (i, j)위치에 있는 데이터의 벡터로 나타내고, 다음 레이어의 출력 $\mathbf{y}_{ij}$ 다음과 같이 계산된다.
$$\mathbf{y}_{ij}=f_{ks}(\{\mathbf{x}_{si+\delta i,sj+\delta j}\}_{0 \le \delta i, \delta j \le k})$$
* k는 커널 크기, s는 스트라이드 혹은 subsampling factor, $f_{ks}$는 레이어의 유형(convolution, avgpool, maxpool, activation, 혹은 다른 무언가)이다. 
---
### 3.1 Adapting classifiers for dense prediction
