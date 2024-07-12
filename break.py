pa = 5201314
t = False
n = 1
while 1:
    a = int(input("第"+str(n)+"次 請輸入密碼 : "))
    if a!= pa:
        print("密碼輸入錯誤!")
        if n <= 2:
            n += 1
            continue
        else:
            print("---------------")
            print("已密碼錯誤三次，停止登入")
            break
    else:
        print("---------------")
        print("輸入正確，歡迎光臨")
        break