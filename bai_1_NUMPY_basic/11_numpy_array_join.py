#mục đích là đưa nội dung của nhiều mảng vào 1 mảng duy nhất
#trong sql nối các bảng dựa trên các khóa(key)
#trong numpy nối mảng theo trục

#sử dụng hàm concatenate()
#vidu: mảng 1 chiều
print('vidu mảng 1 chiều')
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

print('vidu mảng 2 chiều')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#join arrays using stack functions
'''
xếp chồng giống như nối, khác biệt duy nhất là xếp chồng được thực hiện dọc theo một trục mới
chúng ta có thể nối hai mảng 1D dọc theo trụ thứ 2
chúng ta truyền 1 chuỗi các mảng cta mong muốn nối vào phương thức stack() cùng với trục, nếu không được truyền rõ thì nó được coi bằng 0

'''
print('vidu: stack()')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
arr3=np.stack((arr1,arr2),axis=0)
print(arr3)
print(arr)

#stacking along rows: xếp chồng dọc theo hàng
'''
sử dụng hstack() method
'''

print('vidu: hstack()')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

#stack along columns: xếp chồng theo cột
'''
sử dụng vstack() method
'''
print('vidu: vstack()')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)


#stack along height(depth): xếp chồng theo độ sâu
'''
sử dụng dstack() method
'''
print('vidu: dstack()')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)
print(arr.shape)


