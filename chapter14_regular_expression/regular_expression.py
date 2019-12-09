'''METHOD 1 (long way)'''

import re
prog = re.compile(r'm\w\w')
str = 'cat mat bat rat'
result = prog.search(str)
print(result.group())

# ------------------------------------------------------------------------------
'''METHOD 2 (shortway)'''
import re
str = 'man sun map run'
result = re.search(r'm\w\w',str)
print(result)
if result:
    print(result.group())

# ------------------------------------------------------------------------------
'''METHOD 3: findall() prints all matching values in list format'''
import re
str = 'man sun map run'
result = re.findall(r'm\w\w',str)
print(result)
# OUTPUT
#   ['man', 'map']

# ------------------------------------------------------------------------------
'''method 4 : match'''
import re
str = 'man sun map run'
result = re.match(r'm\w\w',str)
print(result.group())

# ------------------------------------------------------------------------------
'''method 5 : split
    returns list of matached'''
import re
str = 'man sun map run'
result = re.split(r'm\w+',str)
print(result)

# ------------------------------------------------------------------------------
'''method 6 : replace
    syntax:
        sub(regular_expression, new_string, string)
'''

import re
str = 'man sun map run'
result = re.sub(r'map','women',str)
print(result)
# ------------------------------------------------------------------------------
