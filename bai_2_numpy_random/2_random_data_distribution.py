#phân phối ngẫn nhiên:
from numpy import random
print('tạo mảng với các số 3,5,7,9 với xác xuất  lần lượt:0.1,0.3,0.6,0.0')
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
