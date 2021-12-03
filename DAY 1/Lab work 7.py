list = [1,2,3,4,5,6,7,8,9,10]
odd=int(0)

for a in range(1, 10):
    if list[a] % 2 != 0:
        odd = odd + list[a]
print("The sum of odd number is: ", odd)

list = [1,2,3,4,5,6,7,8,9,10]
even=int(0)

for a in range(0, 10):
    if list[a] % 2 == 0:
        even = even + list[a]
print("The sum of odd number is: ", even)


