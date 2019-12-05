from array import *

'''

    arrays are not default available in the python.
    for using arrays you need to do the following:
        from array import *

    datatype :
    i --> integer
    f --> float
'''

# create array
a = array('i', [1,2,3,4])
print(type(a))
print(a)


''' add element at end of the array '''
a.append(5)
print(a)


''' count number of times elements occurs on array '''
print(a.count(3))



'''extend array with another array'''
a.extend([6,7,8])
print(a)

''' get the index number of the element'''
print(a.index(6))

'''remove specific index'''
a.pop(5)
print(a)


'''remove last element on the array'''
a.pop()
print(a)


'''reverse the array'''
a.reverse()
print(a)

'''convert the array to list'''
l = a.tolist()
print(a)
print(l)


''' convert array to string in unicode format'''
s = a.tostring()
print(a)
print(s)

'''length of array'''
print(len(a))


'''slicing of array
    arrayname[start:end:stride]'''
print(a[1:5:2])
