import numpy as np

############################################################################################################################
######################################################SHAPE OF ARRAY(HOW MANY ELEMENTS GAVE EVERY DIMENSION) - ARRAY SIZE
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr1.shape)

######################################################ARRAY CAN BE RESHAPED TO OTHER ARRAY(IF THERE RIGHT ELEMTS COUNT)
arr2 = arr1.reshape(2, 2, 2)
arr3 = arr1.reshape(-1)
print(arr2)
print(arr3)

######################################################ITERATING(GOING THROUGHT ELEMENTS ONE BY ONE)
arr4 = np.array([5, 15, 25, 35, 45])
for i in arr4:
    print(i)

arr5 = np.array([[11, 22, 33], [44, 55, 66]])
for i in arr5:
    for j in i:
        print(j)

######################################################ITERATING BY nditer()
arr6 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for i in np.nditer(arr6):
  print(i)

######################################################ITERATING WITH STEPS
arr7 = np.array([[11, 22, 33, 44], [55, 66, 77, 88]])

for i in np.nditer(arr7[:, ::2]):
  print(i)

######################################################ITERATE ARRAY WITH DIFFERENT DATA TYPES
arr8 = np.array([46, 2, 2943])

for i in np.nditer(arr8, flags=['buffered'], op_dtypes=['S']):
  print(i)  

######################################################ENUMERED ITERATION
arr9 = np.array([15, 25, 35])

for idx, i in np.ndenumerate(arr9):
  print(idx, i)

######################################################JOINING ARRAYS
arr10 = np.array([1, 2, 3])
arr11 = np.array([4, 5, 6])
arr12 = np.concatenate((arr10, arr11))
print(arr12)

######################################################JOIN ARRAYS AS ROWS(hstack)
arr13 = np.array([111, 222, 333])
arr14 = np.array([444, 555, 666])
arr15 = np.vstack((arr13, arr14))
print(arr15)

######################################################JOIN ARRAYS AS COLUMNS(vstack)
arr16 = np.array([1, 2, 3])
arr17 = np.array([4, 5, 6])
arr18 = np.vstack((arr16, arr17))
print(arr18)

######################################################JOIN ARRAYS AS HEIGHT(dstack)
arr19 = np.array([111, 222, 333])
arr20 = np.array([444, 555, 666])
arr21 = np.dstack((arr19, arr20))
print(arr21)