'''numpy arrays are called n dimensional arrays  where n=dimension'''

import numpy as np

# 1 demensional
arr = np.array([1,2,3])
print(arr)

# 2 demensional
arr = np.array([[1,2,3],[4,5,6]])
print(arr)



'''creating numpy array while declaring the datatype'''
arr = np.array([1,2,3], int)
print(arr)



'''
    numpy array as linspace
    creates array with evenly spaced points
    syntax :  array = numpy.lispace(start, end, n)
'''
arr = np.linspace(1,10,2)
print(arr)
arr = np.linspace(0,10,5)
print(arr)



''' numpy with logspace
    evenly spaces points on a logaithmically spaced scale
    syntax : numpy.logspace(start, end, n)
    '''

arr = np.logspace(1,10,2)
print(arr)


'''numpy with arange,
    works same as range
    syntax : numpy.arange(start,end,stepsize)
    '''
arr = np.arange(1,10,2)
print(arr)

''' create numpy with zeros
    syntax : numpy.zeros(n,datatype)
    datatype : int or float
    '''
arr = np.zeros(10, int)
print(arr)
arr = np.zeros(10, float)
print(arr)

''' create array with ones
    syntax : numpy.ones(n, datatype)
    datatype : int or float
'''
arr = np.ones(10, int)
print(arr)
arr = np.ones(10, float)
print(arr)


''' OPERATORS
    mathematical operators work on numpy'''
a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.array([11,12,13,14,15,16,17,18,19,20])
c = a+b
print(c)
c = a-b
print(c)
c = a/b
print(c)
c = a*b
print(c)

''' more operators'''
print(np.sin(c))
print(np.cos(c))
print(np.tan(c))
print(np.arcsin(c))
print(np.arccos(c))
print(np.arctan(c))
print(np.log(c))

# absolut value
print(np.abs(c))
print(np.sqrt(c))
#print(np.pow(c,2))
print(np.exp(c))

#sum of all the elements of array
print(np.sum(c))
# prod of all elements of the array
print(np.prod(c))
# returns smallest element
print(np.min(c))
# returns largest element
print(np.max(c))
# returns avaerage of all the elements
print(np.mean(c))
# returns the median values (center value of the array when its in sorted format)
print(np.median(c))
# returns the variance
print(np.var(c))
# returns the convariance
print(np.cov(c))
# returns standard deviation
print(np.std(c))
# returns the index of min values of the array
print(np.argmin(c))
# returns the index of max values of the array
print(np.argmax(c))
# returns unique elements on the array in list format
print(np.unique(c))
# returns the array in sorted format
print(np.sort(c))




'''COMPARING THE ARRAYS:
    when the arrays are compared the output is in True False format
'''
a = np.array([1,2,3,4,5,6,7,8,9,10])
a = np.array([11,2,13,4,15,6,17,8,19,10])
c = a==b
print(c)
# output : [ True False  True False  True False  True False  True False]

c = a>b
print(c)

c = a>=b
print(c)

c = a<b
print(c)

c = a<=b
print(c)

c = a!=b
print(c)





''' where clause
    if we have a condition which we need to check on every element of the array.
    if condition is meant true. then  expression of true is printed
    else false expression is printed

    syntax :  a = where(condition, true_expression, false_expression)
'''

a = np.array([1,2,3,4,5,-6,-7,-8,-9,-10])
from numpy import where
c = where(  a>=1,
            "found",
            "not_found")
print(c)
# output:
# ['found' 'found' 'found' 'found' 'found' 'not_found' 'not_found'
# 'not_found' 'not_found' 'not_found']




'''
    shallow copy:
    syntax : b = a.view()
    which means that when b is modified, a will also be updated
'''
from numpy import *
a = np.arange(1,10,2)
b = a.view()
print(a)
print(b)
b[2]=10
print(a)
print(b)



'''
    deep copy:
    syntax : b = a.copy()
    means when b is modified , a is not effect
'''
from numpy import *
a = np.arange(1,10,2)
b = a.copy()
b[2]=10
print(a)
print(b)


'''FIND DIMENSIONS
    syntax : arr.ndim
'''
arr = array([1,2,3,4])
print(arr.ndim)
arr = array([[1,2,3,4],[5,6,7,8]])
print(arr.ndim)


'''
    shape
    syntax : arr.shape
    will give the exact shape (row, column)
'''
a = array([[1,2,3],[4,5,6]])
print(a.shape)
# output : (2,3)
# 2 rows and 3 columns


'''
    total number of elements in array
    syntax : arr.size
'''
a = array([[1,2,3],[4,5,6]])
print(a.size)


'''
    total itemsize of the array in bytes
    syntax : arr.itemsize
'''
arr = array([[1,2,3],[4,5,6]])
print(arr.itemsize)


'''
    datatype
    synatx : arr.dtype
'''
a = array([[1,2,3],[4,5,6]])
print(a.dtype)


''' reshape the dimensions of the array
    syntax :
        arr.reshape(rows, columns)

        in reshape new array is created and reshaped structure and old array remains same
'''
arr = array([1,2,3,4,5,6,7,8,9,10])
arr1 = arr.reshape(2,5)
print(arr1)
print(arr)



''' flatten the multi-dimensional array
    syntax :
        arr.flatten()
'''
arr = array([[1,2,3,4,5],[6,7,8,9,10]])
arr1 = arr.flatten()
print(arr1)


'''
    ones,zeros, eye for multi dimensions
    np.ones((r,c),int))
    np.zeros((r,c),int))
    np.eye(r))

        int or float
'''

print(np.ones((2,3),int))
print(np.zeros((2,3),int))
print(np.eye(3))


''' slicing
    syntax :
            array[start:end:stepwise , start:end:stepwise]
            array[row_start:row_end:row_stepwise , col_start:col_end:col_stepwise]
'''
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr[1:3,2:4])


''' get diagonal value of the matrix
    syntax : diagonal(arr)
     1  2  3  4
     5  6  7  8
     9 10 11 12
    13 14 15 16

    answer is [1,6,11,16]
'''
print(diagonal(arr))






''' TRANSPOSE:
    syntax :
        arr.transpose()
'''
t = arr.transpose()
print(t)



'''
    random number generator'''

# random number generated as single element
print(random.rand())

# random.rand(row, column)

print(random.rand(5))
print(random.rand(5,2))
