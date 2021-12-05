# WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
m = int(input("enter the math marks? :"))
s = int(input("enter the science marks? :"))
e = int(input("enter the english marks? :"))
n = int(input("enter the nepali marks? :"))
total=m+s+e+n
print("The total marks is :")
percentage = (total/400)*100
if percentage > 70 and percentage <= 100:
    print ("distinction")
elif percentage > 60 and percentage <= 70:
    print ("1division")
elif percentage > 40 and percentage <= 60:
    print ("2division")
else:
    print ("fail")



