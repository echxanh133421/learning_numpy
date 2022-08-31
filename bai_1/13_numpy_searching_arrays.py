#dùng where method: tìm index

import numpy as np
print('tìm vị tri co gia tri =4:')
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

print('tim vi tri co gia trị chia dư cho 2==1')
x = np.where(arr%2 == 1)
print(x)

#search sorted
'''
searchsorted() method
'''
print('vidu: search sorted: tìm vị trí chèn vào mảng đã sắp xếp')
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

#search from the rigth side: tìm kiếm từ bên phải

#vidu:
print('vd: tìm kiếm từ bên phải sang:')
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

print('search sorted nhiều biến')
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
