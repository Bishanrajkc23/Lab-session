#Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero.
a = int(input("enter one integers: "))
b = int(input("enter two integers: "))
c = int(input("enter three integers: "))
if (a != b and b != c and c !=a ):
    sum = a + b + c
    print("sum of the number ",format(sum))
else:
    print("two or more than more number is equal and sum=0 ")
