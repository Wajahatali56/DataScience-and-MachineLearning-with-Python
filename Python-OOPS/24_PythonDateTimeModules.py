# reference website : strftime.org
import datetime
x = datetime.datetime.now()
print(x)

# 2023-08-08 09:24:14.368691
# This will return the year and name of weekday

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) # %A return current weekday name

# Creating the date object - you can use datetime() for creating the date.

import datetime
x = datetime.datetime(2023 , 8 , 16)
print(x)

import datetime
x = datetime.datetime(2023 , 8 , 16 ,hour= 12, minute= 10 , second= 2 , microsecond= 234233)
print(x)

# The strftime() method

import datetime
x = datetime.datetime(2023 , 8 , 16)
print(x.strftime("%B")) # %B returns current month name according to given date

# A reference of all the legal format datetime code
'''
%a - return weekday name in short - wed
%A - return weekday name in full - wednesday
%w - return weekday(wednesday) name as a number - 3 / Monday is at index_1 so far 
%d - return days 1-31 - 31
%b - return Month name in short - Dec
%B - return Month name in full - December
%m - return Month as number - 12(december)
%y - return year short - 23 (2023)
%Y - return year full - 2023
%H - return hour24 - 17(suppose 5am)
%I - return hour12 - 5am
%p - am/pm - PM
%M - minute - 41
%S - second - 30
%f - microsecond 000000 - 999999 -(647888)
%Z - timezone - CST
%j - daynumber of year - 365
%U - week number - 52
%C - century - 2000 / 20*
%x - local version of date - 05/15/2023

'''


#__________________BEST OF LUCK ____________________#