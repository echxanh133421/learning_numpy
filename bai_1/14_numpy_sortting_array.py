#sort() method

import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

#trả ra bản copy

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

#sort 2d array

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))