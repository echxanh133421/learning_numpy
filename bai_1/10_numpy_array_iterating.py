#lặp qua array:
#vidu1:mảng 1 chiều:
print('vidu: lap qua mang 1 chieu:')
import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
  print(x)

#lặp qua mảng hai chiều
print('vidu: lặp qua mảng 2 chiều:')
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
  for y in x:
    print(y)

#3 chiều tuowg tự

#1 số kiến thức khác đọc thêm :
'''
https://www.w3schools.com/PYTHON/numpy/numpy_array_iterating.asp
'''
#nditer(): kiểu dữ liệu, lặp có bước nhảy
#ndenumerate(): toàn bộ phần tử có thêm chỉ số