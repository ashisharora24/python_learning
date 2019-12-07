''' how to zip a file'''

from zipfile import *

f = ZipFile('test.zip','w', ZIP_DEFLATED)
f.write("F3.txt")
f.write('testing_read_file.txt')
f.close()


# # ------------------------------------------------------------------------------


''' how to unzip a file '''

from zipfile import *
z = ZipFile("test.zip",'r')
names = z.namelist()

for file in names:
    f = z.open(file,"r")
    content=f.read()
    WR = open(file,'w')
    WR.write(content.decode())
    WR.close()
    f.close()
