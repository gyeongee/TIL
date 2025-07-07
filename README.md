# 250708
### pairplot() : 각 특성들의 관계를 시각화
선형 관계를 가지는 특성들을 발견 
> 다중공선성을 가질 수도 있기에 확인 필요 
> 
정량적 확인 : 상관관계수 확인
> 변수들간의 상관계수가 유의미하다는 것은 변수들끼리의 연관성이 높다는 의미, 중복된 의미를 가지는 특성이 여러개가 되어 회귀계수의 가중치가 불안정해짐 

### 회귀모델이 어떤 변수에 얼마만큼의 중요도를 부여할지 결정하기 어려워진다.
## 즉, 모델이 불안정해짐

## 다중공선성 확인
- VIF
```python
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# VIF 지표 담아줄 리스트
vif_list = []

# VIF 지수를 시각화 할 데이터프레임 생성
vif_data = pd.DataFrame()

# X 데이터프레임에 숫자형 데이터만 추출
vif_data['특성'] = X.select_dtypes(include='number').columns.tolist()

for i in range(len(X.select_dtypes(include='number').columns.tolist())):  # X_one의 열의 개수
    vif = variance_inflation_factor(X[X.select_dtypes(include='number').columns.tolist()].values, i)  # i는 현재 계산할 변수의 열 번호
    # vif_list에 추가
    vif_list.append(vif)

vif_data['vif_list'] = vif_list
vif_data
```

| 특성       | VIF 값        |
|------------|---------------|
| Rooms      | 99.29         |
| Bedroom2   | 94.53         |
| Bathroom   | 9.45          |
| Car        | 4.78          |
| Distance   | 4.57          |
| Lattitude  | 266,003.80    |
| Longtitude | 266,080.02    |
## 해결방법 ##
# 다중공선성이 발생하는 특성들끼리 특성곱, 특성합, 하나를 삭제
#dfdf
