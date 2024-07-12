i,j = 10,20
r1 = 'a'>'z'
r2 = i*6 <= j*3
r3 = i and (j*3)
#在python中 若第一個值為真，將返回第二個操作數，否則返回第一個操作數
r4 = (i < 0) or (i > 100)
print("以字串顯示")
print("r1 = %s"%r1)
print("r2 = %s"%r2)
print("r3 = %s"%r3)
print("r4 = %s"%r4)

print("以整數顯示")
print("r1 = %d"%r1)
print("r2 = %d"%r2)
print("r3 = %d"%r3)
print("r4 = %d"%r4)