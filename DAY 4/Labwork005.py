'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''
totalclass = int(input("enter total class: "))
attendclass = int(input("enter attend class: "))
percentageoftanda = (attendclass/totalclass)*100
print(f"Student attended {percentageoftanda}% of classes.")
if percentageoftanda<75:
    print(f"Sorry,You aren't allowed to sit in exam.")
else:
    print(f"Congratulations! You are allowed to sit in exam.")
