"""there are mupltiple ways of doing output string:

    print('ashish\tarora')   --> ashish  arora
    print("ashish\tarora")   --> ashish  arora
    print(r'ashish\tarora')  --> ashish\tarora

    """
print('ashish\tarora')
print("ashish\tarora")
print(r'ashish\tarora')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

""" for catenation we use + file """

a = "ashish"
b= "arora"
print(a+b)

""" during concatenation there is no extra space added around +
but if we do the same with comma it will add extra space"""

a = "ashish"
b= "arora"
print(a,b)


"""
    how to remove this extra space from the comma --> sep = ""
"""

a = "ashish"
b= "arora"
print(a,b,sep="_")

""" after every print statement the is a default newline character added to it """

print(a)
print(b)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

""" removing or replacing the newline character from end of the string"""

print(a, b, sep="@")

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
"""
formating the string for variables . make this as habit.
"""
a = "ashish"
b = "arora"

# way 1
print("Firstname : {}, Last name :{}".format(a,b))
# way 2
print("Firstname : {0}, Last name :{1}".format(a,b))

# way 3
print("Firstname : {firstname}, Last name :{lastname}".format(firstname=a,lastname=b))
# way 3 advantage
print("Firstname : {firstname}, Last name :{lastname}".format(lastname=b, firstname=a))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

""" another way to do formating is :

    example  :
        print("FirstName : %20s, LastName : %20s"%(a,b))

        %s --> string
        %f --> float
        %i --> decimal and integers
        %20s--> 20 spaces inserted before s string
        %-20s--> 20 spaces inserted after s string
"""
print("FirstName : %s, LastName : %s."%(a,b))
print("FirstName : %20s, LastName : %20s."%(a,b))
print("FirstName : %-20s, LastName : %-20s."%(a,b))
