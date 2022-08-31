#numpy có 1 số kiểu dữ liệu bổ sung so với data type basic python:
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

#checking the data type of an array:
#dùng thuộc tính dtype

import numpy as np

arr=np.array([1,4,6,7])
print(arr.dtype)

arr2=np.array(['cuong, huyen'])
print(arr2.dtype)

#create arrays with a define data type
#tạo mảng với định nghĩa kiểu dữ liệu trước
arr3=np.array([1,3,5,67], dtype='S')
print(arr3)
print(arr3.dtype)

#với các kiểu dữ liệu i,u, and u thì ta có thể định gnhixa kích thước trước

#ví dụ tạo ra 1 mảng 4 byte integer
arr4=np.array([1,2,3,4],dtype='i4')
print(arr4)
print(arr4.dtype)

#sẽ bị lỗi nếu như trong array có ít nhát 1 phần tử không thể ép kiểu dữ liệu theo dtype:
#vi dụ trong array có 1 kí tự 'a' không thể dùng dtype='i'


#chuyển đổi kiểu dữ liệu hiện có của mảng:
'''
- cách tốt nhất là tạo ra 1 bản sao của array bằng phương thức astype()
- phương này cho phép tajop ra bản sao của mảng và chỉ định kiểu dữu liệu dưới dạng tham số
- kiểu dữ liệu có thể được chỉ định bằng 1 chuỗi như: 'f' ,'i'...
hoặc có thể dử dụng trực tiếp kiểu dữ liệu như float, int ...
'''
#ví dụ: thay đổi kiểu dữ liệu từ float sang int
print('ví dụ chuyển từ float sang int')
arr5=np.array([1.1,5.7,3.4])
newarr=arr5.astype('i')
newarr1=arr5.astype(int)
print('cach 1:',newarr)
print('cach2:',newarr1)
print(newarr.dtype,newarr1.dtype)