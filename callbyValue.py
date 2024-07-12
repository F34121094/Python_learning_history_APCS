def triple (x,y):
    x = x*3
    y = y*3
    print("\tx = %d\t\ty = %d" % (x, y))
    print()
x = 10
A = [2, 4, 6]
print("-----呼叫 triple() 前-----")
print("\tx = %d\t\tA[1] = %d"%(x,A[1]))
print()
print("-----執行 triple 函式-----")
triple(x,A[1])
print("-----呼叫 triple() 後-----")
print("\tx = %d\t\tA[1] = %d"%(x,A[1]))
