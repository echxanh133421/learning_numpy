#số ngẫu nhiên là gì
'''
số ngẫu nhiên không có nghĩa là một số khác mỗi lần
mà có nghĩa là một cái gì đó không thể dự đoán 1 các logic
'''

#Pseudo random and True Random
import random

'''
-máy tính thì hoạt dộng dựa trên các chương trình , vậy phải cso chương trình tạo ra số ngẫu nhiên.
-nếu 1 chương trình tạo ra 1 số ngẫu nhiên thì nó có thể dự đáon , do đó không thực sự ngẫu nhiên.
-các số ngẫu nhiên được tạo ra thông qua các thuật toán thì gọi là ngẫu nhiên giả
-chúng ta có thể tạo ta các số thực sự ngẫu nhiên không?
+để tạo ra số ngẫu nhiên chúng ta càn các dữ liệu ngẫu nhiên ở bên ngoài....
- trong huosng dẫn này chỉ hướng dẫn các số giả ngẫu nhiên

'''

#tạo số ngẫu nhiên nguyên
import numpy
from numpy import random
x=numpy.random.randint(100)
y=random.randint(100)
print(x)
print(y)

#tạo ra số float ngẫu nhiên
print('tạo ra số float từ 0-1')
x = random.rand()
print(x)

#tạo array ngẫu nhiên:
print('vidu: tạo mảng ngãu nhiên nguyên có 5 phần tử')
x=random.randint(100, size=(5))
print(x)

#tạo array ngẫu nhiên 2d:
print('tạo mảng 2d ngẫu nhiên, mảng nguyên')
x = random.randint(100, size=(3, 5))
print(x)

#tạo mảng ngẫu nhiên kiểu float
print('vd: tạo mảng 1 chiều ngẫu nhiên float:')
x=random.rand(5)
print(x)

print('vd: tạo mảng 2d ngẫu nhiên float:')
print(random.rand(3,4))

#tạo số ngẫu nhiên từ mảng:
print('chọn số bất kì trong mảng:')
x = random.choice([3, 5, 7, 9])
print(x)

print('tạo mảng  bất kì với các sô cho truosc:')
x = random.choice([3, 5, 7, 9], size=(3,5))
print(x)