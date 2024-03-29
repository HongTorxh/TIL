# 기계학습11(Logistic Regression)

![스크린샷 2022-08-18 오후 4.21.08.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.21.08.png)

- linear model은 모델이 단순하고, 관계가 linear할때 적용 가능하여, 제약 상황이 있긴 하지만,
- 해석 가능성도 좋고, 의외로 linear한 모델로 설명할 수 있는 부분들이 꽤 많아서 많이 사용되고 있다.
- K-NN 같은 알고리즘은 test phase에서 굉장히 느림, semple 수 만큼 매번 distance를 계산해야하기 때문에 굉장히 느리지만, linear 모델은 그렇지 않고, 학습할때도 빠르고, test할때도 빠르다는 장점을 가지고 있다.

![스크린샷 2022-08-18 오후 4.28.21.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.28.21.png)

- logistic regression의 output은 각 class에 대한 확률 값
- 확률 값 자체를 직접 사용할 수도 있고, 적절한 threshold를 두어서 1,0으로 변환하여 사용할 수도 있다.
- linear regression에서는 y값을 직접 예측하기 위함이지만, 분류 문제에서는 linear regression이 적합하지 않기 때문에, 이것을 numeric한 값인 특정 class의 확률 값으로 변환을 해서 모델링을 하고 예측을 하게 됨.

![스크린샷 2022-08-18 오후 4.30.56.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.30.56.png)

- Logistic function or Sigmoid function
- t가 커질수록 1에 가까워지고, 작아질수록 0에 가까워짐

![스크린샷 2022-08-18 오후 4.32.02.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.32.02.png)

- simple이라는 것은 x 변수가 1개일 때
- x가 주어져있을 때, y가 1일 확률 값을 모델링 하는데, 그냥 x에 관한 1차식이 아니라, x에 관한 linear식을 logistic function에 넣은 걸로 표현 됨.
- 학습해내야 하는 parameter는 B0,B1 두개
- 크게는 2가지 목적
    - B1이 0인가, 아닌가 ; x값이 y에 얼마나 영항을 미치는지 예측
    - coefficient 해석하는 용도

![스크린샷 2022-08-18 오후 4.36.24.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.36.24.png)

- y가 1일 확률로 확률값을 y축에 대응하게 한다면, 부드러운 곡선이 모델링된다.

![스크린샷 2022-08-18 오후 4.38.19.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.38.19.png)

- 명확하게 나뉘어져있는경우 되게 쉽게 curve를 구할 수 있다.
- 가파른 곡선이 생기긴 한다.

![스크린샷 2022-08-18 오후 4.39.34.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.39.34.png)

- 값이 노이즈가 많은 경우, 곡선이 완만하게 변함.
- 그리고 위 그림을 보면, curve가 0과 1에 붙어있지 않는 것을 보아 확신이 없어보일수 있다.

![스크린샷 2022-08-18 오후 4.40.28.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.40.28.png)

- B1을 해석이 가능한데, linear regression처럼 직접적으로 해석이 되진 않음.
- 이유 ? B1이라는 것이 직접 y를 모델링하기 위한 기울기가 아니라, y가 1일 확률을 예측하는 기울기이기 때문이다.
- But, 비례하는 관계가 있긴 하다.

![스크린샷 2022-08-18 오후 5.07.45.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.07.45.png)

- odd : 0의 확률분의 1의 확률 ; 성공의 확률 / 실패 확률

![스크린샷 2022-08-18 오후 5.17.25.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.17.25.png)

- p개 만큼의 variable이 있을때, p+1개의 파라미터를 추정해야댐

![스크린샷 2022-08-18 오후 5.23.29.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.23.29.png)

- simple과 multiple일때, 서로 학생변수에 대한 coefficient값이 양과음으로 다름
    - student자체가 다른 변수들의 값을 다 무시하고 y값과 관계가 있는지를 보여주는 것이 아니라  다른 변수가 주어져 있을 때, 추가적으로 student변수를 줄이거나 키웠을 때, 어떻게 변화하는지 보여주는 것?

![스크린샷 2022-08-18 오후 5.30.35.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.30.35.png)

- multi-class 자체를 모델링 하는 방식
- 1대 다로 모델링 하는 방식
- Multinomial logistic regression : multi-class 자체를 모델링 하는 방식 ; softmax regression이라고도 불림
    - class가 k개, wk는 백
    - 상호, 겹치지 않는 class에 경우에 사용하면 좋음.
    - 1이라는 숫자를 k개의 클래스가 나누는 방식으로 진행되기 때문에

![스크린샷 2022-08-18 오후 5.35.15.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.35.15.png)

- binary classifier를 여러번 사용하는 방식도 있음
- 1 대 다
- 특히, 여러개의 class에 모두 속할 가능성이 있는 경우에도 사용 가능

![스크린샷 2022-08-18 오후 5.38.15.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.38.15.png)

- 상황에 따라 알맞게 사용해라

![스크린샷 2022-08-18 오후 5.38.35.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.38.35.png)

- linear regression보다 훨씬 복잡하다.
    - 예측값과 실제값의 차이의 제곱에 합이 가장 작아지는 쪽으로 함
    - 항상 유일한 최저점을 가짐
    - 쉽게 계산 가능
- likelihood(각 확률에 대하여 weight * x를 다 한것)를 가장 크게 해주는 y값을 찾자!

![스크린샷 2022-08-18 오후 5.40.52.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.40.52.png)

![스크린샷 2022-08-18 오후 5.45.34.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.45.34.png)

![스크린샷 2022-08-18 오후 5.47.02.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.47.02.png)

- overfitting을 방지하기 위해 L2 penalty 사용

![스크린샷 2022-08-18 오후 5.49.43.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.49.43.png)

- regularization을 적당히 해서 찾아라

![스크린샷 2022-08-18 오후 5.50.17.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.50.17.png)

- class별로 분포에 대한 가정 x
- dicision boundary에 집중하는 모델
- logistic regression 모델을 학습을 했다고 해서 각 클래스에 해당하는 샘플을 모델로부터 생성 불가, 구별만 가능
- 복잡한 boundary에서는 작동하지 않을 수 있다.

![스크린샷 2022-08-18 오후 5.52.48.png](%E1%84%80%E1%85%B5%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B811(Logistic%20Regression)%20ba15780187f44326a1009313ad5a2fd7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-08-18_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.52.48.png)

- regression model은 outcome, y값에 대한 predictor, x값들의 평균적인 effect를 예측하는 것
- multiple regression인 경우 각각 Predictor들이 다른 predictor들을 조정해주는 것, 특정 변수가 어느정도 영향이 있는지
- 연관 없는 변수들을 최대한 제거하는게 훨씬 유리하다.
- coefficent 해석, 모델 예측