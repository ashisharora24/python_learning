'''
python provides 3 modules:
    1. datetime
    2. time
    3. calendar

datetime module has 4 important classes:
    1. datetime class
        - handles conbination of date and time
        - attributes : year, month, day, hour, minute, seconds, microseconds, and tzinfo
    2. date class
        - handles dates of Gregorian Calendar
        - attributes: year, month and day
    3. time class
        - handles time assuming that everyday has exactly 24*60*60 seconds
        - attributes : hours minutes seconds microseconds and tzinfo
    4. time delta class
        - handles the duration
        - difference between two dates and time or datetime instance
'''

# ------------------------------------------------------------------------------
'''the epoch time : means time duration from 1st Jan 1990'''

import time
epoch = time.time()
print(epoch)
# output : 1575903408.308934

# ------------------------------------------------------------------------------
''' converting epoch to date time '''
t = time.localtime(epoch)
year = t.tm_year          #   2019
month = t.tm_mon          #   12
day = t.tm_mday           #   9
hour = t.tm_hour          #   15
min = t.tm_min            #   20
second = t.tm_sec         #   17
dayInWeek = t.tm_wday     #   0

#print("Current Time : {%d}-%d-%d %d:%:%d"%(day,month,year,hour,min,second))
print("{}-{}-{} {}:{}:{}".format(day,month,year,hour,min,second))
#  OUTPUT : 9-12-2019 20:26:48
# ------------------------------------------------------------------------------
'''
    Date and time NOW

    for current date and time in our computer

    1. ctime() of "time" module
        - direct output as Mon Dec  9 20:28:18 2019
    2. now() of 'datetime' module
        - direct output as 2019-12-09 20:28:18.294130
    3. today() of 'datetime' module
        - direct output as 2019-12-09 20:30:38.989535
    4. date.today() if we need only date
        - direct output as 2019-12-09
'''

import time
t = time.ctime()
print(t)
# output Mon Dec  9 20:28:18 2019

from datetime import *
time = datetime.now()
print(time)
# output as 2019-12-09 20:28:18.294130

print("Current Time : {}-{}-{} {}:{}:{}".format(
    time.day,
    time.month,
    time.year,
    time.hour,
    time.min,
    time.second))


from datetime import *
tdm = datetime.today()
print("tdm : ",tdm)
tdm = date.today()
print(tdm)


# ------------------------------------------------------------------------------
''' how to create date time object from date time variables'''
# combining date and time
# create date time object
from datetime import *

# 1 (No date time feeded)
dt = datetime.now()
print(dt)

# 2 (when u have separate date time object)
d = date(2016,4,29)
t = time(15,30)
dt = datetime.combine(d,t)
print(dt)

# 3 (only date is available)
dt = datetime(year=2016,month=6,day=24)
print(dt)

# 4 (and time time both are avaialable)
dt = datetime(2016,6,24,18,30)
print(dt)

# 5 (passing date and time as defined parameters)
dt = datetime(year=2016,month=6,day=24,hour=15, minute=30,second=10)
print(dt)

# ------------------------------------------------------------------------------
'''replacing parameters'''
dt = datetime(year=2016,month=6,day=24,hour=15, minute=30,second=10)
print(dt)
# output as 2016-06-24 15:30:10
dt = dt.replace(year=2018,day=10)
print(dt)


# ------------------------------------------------------------------------------
'''
    FORMATING OF DATES AND TIME:

    string format
    syntax :
        from datetime import *
        td = date.today()
        str = td.strftime("%d,%B,%y")
    '''
