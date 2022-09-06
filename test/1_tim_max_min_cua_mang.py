import numpy as np
#tạo ra mảng ngẫu nhiên 5 phần tử giá trị từ 1-100
array=np.random.randint(1,100,5)
#in mảng ra mành hình
print(array)
#tìm max min của mảng ra màn hình
xmax=array.max()
xmin= array.min()
#in kết quả max min
print(xmin,xmax)
#chỉ mục phần tử lớn nhất trong mảng
print('tìm chỉ mục của phần tử lớn nhất')
print(array.argmax())