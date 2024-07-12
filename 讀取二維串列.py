arr = [[1,3,5,7],[22,66,44,88],[-3,-9,-5,-6]]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print("arr["+str(i)+"]["+str(j)+"] = "+str(arr[int(i)][int(j)]),end = '\t ')
    print()