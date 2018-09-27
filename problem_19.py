# Problem_19
# Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

month = {
    1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30,
    10 : 31, 11 : 30, 12 : 31
}
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

answer = 0
year = 1900
day_count = 0
while year < 2001:
    month[2] = 28
    for mon in range(1, 13):
        if year != 1900 and year % 4 == 0 and mon == 2:
            month[mon] = 29
        for date in range(1, month[mon]+1):
            if year >= 1901 and date == 1 and day[day_count] == 'Sun':
                answer += 1
            day_count += 1
            if day_count == 7:
                day_count = 0
    year += 1

print(answer)

# Datetime 활용 
import datetime

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
mydict = {}
for i in range(1901,2001):
    for j in range(1,13):
        x = days[datetime.date(i,j,1).weekday()]
        if (x in mydict):
            mydict[x] += 1
        else:
            mydict[x] = 1
print(mydict["Sun"])
