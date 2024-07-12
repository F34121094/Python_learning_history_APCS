num = int(input("請輸入里程數 : "))
ys = input("是否為連續假期(y/n) : ")
print("里程數 :　%d"%num,end = '')
total = 0
if(ys == 'n'):
    if(num <= 20):
        print("免費")
    elif(num > 20 and num <= 200):
        total += 1.2*(num-20)
        print(" 收費 : %.2f"%total)
    else:
        total += (num-200)*0.9
        num -= (num-200)
        total += (num-20)*1.2
        print(" 收費 : %.2f"%total)
if(ys == 'y'):
    total += num*1.2
    print(" 收費 : %.2f"%total)