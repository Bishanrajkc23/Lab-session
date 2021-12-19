#write a Python Program that accepts a string and calculate number of digits and letters
a = str(input("enter any number"))

d= 0

l =0

for i in a:

    if i.isdigit():

        d=d+1

    elif i.isalpha():

        l=l+1

    else:

        pass



print("letter",l)

print("digit",d)