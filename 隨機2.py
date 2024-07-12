import random as r
arr = [x for x in range(1,50)]
a = r.sample(arr,6)
#sample從一串裡面取不重複的n個字
for i in range(len(a)):
    num = i+1
    print("第 %d 個亂數 : "%num,end = "")
    print(a[i])
