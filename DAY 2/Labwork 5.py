# number of bench and students
one = int(input("enter the student in one class"))
two = int(input("enter the student in two class"))
three = int(input("enter the student in three class"))

# 1 bench = 2 student
onetwo = int(one/2)
oneonetwo = int(one%onetwo)
one_bench = onetwo+oneonetwo

twotwo = int(two/2)
twotwotwo = int(two%twotwo)
two_bench = twotwo+twotwotwo

twothree = int(three/2)
threetwotwo = int(three%threetwo)
three_bench = threetwo+threetwotwo

total_bench = one_bench + two_bench + three_bench

print(f"Total number of bench needed is {total_bench}")