######################################################numpy repository https://github.com/numpy/numpy
import numpy as np

############################################################################################################################
######################################################NUMPY VERSION
# print(np.__version__)

######################################################CREATE SIMPLE ARRAY(ALSO SHOW ITS TYPE)
arr1 = np.array([1, 2, 3, 5, 18])
# print(arr1)
# print(type(arr1))

######################################################CREATE ARRAY FROM TUPLE(TUPLES ELEMENTS ARE NOT CHANGING)
arr2 =np.array((10, 20, 30, 40))
# print(arr2)

######################################################0-D, 1-D, 2-D, 3-D ARRAYS(0,1,2,3 dimensions)
arr_0d = np.array(5)
arr_1d = np.array([5, 15, 25, 35, 45])
arr_2d = np.array([[5, 15, 25], [35, 45, 55]])
arr_3d = np.array([[[5, 15, 25], [35, 45, 55]], [[65, 75, 85], [95, 105, 115]]])

# print(arr_0d)
# print('\n')
# print(arr_1d)
# print('\n')
# print(arr_2d)
# print('\n')
# print(arr_3d)

######################################################ARRAY CAN HAVE ANY NUMBER OF DIMANSIONS(EXAMLE FOR 5 DIMENSIONS)
arr3 = np.array([1, 2, 3], ndmin=5)
# print(arr3)
# print('number of dimensions :', arr3.ndim)