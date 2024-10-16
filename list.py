list_a = [1,2,3]
list_b = [2,4,6]

list_c = [a * b for a, b in zip (list_a, list_b) ]
print(list_c)

import numpy as np

array_a = np.array(list_a)
array_b = np.array(list_b)

print(array_a * array_b)

array_1d = np.array([1,2,3,4,5])
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 三维数组矩阵

# 输出每个数组的0,1元素
slice_array_1d = array_1d[0:2]
slice_array_2d = array_2d[0:2]

print(array_1d)
print(array_2d)

print(slice_array_1d)
print(slice_array_2d)

# 真正的切片操作
print(array_2d[0][0])

# 创建一个3维数组
array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(array_3d)

# 创建一个全为5的二维数组:两行三列,用5填充   
array_2d = np.full((2,3), 5)
print(array_2d)

# 降维操作
array_flatten = array_2d.flatten()
print(array_flatten)

# 转置操作:转为3行两列
array_reshape = array_2d.reshape(3,2)
print(array_reshape)

print(array_2d.dtype)
