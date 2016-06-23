import sys
import calendar

day = raw_input().strip().split(' ')
day_week = calendar.weekday(int(day[2]), int(day[0]), int(day[1]))
print calendar.day_name[day_week].upper()


