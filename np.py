import numpy as np

### 1
arr = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
print(arr)
print( arr.ndim )
print( arr.shape )
print( arr.size )
print( arr.dtype )



### 2
print('\n#2')
arr2 = np.array([['a', 'b'], ['c', 'd'], [3, 3]])
print(arr2)
print( arr2.ndim )
print( arr2.shape )
print( arr2.size )
print( arr2.dtype )



### 3
print('\n#3')
arr3 = np.arange(0, 5)
print( arr3 )

arr4 = np.random.rand(5)
print( arr4 )



### 4
print('\n#4')
arr5 = np.zeros((5, 5))
print( arr5 )

arr6 = np.random.rand(5, 5)
print( arr6 )



### 5
print('\n#5')
arr7 = np.ones(20) * 7
new_array = arr7.reshape(4,5)
print(new_array)



### 6
print('\n#6')
arr8 = np.arange(1, 37).reshape(6, 6)
print('Original: ', arr8)
print('only the first element on it: ',  arr8[0,0] )
print('only the last 2 rows for it: ', arr8[4:6,:] )
print( 'only the two mid columns and 2 mid rows for it: ', arr8[2:4,2:4] )
print( 'the sum of values for each column: ',  arr8.sum(0) )