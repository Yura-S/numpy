######################################################numpy repository https://github.com/numpy/numpy
import numpy as np

############################################################################################################################
######################################################NUMPY VERSION
print(np.__version__)

######################################################CREATE SIMPLE ARRAY(ALSO SHOW ITS TYPE)
arr1 = np.array([1, 2, 3, 5, 18])
print(arr1)
print(type(arr1))

######################################################CREATE ARRAY FROM TUPLE(TUPLES ELEMENTS ARE NOT CHANGING)
arr2 =np.array((10, 20, 30, 40))
print(arr2)

######################################################0-D, 1-D, 2-D, 3-D ARRAYS(0,1,2,3 dimensions)
arr_0d = np.array(5)
arr_1d = np.array([5, 15, 25, 35, 45])
arr_2d = np.array([[5, 15, 25], [35, 45, 55]])
arr_3d = np.array([[[5, 15, 25], [35, 45, 55]], [[65, 75, 85], [95, 105, 115]]])

print(arr_0d)
print('\n')
print(arr_1d)
print('\n')
print(arr_2d)
print('\n')
print(arr_3d)

######################################################ARRAY CAN HAVE ANY NUMBER OF DIMANSIONS(EXAMLE FOR 5 DIMENSIONS)
arr3 = np.array([1, 2, 3], ndmin=5)
print(arr3)
print('number of dimensions :', arr3.ndim)

######################################################PRINT ELEMENTS OF ARRAY BY INDEX USING ARRAYS CREATED ABOVE
print('third element of arr_1d array ', arr_1d[2])
print('first element of second row in arr_2d array ', arr_2d[1, 0])
print('element in arr_3d arrays thats index - x=1, y=0, z=2 ', arr_3d[1, 0, 2])

######################################################ELEMENTS CA BE ADDED AND CAN BE READED BY END(REVERSE)
print(arr_1d[2] + arr_1d[3])
print(arr_1d[-1])

######################################################ARRAY SLICING(CUTTING A PART OF ARRAY) BY DEFFERENT WAYS
print(arr_1d[1:4:1]) #SYNTAX [start:end:step]
print(arr_1d[3:])
print(arr_1d[:3])
print(arr_1d[::2])

######################################################CREATE ARRAY BY SETTING DATATYPE OF ELEMENTS WHILE CREATING
######################################################IF CANT SET WILL BE 'ValueError'
arr4 = np.array([21, 22, 23, 24, 25], dtype='S')
print(arr4.dtype)

######################################################CHANGING TYPE OF ARRAY ELEMENTS
######################################################IF CANT SET WILL BE 'ValueError'
arr5 = np.array([1.5, 2.5, 3.5])
print(arr5.astype('i'))

######################################################CREATING COPY(COPY CHANGES DOES NOT AFFECT ORIGINAL)
arr6 = np.array([11, 22, 33, 44, 55])
x = arr6.copy()
x[0] = 365
print(arr6)
print(x)

######################################################CREATING VIEW(VIEW CHANGES AFFECTS ORIGINAL)
arr7 = np.array([12, 23, 34, 45, 56])
y = arr7.view()
y[1] = 365
print(arr7)
print(y)