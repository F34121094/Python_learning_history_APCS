a = eval(input("請輸入行駛的公里數 : "))
price = 80
a -= 1.5
while(a > 0):
    a -= 0.25
    price += 5
print("車資 = %d"%price)