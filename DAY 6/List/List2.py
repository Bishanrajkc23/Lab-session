#Write a Python program to multiplies all the items in a list.
list =[1,2,3,4,5,6,7,8,9]
b = list[0]
multi = 1
for i in range(1 , len(list)):
    b = list[i]
    multi = b * multi
    print(multi)