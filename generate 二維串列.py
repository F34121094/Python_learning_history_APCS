A = [0 for x in range(10)]
arr = [A for i in range(5)]
i = 1
for item in arr:
    print(item,end = " ")
    i+=1
    if(i%10 == 0):
        print()