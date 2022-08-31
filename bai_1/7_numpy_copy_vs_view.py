#the difference between copy and view
#sự khác nhau giữa bản sao và dạng xem:

'''
-bản sao là 1 array mới, còn view là dạng xem của maeng ban đầu
-bản sao(copy) sở hữu dữ liệu , thay đổi trên bản sao sẽ không ảnh hưởng đến bản gốc và ngược lại
-dạng xem (view) không sở hữu dữ liệu, thay đổi dữ liệu trên bản gốc sẽ làm thay đổi view và ngược lại

'''

#ví dụ minh họa:

import numpy as np

arr=np.array([1,3,4,67,3])
x=arr.copy()
arr[0]=42
print('bản gốc thay đổi:')
print(arr)
print('bản gốc thay đổi không làm thay đối bản copy:')
print(x)

arr1=np.array([1,4,2,34,5,6])
x=arr1.view()
arr1[2]=8
print('vidu: thay dổi bản gốc ảnh hưởn đến  view')
print('bản gốc sau khi thay đổi:',arr1)
print('bản view sau khi thay đổi bản gốc:',x)

#checking if array owns its data: kiểm ttra xem mảng có sở hữu dữ liệu của nó hay không
'''
như trên đã nói coppy thì sở hữu dữ liệu, còn view thì không
-cách kiểm tra: thuộc tính base
+none là có sở hữu dữ liệu
+trả ra dữ liệu tham chiếu đối tượng ban đầu thì không sở hữu dữ liệu
'''
#ví dụ minh họa:
print('vidu: kiểm tra sở hữu dữ liệu')
arr5=np.array([1,4,6,7,3])
x=arr5.copy()
y=arr5.view()
print(x.base)
print(y.base)
