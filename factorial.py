a = eval(input("請輸入1~10的整數 : "))
total = 1
for i in range(1,a+1):
    total *= i
    if i < a:
        print(i, end=" * ")
    else:
        print(i, end = " = ")

print(total)