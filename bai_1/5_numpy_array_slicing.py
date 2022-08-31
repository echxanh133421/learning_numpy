'''
[start:end]
[start:end:step]

không có index số bắt đầu thì mặc định là 0
không có index end thì mặc định là hết mảng
không có step thì mặc đing step=1
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#negative slicing; chỉ số âm

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#step
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#các chỉ số chẵn
print(arr[::2])


#slicing 2d array:
print('cat mang  chieu:')
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
