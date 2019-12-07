'''list vs array

  list: can have elements on any datatype (mixer)
  array : all elements in arrays are of same datatype

'''

a = []
print(a)


a = [10,20,30,'as','b']
print(a)


'''
    creating list from  range
'''
a = list(range(1,10,2))
print(a)



''' how to add elements to list'''
a.append("ashish")


'''slicing'''
print(a[1:10:2])


'''concaatenation of list'''
a = [1,2,3,4,5]
b = ['a','b','c','d','e']
c = a+b
print(c)


'''repetition'''
print(c*2)


'''membership in list'''
print("a" in a)
# output : True or False


list = [1,2,3,4,5,'a','b','c','d','e']
print(list.index('a'))
# returns the index number of the element of found and if not found it returns error

list.insert(5,6)
print(list)
# inserts element "6" at the index 5

new_list = list.copy()
# copys the list to new list
# no relation in both after creation

new_list.extend(list)
# adds list elements to new_list

list.count("a")
# returns the number of occurance of element "a" on the list
# if element is not found then value 0 is returned

list.remove('a')
# removes the element a from list
# removes only the first occurence element of the list
# looks from left to right

last_element = list.pop()
# removes the last element of the list

#list.sort()
# list is sorted in the ascending order

list.reverse()
# reverse the order of the elements

list.clear()
# clears all the elements of the list


# n1 = max(list)
# n2 = min(list)


# ------------------------------------------------------------------------------
'''finding common elements in between 2 list'''
l1 = [1,2,7,6,5,1,2]
l2 = [5,6,7,8,9,5,5]

# change element to set() to get unique elements
s1 = set(l1)
s2 = set(l2)

# get intersection elements
s3 = s1.intersection(s2)
print(s3)
# common_elements = list(s3)
# print(common_elements)



# ------------------------------------------------------------------------------
list = [x for x in range(1,10,1) if x%2==0]
print(list)
