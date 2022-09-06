import numpy as np

nums = np.array([1,2,3,4])
num=np.exp(nums)
print(num)

x = np.array([2,4])
y = np.array([1,3])
print(x*y)
print(x.dot(y))
print(np.dot(x,y))
print('nhan ma tran')
X = np.array(([1,2,3], [4,5,6]))
print(X)
Y = np.array(([1,2], [4,5], [7,8]))
print(Y)
Z = np.dot(X, Y)

print(Z)