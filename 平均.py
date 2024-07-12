def avr(a,b):
    return (a+b)/2

a = eval(input("輸入第 1 個整數 : "))
b = eval(input("輸入第 2 個整數 : "))
ans = avr(a,b)
print("%d 和 %d 兩整數的平均為 : %.2f"%(a,b,ans))
