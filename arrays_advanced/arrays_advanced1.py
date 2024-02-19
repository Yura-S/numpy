import numpy as np

############################################################################################################################
######################################################CREATING ARRAYS WITH ARRAY(AUTOMATIC ADJUSTS BY COUNT OF ELEMENTS)
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array_split(arr1, 4)
print(arr2[0])
print(arr2[1])
print(arr2[2])

######################################################SAME WITH ARRAYS HAVING MORE DIMESIONS
arr3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr4 = np.array_split(arr3, 2)
print(arr4[0])
print(arr4[1])

######################################################FIND ELEMENT INDEX IN ARRAY
arr5 = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr5 == 4)
print(x)

######################################################FIND EVEN NUMBERS IN ARRAY
arr6 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr6%2 == 0)
print(x)

######################################################SORTING ARRAY(WORKS WITH ALL DATA TYPESS)
arr7 = np.array([3, 2, 0, 1])
print(np.sort(arr7))

arr8 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr8))

arr9 = np.array([True, False, True])
print(np.sort(arr9))

######################################################ALSO WORKS WITH ARRAYS HAVING MORE DIMENSIONS
arr10 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr10))

######################################################FILTERING ARRAY(2 SAME WAYS)
arr11 = np.array([15, 25, 31, 4])
x = [True, False, True, False]
arr12 = arr11[x]
print(arr12)

arr13 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19])
filter_arr = arr13 > 14
arr14 = arr13[filter_arr]
print(filter_arr)
print(arr14)