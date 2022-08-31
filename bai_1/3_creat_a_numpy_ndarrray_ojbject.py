#ví dụ tạo dối tượng mảng
#dùng phương thức array()
#có thể sử dụng list, tuple, hoặc bất kì dối tượng nào giống mảng


import numpy as np
#list
arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
#tuple
arr2=np.array((1,2,3,4))
print(arr2)

#0-D array: 1 phần tử
arr = np.array(42)
print(arr)

#1-D array: mảng 1 chiều
arr=np.array([3,6,7,4])
print(arr)

#2-D array: mảng 2 chiều

arr3=np.array([[1,2,3],[3,4,6]])
print(arr3)

#3-D array: mảng 3 chiều: tuoqwng tự

#check number of dimensios: kiểm tra số chiều
'''
thuộc tính ndim
'''
print(arr3.ndim)

#higher dimensional arrays: tạo ra mảng với số thứ nguyên mong muốn
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

