a = [4,-15,20,13,-6]
time = 1
print("排  序  前  : ",end = "")
for b in range(len(a)):
    print("a["+str(b)+"] = "+str(a[b]),end="\t")
print()
for i in range(len(a),0,-1): #5 4 3 2
    for j in range(i-1): # 0 1 2 3 4
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
    print("第 %d 次排序 : "%time,end = "")
    time += 1
    for x in range(len(a)):
        print("a[" + str(x) + "] = " + str(a[x]), end="\t")
    print()

