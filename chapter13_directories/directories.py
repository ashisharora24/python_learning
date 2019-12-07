'''
    get current directory path
'''

import os
current = os.getcwd()
print(current)


'''
    create directory
    # gives error if directory already exist
'''
import os
#_ os.mkdir('mysub')
# gives error if directory already exist



# if mysub doesnt exist then mysub2 will not be created
#_ os.mkdir('mysub/mysub2')
# gives error if directory already exist


'''
    create complete directory path
'''
#_ os.makedirs('mysub3/mysub4')
# gives error if directory already exist


'''
    not understood
    change directory
'''
import os
goto = os.chdir('mysub/mysub2')


'''remove directory'''
os.rmdir(mysub)

'''remove complete directory path'''
os.removedirs('mysub3/mysub4')


'''rename directory'''
os.rename('old_name', 'new_name')

'''get directory content'''
os.walk(path,topdown=True,oneerror=None,followlinks=False)

for dirpath, dirname,filenames in os.walk('.'):
    print("current directory : ", dirpath)
    print("directories : ", dirname)
    print("files : ", filenames)
