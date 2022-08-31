#splitting numpy arrays

#chia tách mảng:
#tạo ra nhiều mảng từ 1 mảng
'''
#sử dụng array_split()
'''
#vidu:

import numpy as np
print('vi du: cắt 1 mảng 1 chiều 6v phần tử thành 3 mảng 2 phần tử')
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])

print('vidu 2:')
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

#có phương thức split() nhưng nó không tự điều chỉ được phần tử cắt như trong vị du2 ở trên

#giá trị mà hàm rtar về là 1 mảng gồm các mảng con


#splitting 2-D arrays
'''
tương tụ như ở trên
'''
print('vidu: cắt amrng hai chiều:')
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print('chieu array ban đầu:',arr.shape)
newarr = np.array_split(arr, 3)
print(newarr)

print('vidu cat array 2 chiều theo trục khác:')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print('chieu cua ma tran ket qua',newarr[0].shape)
print(newarr)


#vidu :
print('hsplit')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr[0])

#Các thay thế tương tự cho vstack () và dstack () có sẵn dưới dạng vsplit () và dsplit ()
