x,y = 4,0
print("x = 4, y= 0")
print("進行x / y計算")
print("----------------")
try:
    ans = x / y
except Exception as e:
    print("錯誤類型 : ",end="")
    print(e)
else:
    print(f'{x}/{y} = {ans}')
finally:
    print("finally敘述區段")
print("----------------")
x, y = 8, 2
print("x = 8, y= 2")
print("進行x / y計算")
print("----------------")
try:
    ans = x / y
except Exception as e:
    print("錯誤類型 : ", end="")
    print(e)
else:
    print(f'{x}/{y} = {ans}')
finally:
    print("finally敘述區段")
