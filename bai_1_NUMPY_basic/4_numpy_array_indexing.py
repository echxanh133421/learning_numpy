#truy cập phần tử mảng
import numpy as np

arr=np.array([1,2,3])
print(arr[0])

arr_2d=np.array([[1,2,3],[1,5,6]])
print(arr_2d[0,1],arr_2d[1,2])

arr_2d_am = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr_2d_am[1, -1])