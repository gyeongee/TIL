# coding: utf-8
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))

import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


#normalize=True로 설정하여 0~255 범위인 픽셀값을 0.0~1.0 범위로 변환
# 데이터를 특정 범위로 변환하는 처리를 정규화라고 함
# 입력 이미지 데이터에 대한 전처리 작어븡로 정규화 수행
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    weight_path=os.path.join(
        os.path.dirname(__file__),
        "sample_weight.pkl"
    )
    with open(weight_path, 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y) # 확률이 가장 높은 원소의 인덱스를 얻는다.
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