from datetime import *
td = date.today()
str = td.strftime("%d,%B,%y")
print(td.strftime("a : %a"))
print(td.strftime("A : %A"))
print(td.strftime("w : %w"))
print(td.strftime("d : %d"))
print(td.strftime("b : %b"))
print(td.strftime("B : %B"))
print(td.strftime("m : %m"))
print(td.strftime("y : %y"))
print(td.strftime("Y : %Y"))
print(td.strftime("H : %H"))
print(td.strftime("I : %I"))
print(td.strftime("p : %p"))
print(td.strftime("M : %M"))
print(td.strftime("S : %S"))
print(td.strftime("f : %f"))
print(td.strftime("Z : %Z"))
print(td.strftime("j : %j"))
print(td.strftime("U : %U"))
print(td.strftime("W : %W"))
print(td.strftime("c : %c"))
print(td.strftime("x : %x"))
print(td.strftime("X : %X"))

'''
a : Mon                         (day)
A : Monday                      (day)
w : 1                           (week)
d : 09                          date of the month
b : Dec                         month
B : December                    month
m : 12                          month
y : 19                          year
Y : 2019                        year
H : 00                          hour
I : 12                          hour
D : AM                          am or pm
M : 00                          minutes
S : 00                          seconds
f : 000000                      microseconds
Z :                             timezone(empty or utc or est or cst)
j : 343                         day of the year
U : 49                          week of the year (sunday as start day)
W : 49                          week of the year (monday as start day)
c : Mon Dec  9 00:00:00 2019    (appropriate date time representation)
x : 12/09/19                    appropriate date representation
X : 00:00:00                    appropriate time representation
'''



# ------------------------------------------------------------------------------

'''
    Time Difference

d1 = date(y1, m1, d1)
d2 = date(y2, m2, d2)

dt = d1-d2
dt --> this is in days

for weeks : divmod(dt.days, 7)
for months : divmod(dt.days, 30)
'''


t1 = datetime(2018,12,12,15,15,15)
t2 = datetime(2017,6,6,14,14,14)
print(t1)
print(t2)
dt = t1-t2
print(dt)
print("dt.days", dt.days)
print("dt.seconds", dt.seconds)



months, days = divmod(dt.days,30)
print("months, days : ", months, days)

weeks, days = divmod(days,7)
print("weeks, days : ", weeks, days)

hours, secs = divmod(dt.seconds, 3600)
print("hours, seconds : ",hours, secs)

minutes = secs//60
secs = secs%60
print("minutes, seconds : ", minutes, secs)


print("Difference : {} months {} weeks {} days {} hours {} minutes {} seconds".format(
            months,
            weeks,
            days,
            hours,
            minutes,
            secs))



# ------------------------------------------------------------------------------
'''
    FINDING  duration using "time delta"

    time_old + delta_time = new_time
'''
from datetime import *

d1 = datetime(2016,4,29,16,45,0)

delta = timedelta(
                    days=10,
                    seconds=10,
                    minutes=20,
                    hours=12,
                    weeks=2
                )
new_time = d1+delta
print(new_time)


#-------------------------------------------------------------------------------
'''
    comparing 2 dates:
'''
t1 = datetime(2018,12,12,15,15,15)
t2 = datetime(2017,6,6,14,14,14)

if t1==t2:
    print("both same")
elif t1>t2:
    print(t1)
else:
    print(t2)


# ------------------------------------------------------------------------------

'''
    sorting of dates

    sorting is done in list
    add the dates to the list and and then sort them in order
'''



t1 = datetime(2016,1,12,15,15,15)
t2 = datetime(2017,2,6,14,14,14)
t3 = datetime(2018,3,12,15,15,15)
t4 = datetime(2019,4,6,14,14,14)
list = [t4,t2,t3,t1]
list.sort()
print(list)


# ------------------------------------------------------------------------------

'''
    stop the execution temporarily
'''
import time
seconds = 10
time.sleep(seconds)

# ------------------------------------------------------------------------------

'''
    how to find the time taken by a program

    Syntax :
        t1 = perf_counter()
        t2 = perf_counter()
        seconds = t2-t1
'''
from time import *
t1 = perf_counter()
t2 = perf_counter()
print("seconds  : {}".format(t2-t1))


# ------------------------------------------------------------------------------

'''
    check if year is leap year or not
'''
from calendar import *
year = 2016
if(isleap(year)):
    print("its leap year")
else:
    print("its not leap year")
