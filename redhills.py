def month_days(month): 
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    else:
        return 28
    
cycle_length=28

print("                  ____________")
print("Your sister from |Red Hills Rd|")
print("                  ------------")
print("                       | |")
print("                       | |")
print("                       | |")
print("                       | |")

last_period_month=int(input("Enter the month of your last visit (1-12): "))
last_period_day=int(input("Enter the day of your last visit (1-31): "))
period_duration=int(input("Enter the visit duration: "))

next_period_day= last_period_day+cycle_length
next_period_month= last_period_month

#month overflow
while next_period_day > month_days(next_period_month):
    next_period_day -= month_days(next_period_month)
    next_period_month +=1
    if next_period_month > 12:
        next_period_month = 1

print(f"You can expect your next period on: {next_period_month}/{next_period_day}")

from datetime import datetime

today = datetime.now()
period_end= next_period_day + period_duration -1

if today.month == next_period_month:
    if next_period_day <= today.day <= period_end:
        print("You are currently on your period.")
elif today.month == next_period_month + 1 and next_period_day> period_end:
    if today.day <= period_end:
        print("You are currently on your period.")
elif next_period_month == 12 and today.month ==1:
    if today.day <= period_end:
        print("You are currently on your period.")
