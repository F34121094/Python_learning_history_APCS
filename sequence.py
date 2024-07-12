a = int(input("請輸入等差數列的首項 : "))
d = int(input("請輸入等差數列的公差 : "))
b = int(input("請輸入等差數列的末項 : "))
n = 0
total = 0
for i in range(a,b+1,d):
    n += 1
    total += i
print("等差數列的項數為 %d"%n)
print("等差數列的總和為 %d"%total)