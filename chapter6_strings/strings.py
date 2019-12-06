'''there are 4 ways to handle string,
    and when we say handle we mean by single quote double and all abs
'''
a1 = 'ashish arora'
a2 = "ashish arora"
a3 = '''ashish
        arora'''
a4 = """ashish
        arora"""
a5 = r'ashish \ arora'

print("a1 : ", a1)
print("a2 : ", a2)
print("a3 : ", a3)
print("a4 : ", a4)
print("a5 : ",a5)

# OUTPUT
# a1 :  ashish arora
# a2 :  ashish arora
# a3 :  ashish
#         arora
# a4 :  ashish
#         arora
# a5 :  ashish \ arora


# ------------------------------------------------------------------------------

''' ESCPAE CHARACTERS'''
    # ESCAPE CHARACTERS
    # \a  :   bell or alert
    # \b  :   backspace
    # \n  :   newline
    # \t  :   horizontal tab space
    # \v  :   vertial tab space
    # \r  :   Enter Button
    # \x  :   character x
    # \\  :   display single \
print("bell or alert: \a")
print("backspace: \b")
print("newline: \n")
print("horizontal tab space: \t")
print("vertial tab space: \v")
print("Enter Button: \r")
print("display single slash: \\")


# ------------------------------------------------------------------------------
''' create a string by unicode'''
a = u'\u0915\u094b\u0930'
print(a)


# ------------------------------------------------------------------------------
'''length of string'''
a = "ashish arora"
print(len(a))


# ------------------------------------------------------------------------------
'''
    slicing in strings
    stringName[start:stop:stepsize]
'''
a = "ashish arora"
print(a[1:6:2])

# ------------------------------------------------------------------------------
''' repeating the strings'''
print("abc"*3)


# ------------------------------------------------------------------------------
''' concatenation in string
    concatenation doesnot add any extra spaces
'''

a,b = "ashish", "arora"
c = a+b
print(c)


# ------------------------------------------------------------------------------
'''checking membership
    returns True or False'''
a = "ashish arora"
b = 'sh'
if b in a:
    print("found")
else:
    print("not found")

c = b in a
print(c)

# ------------------------------------------------------------------------------
'''
    comparing 2 or more strings
    comparsion happens on the basis of the english dictionary order
    comparsion operators:
    >,>=,<,=<,==,!=
'''
a = "ashish"
b = "ASHISH"
if a==b:
    print("same")
else:
    print("different")

# ------------------------------------------------------------------------------
'''
removing the extra spaces from the strings
this can be removed from
string.lstrip() : left side of string,
string.rstrip() : right side of the string
string.strip()  : both sides of the string
'''
a = " ashish arora "
print(a.strip())
a = " ashish arora "
print(a.rstrip())
print(a.lstrip())


# ------------------------------------------------------------------------------
''' find in strings
    front search :
        find()      : gives index number or -1 if not found
        index()     : gives index number or error if not found
    backward search:
        rfind()     : gives index number or -1 if not found
        rindex()    : gives index number or error if not found

    syntax :
        result = mainString.find(substring, startIndex, endIndex)
        result = mainString.index(substring, startIndex, endIndex)
        result = mainString.rfind(substring, startIndex, endIndex)
        result = mainString.rindex(substring, startIndex, endIndex)
'''
main_string = "ashish arora how are you"
sub_string = "aro1ra"
result = main_string.find(sub_string)
print(result)



# ------------------------------------------------------------------------------
''' count the number of occurence of substring in string
    syntax:
        result = mainString.count(substring)

        result gives zero if not found
'''
mainString = "ashish"
subString = "is"
print(mainString.count(subString))


# ------------------------------------------------------------------------------
''' string are immutiable
    means :
    string = "ashish"
    string[0]="U"

    this is not possible
'''

# ------------------------------------------------------------------------------
'''replacing text in the string
    syntax :
        newString = mainString.replace(oldtext, newtext)
'''
mainString = "ashsih"
old_text='si'
new_text='is'
newString = mainString.replace(old_text, new_text)
print(newString)


#-------------------------------------------------------------------------------
''' spliting of the string
    syntax :
        list = string.split(split_text)

        default the spliting_text is " " (one space)
'''
mainString = "ashish arora"
print(mainString.split())


#-------------------------------------------------------------------------------
''' join list to make a string
    list = ['a','b','c','d']

    syntax :
        string = "joining_sring".join(list)
'''
list1 = ['a','b','c','d']
string = "-".join(list1)
print(string)

#-------------------------------------------------------------------------------
'''
    changing the case senetivity of the string
    mainString.upper() : make all upper
    mainString.lower() : make all lower
    mainString.title() : make all Camel Case
'''
mainString = "ashish arora"
newString = mainString.upper()
print(newString)

mainString = "ASHISH ARORA"
newString = mainString.lower()
print(newString)

mainString = "ASHISH ARORA"
newString = mainString.title()
print(newString)


#-------------------------------------------------------------------------------
'''
    checking starting and ending of the string

    syntax:
        result = mainString.startswith(substring)
        result = mainString.endswith(substring)

    returns : True and False
'''
mainString = 'ashish arora'
substring = 'a'
result = mainString.startswith(substring)
print(result)
result = mainString.endswith(substring)
print(result)


#-------------------------------------------------------------------------------
''' string testing methods:
    syntax :
        result = mainString.isalnum()   :   checks alphabets and characters
        result = mainString.isalpha()   :   checks for alphabets
        result = mainString.isdigit()   :   checks for digits
        result = mainString.islower()   :   checks for lower case
        result = mainString.isupper()   :   checks for upper case
        result = mainString.istitle()   :   checks for title or camelcase
        result = mainString.isspace()   :   checks for spaces

        result is in True or False
'''
mainString = "Ashish Arora 123"
result = mainString.isalnum()
print(result)
result = mainString.isalpha()
print(result)
result = mainString.isdigit()
print(result)
result = mainString.islower()
print(result)
result = mainString.isupper()
print(result)
result = mainString.istitle()
print(result)
result = mainString.isspace()
print(result)

#-------------------------------------------------------------------------------
''' formating of strings
    3 ways :
        string = "My name is {}. My age is {}".format(name,age)
        string = "My name is {0}. My age is {1}".format(name,age)
        string = "My name is {fullname}. My age is {agenow}".format( fullname=age, agenow=age)
'''
name = "ashish arora"
age = 33
string = "My name is {}. My age is {}".format(name,age)
string = "My name is {0}. My age is {1}".format(name,age)
string = "My name is {fullname}. My age is {agenow}".format( fullname=age, agenow=age)


#-------------------------------------------------------------------------------
'''formatting contains 3 datatypes
    d   :   decimals
    i   :   integers
    c   :   character
    s   :   string
    f   :   floating

    also:
        {:*>15d}    :   means   :   *************32
        {:*^15d}    :   means   :   ******32*******
        {:*<15d}    :   means   :   32*************
'''
age=32
string = "{:*>15d}".format(age)
print(string)
string = "{:*^15d}".format(age)
print(string)
string = "{:*<15d}".format(age)
print(string)



#-------------------------------------------------------------------------------
'''
    sorting of the strings:

        doesnt modify the mainString : sorted()

    syntax :
        list = Sorted(mainString)
'''

result = sorted(mainString)
print(mainString)
print(result)
