""" while taking the input values from the users, we have a single syntax:
a = input("How are you")

input is received only in the form of string

once received it can be converted to what we like :

a = int(input("Enter Your age : "))
"""




fullname = input("Enter Your Name : ")
print("You have entered  : {name}".format(name=fullname))

age = int(input("Enter your age : "))

print("age type is : ", type(age))
print("you have entered your age as {age}".format(age=age))
