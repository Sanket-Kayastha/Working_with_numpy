import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image

from numpy.random import random


z = random((3,3,3))
print(z)
print(z.shape)
print(z.ndim)

# my_array = np.array([1.1, 9.2, 8.1, 4.7])
# print(my_array.shape)
# print(my_array[2])
# print(my_array.ndim)

# array_2d = np.array([[1,2,3,9],[5,6,7,8]])

# print(f"Dimension is {array_2d.ndim}")
# print(f"Its shape is {array_2d.shape}")
# print(f"It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns")
# print(array_2d[1,:])

# mystery_array = np.array([[[0,1,2,3],[4,5,6,7]], [[7,86,6,98],[5,1,0,4]],[[5,36,32,48],[97,0,27,18]]])
# print(f"Dimension is: {mystery_array.ndim}")
# print(f"Shape is {mystery_array.shape}")
# print(f"To get the value of 18 is : {mystery_array[2,1,3]}")
# print(mystery_array[:,:,0])

a = np.arange(10,30)
print(a)
print(a[-3:])
print(a[3:6])
print(a[12:])
print(a[::2])
print(np.flip(a))

b = np.array([6,0,9,0,0,5,0,0])
nz_indices = np.nonzero(b)
print(nz_indices)

# x = np.linspace(0,100, num=9)
# # print(x)
# # print(x.shape)

# y = np.linspace(start=-3, stop=3, num=9)
# print(y)
# plt.plot(x, y)
# plt.show()

noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)
plt.show()

