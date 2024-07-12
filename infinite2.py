#設計 2x <= m運算式
a = int(input("請輸入正整數m : "))
ans = 0
while (2**ans <= a ):
    ans+=1
ans -= 1
print("x = %d"%ans)
print("2^"+str(ans)+" = "+str(2**ans)+" <= "+str(a))