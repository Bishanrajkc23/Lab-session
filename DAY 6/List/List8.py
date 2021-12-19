#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
list=['apple','ball','cat','dog','elephant','fish','goat']
for i in list:
    if i!=list[0] and i!=list[4] and i!=list[5]:
        print(i)