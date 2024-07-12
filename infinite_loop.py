while 1:
    a = eval(input("請輸入第1個整數 : "))
    b = eval(input("請輸入第2個整數 : "))
    ans = a*b
    while 1:
        type = eval(input(str(a)+" * "+str(b)+" = "))
        if(type == ans):
            print("對了，恭喜")
            break
        else:
            print("錯了，再來一次")
            continue
    ys = input("是否繼續(Y/N) : ")
    if(ys == "Y" or ys == "y"):
        continue
    else:
        break