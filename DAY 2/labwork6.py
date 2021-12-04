# running faster or bus
a = 9
timetaken = (9/25)*60
total = timetaken*20
timetakenA = (1/7)*60
timetakenB= (2/15)*60
timetakenC = (1/7)*60
totaltime = timetakenA+timetakenB+timetakenC
print("the total time taken by bus is : " , total)
print("the total time taken by walkikng : " , totaltime)
if totaltime>total:
    print("walking is faster")
else:
    print("bus is faster")