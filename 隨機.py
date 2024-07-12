import random as r
for i in range(5):
    num = i + 1
    print("第 %d 個亂數 : "%num,end = "")
    print(r.randint(1,10)) #就真的是1~10
