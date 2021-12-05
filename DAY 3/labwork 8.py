# Given a n-digit number. Find the sum of its digits.
number = int(input("enter a number"))
sumofdigit = 0
for digit in str(number):
    sumofdigit += int(digit)
print(sumofdigit)