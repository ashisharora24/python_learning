"""is operator is used for checking the memory address of 2 variables are same or not.
if the address of the memory is same then it returning True else False

in order to check the addess of the memory for any variable. we do
id(variable)
"""

a = 10
b = a
if b is a:
    print(True)
else:
    print(False)

print(id(a))
print(id(b))
