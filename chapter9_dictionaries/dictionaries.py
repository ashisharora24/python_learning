'''
    dictionary handles key:value pair
'''

dict1 = {"a":"ashish", "b":"testing", 1:32, 2:"passed"}




# ------------------------------------------------------------------------------
'''
    accessing values of the dictionary
'''

print(dict1["a"])
print(dict1[1])


# ------------------------------------------------------------------------------
'''
    for loop in dictionary
    there are 2 type of forloop in the dictionary

    1. for key in dictionaryName:
    2. for key, value in dictionaryName.items():
'''

# type 1
for key in dict1:
    print("key : ", key)
    print("value : ", dict1[key])

# type 2:

for key, value in dict1.items():
    print("key : ", key)
    print("value : ", value)


# ------------------------------------------------------------------------------
'''
    length of the dictionary means : number of (key,value) pairs
'''

print("length of the dictionary :", len(dict1))



# ------------------------------------------------------------------------------

'''
    checking membership
    incase of dictionary we can check if the key is a member or not
    we are not able to check the membership of the values
'''

print("a" in dict1)

if "c" in dict1:
    print("found")
else:
    print("not found")


# ------------------------------------------------------------------------------

'''
    clearing data from dictionary
'''

# clear dictionary data
print("dict1 : ", dict1)
dict1.clear()
print("dict1 : ", dict1)


# ------------------------------------------------------------------------------
'''
    copy old dictionary to new dictionary
'''
dict2 = {"a":"ashish", "b":"testing", 1:32, 2:"passed"}
dict3 = dict2.copy()
# for testing we will modify dict1 , and dict2 , the changes should not be
# reflected in th oppposite dictionary
dict2[1]=33
dict3[1]=34
print("dict2 : ", dict2)
print("dict3 : ", dict3)


# ------------------------------------------------------------------------------
'''
    - create dictionary :
    - list is given
    - and final value : this can be string, digit or list, or anything.
        same will be placed as values for all the keys
    - new dictionary is created with list elements as keys and final value as its
        values

'''
keysList = [1,2,3,4]
final_value = ["a","b"]
dict4 = dict.fromkeys(keysList, final_value)
print("dict4 : ", dict4)
# output:
#   dict4 :  {1: ['a', 'b'], 2: ['a', 'b'], 3: ['a', 'b'], 4: ['a', 'b']}
# ------------------------------------------------------------------------------


'''
    get the value from dictionary

    syntax:
        n = dictionaryName.get(key,val1)

    note:
        if the key doesnt exist it will return val1
'''
n = dict4.get(1,"key not found")
print(n)
n = dict4.get(11,"key not found")
print(n)
n = dict4.get(1,['a','b'])
print(n)
n = dict4.get(11,['a','b'])
print(n)


# ------------------------------------------------------------------------------

'''
    dictionary.items()
    returns the object containing the key value pair
'''
check = dict4.items()
print(check)



# ------------------------------------------------------------------------------

'''
    dictionary.keys()

    returns all the keys in a sequence
'''
check = dict4.keys()
print(check)


# ------------------------------------------------------------------------------
'''
    dictionaryName.values()

    returns all the values in the sequence format
'''
check = dict4.values()
print(check)


# ------------------------------------------------------------------------------
'''
    dict_a.update(dict_b)

    update one dictionary to another
'''
dict_a = {1:'a',2:'b',3:'c',4:'d'}
dict_b = {5:'e',6:'f',7:'g',8:'h'}

dict_a.update(dict_b)

print("dict_a : ", dict_a)
print("dict_b : ", dict_b)

# ------------------------------------------------------------------------------

'''
    dictionary.pop(key, return_this_if_not_found)

    note:
        1. if the key is found, then key, value pair will be removed
        2.  it will return the value
'''

check = dict4.pop(4,"not_found")
print("check : ", check)
print("dict4 : ", dict4)

check = dict4.pop(24,"not_found")
print("check : ", check)
print("dict4 : ", dict4)


# ------------------------------------------------------------------------------

'''
    dictionary.setdefault(key,value)

    Note :
        - if the key is found then it will return the value of the key from the
            dict and will not perform any taskabs
        - if key is not found then it will add the key value to it
'''
print("dict4 : " , dict4)
check = dict4.setdefault(3,"testing")
print("check : ", check)
print("dict4 : " , dict4)
check = dict4.setdefault(5,"testing")
print("check : ", check)
print("dict4 : " , dict4)

# ------------------------------------------------------------------------------

'''
    dictionary.update({key:value})

    note:
        - if key is found.
            its value will be updated
        - if key not found
            new key value pair will be added to dictionary
'''

print("dict4 : ", dict4)
dict4.update({3:"ashish"})
print("dict4 : ", dict4)
dict4.update({66:"ashish"})
print("dict4 : ", dict4)

# ------------------------------------------------------------------------------
'''
    convert key list and value list to dictionary
'''
keys_list = [1,2,3,4,5]
value_list = ['a','b','c','d','e']

dict5 = dict(zip(keys_list,value_list))
print(dict5)

# output :
#   {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


# ------------------------------------------------------------------------------
'''
    converting a string to dictionary

    string = 'a=ashish,b=testing,1=32,2=passed'

    import json
    res = json.loads(test_string)
'''

import json
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
print("The original string : " + str(test_string))
res = json.loads(test_string)
print("The converted dictionary : ", res)



# ------------------------------------------------------------------------------
'''
    passing dictionary to function

'''

def test(dict):
    for k,v in dict.items():
        print(k,v)
d = {1:2,3:4,5:6}
test(d)

# ------------------------------------------------------------------------------

'''
    ordered dictionary:

    from collections import OrderedDict
    d = OrderedDict()

'''


from collections import OrderedDict
d = OrderedDict()
d[1]=2
d[2]=3
d[3]=4

for k,v in d.items():
    print(k,v)
