# Given the integer N - the number of minutes that is passed since midnight
time_spend_min = int(input("enter minute passed: "))
time_spend_hr = 0
time_rem_min = 0
if time_spend_min > 60:
    time_spend_hr = time_spend_min / 60
    time_rem_min = time_spend_min % 60
if time_spend_hr > 24:
    time_spend_hr = time_passed_hr - 24

print("The time spend after midnight is ", int(time_spend_hr), ":", int(time_rem_min))

num = int(input("enter the time"))
hour = int(num/60)
min = (num%60)
print(f"the hours is {hour}")
print(f"the minute is{min}")