import datetime
import time
import calendar

dt=datetime.date.today()
print("current date and time: ",datetime.datetime.now())
print("current date:",dt)
print("current week day name:",dt.strftime('%A'))
print("current week day number:",dt.strftime('%w'))
print("current month name:",dt.strftime('%B'))
print("current month number:",dt.strftime('%m'))
print("current day of the month:",dt.strftime('%d'))
print("current year:",dt.strftime('%Y'))
print("current day of the year:",dt.strftime('%j'))
print("week number of the year:",dt.strftime('%W'))

print("\nDisplay current calender:")
calendar.setfirstweekday(calendar.SUNDAY)
year=int(dt.year)
month=int(dt.month)
cal=calendar.monthcalendar(year,month)

print(" ______________________")
print("|_______ %s-%s _______|"%(month,year))
print("| Su Mo Tu We Th Fr Sa |")
for i in cal:
    line="|"
    for j in i:
        if(j==0):
            line+="   "
        elif(len(str(j))==1):
            line+="  %d"%j
        else:
            line+=" %d"%j
    line+=" |"
    print(line)
print("|______________________|")