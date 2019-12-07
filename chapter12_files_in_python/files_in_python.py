'''
    file_hanlder = open("filename","open_mode","buffering")

w   :   1. write data to file
    :   2. if data already present, then it will be deleted
    :   3. new data will be written

r   :   1. read data from file
    :   2. pointer is positioned at the start of the file

a   :   1. append data to file
    :   2. file pointer placed at end of the file

w+  :   1. to write and read file
    :   2. previous data not deleted

r+  :   1. read and write data to file
    :   2. pointer at begining
    :   3. new data will be written

a+  :   1. append and read
    :   2. pointer will be at end
    :   3. file created if not exist

x   :   1. open file in exculusive creation mode
        2. file creation fails if file exist already
'''

# ------------------------------------------------------------------------------
'''create file object'''
# read file
F = open("testing_read_file.txt", "r")
F.close()

# ------------------------------------------------------------------------------
'''
    read compete file
'''
# now you can read complete file at once
F1 = open("testing_read_file.txt", "r")
str = F1.read()
print(str)
F1.close()

# ------------------------------------------------------------------------------
'''
    read file line by line
'''
# we can read file line by line
F2 = open("testing_read_file.txt", "r")
list = F2.readlines()
print(list)
F2.close()

# ------------------------------------------------------------------------------
'''
    write data to file
'''
# write data to file
F3 = open("F3.txt", "w")
F3.write("How are you\n")
F3.write("this is ashish")
F3.close()

# ------------------------------------------------------------------------------
'''
    read and write data to file
'''
# append data to existing file
F4 = open("F3.txt", "a+")
# write function will only be writing files at the end of the file
F4.write("ASHISH AROA")

# with seek function we can change the location of the pointer only for the
# reading of the file. not for the writing
F4.seek(0,0)
print("fourth try : ", F4.read())
# Object.seek(offset, fromwhere)
#               offset means bytes from the start position
#   fromwhere have 3 values: 0,1,2
#                            0 --> start of file
#                            1 --> current position in file
#                            2 --> end of file
F4.close()
# ------------------------------------------------------------------------------


''' know if file exist or not'''

import os
filename = "F3.txt"
if os.path.isfile(filename):
    print("found")
else:
    print("notfile")

# ------------------------------------------------------------------------------
'''
    with statement
    advantage of by "with" that we dont need to close the file object
'''
with open("F3.txt","a+") as F5:
    F5.write("\nthis is from with statement")
    F5.seek(0,0)
    print("from with statement block : ", F5.read())


# ------------------------------------------------------------------------------
''' working with binary
w   ->  wb
r   ->  rb
a   ->  ab
w+  ->  wb+
r+  ->  rb+
a+  ->  ab+
x   ->  xb
'''


# ------------------------------------------------------------------------------
'''
    converting string to binary
    and
    converting binary to string
'''
str = "ashish arora"
bny = str.encode()
print(bny)
str = bny.decode()
print(str)
