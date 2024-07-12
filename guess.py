ans = 57
p = False
top = 100
base = 0
while(p == False):
    a = int(input("請從"+str(base)+"~"+str(top)+"中猜一個整數 : "))
    if a == ans:
        print("恭喜猜中了")
        p =True
    elif(a < ans):
        print("太小了，再猜大一點")
        base = a
    else:
        print("太大了，再猜小一點")
        top = a

