def triple (x,list):
    for i in range(len(list)):
        list[i] = list[i]*3
    x = x*3
    print("x = "+str(x)+"\tlist = "+str(list))
    print()
x = 10
list = [2, 4, 6]
print("-----呼叫 triple() 前-----")
print("x = "+str(x)+"\tlist = "+str(list))
print()
print("-----執行 triple 函式-----")
triple(x,list)
print("-----呼叫 triple() 後-----")
print("x = "+str(x)+"\tlist = "+str(list))