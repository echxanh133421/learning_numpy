#shape of an array:hình dạng của 1 mảng
'''
là số phần tử trong mỗi chiều của array
'''

import numpy as np
#visu1:
print('vidu1:')
arr=np.array([[1,2,3],[3,5,6]])
print(arr.shape)

print('vidu2:')
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

#vidu2: chuyển từ mảng 1 chiều sang 2 chiều:
print('chuyển từ mảng 1 chiều sang mảng 2 chiều')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr=arr.reshape(4,3)
print(newarr)
print('chuyển từ mảng 2 chiều sang 1o chiều:')
print(newarr.reshape(-1))