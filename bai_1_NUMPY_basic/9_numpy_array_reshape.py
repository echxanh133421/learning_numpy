#chuyen doi chieu ma tran:

#vi du chuyen 1->2
import numpy as np
print('1->2')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
#chuyển từ 1-<3
print('1->3')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)


#lưu ý là số phần tử phải giống nhau
#kiểu trả ra của method reshape là view không phải copy

#thứ nguyên không xác định: mục đích để tự động tính toán số lượng phần tử của chiều cuối cùng
#vidu:
print('thu nguyen không xác định')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#chuyển về 1 chiều dùng reshape(-1)

#Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.