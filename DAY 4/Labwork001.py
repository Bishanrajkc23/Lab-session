# Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
yrs = int(input("enter a year: "))
p = yrs%4
q = yrs%100
r = yrs%400
while p == 0:
    if (q == 0 and r != 0):
        print("it is common year ",format(yrs))
        break
    else:
        print("it is leap year ",format(yrs) )
        break
else:
    print("it is a Common Year ",format(yrs))

