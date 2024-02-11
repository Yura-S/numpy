import numpy as np

############################################################################################################################
######################################################SHAPE OF ARRAY(HOW MANY ELEMENTS GAVE EVERY DIMENSION) - ARRAY SIZE
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr1.shape)

######################################################ARRAY CAN BE RESHAPED TO OTHER ARRAY(IF THERE RIGHT ELEMTS COUNT)
arr2 = arr1.reshape(2, 2, 2)
arr3 = arr1.reshape(-1)
# print(arr2)
# print(arr3)

######################################################ITERATING(GOING THROUGHT ELEMENTS ONE BY ONE)
arr4 = np.array([5, 15, 25, 35, 45])
for i in arr4:
    print(i)

arr5 = np.array([[11, 22, 33], [44, 55, 66]])
for i in arr5:
    for j in i:
        print(j)

######################################################ITERATING BY nditer()
