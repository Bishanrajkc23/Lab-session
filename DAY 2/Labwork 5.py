# number of bench and students
q = int(input("enter the student in one class"))
w = int(input("enter the student in two class"))
e = int(input("enter the student in three class"))

# 1 bench = 2 student
qw = int(q/2)
qqw = int(q%qw)
q_bench = qw+qqw

ww = int(w/2)
www = int(w%ww)
w_bench = ww+www

we = int(e/2)
eew = int(e%ew)
e_bench = ew+eww

total_bench = one_bench + two_bench + three_bench

print(f"Total number of bench needed is {total_bench}")