#Mô-đun NumPy Random cung cấp hai phương pháp cho việc này: shuffle()và permutation().

#xáo trộn mảng
print('xáo trọn mảng')
from numpy import random
import numpy as np
print('làm thay đổi mảng cũ')
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

#tạo hoán vị mảng
print('tạo ra mảng mới không ảnh hưởng mảng cũ')
print('tạo hóa vị mảng')
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))