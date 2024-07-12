data = [["李天德",30000,2000,1200],["許立旺",40000,3000,2400]]
print("姓名 \t底薪 \t加班費\t勞健保費\t實發金額")
for i in range(40):
    print("=",end  = "")
print()

for x in range(2):
    total = 0
    for j in range(4):
        print(data[x][j],end = "\t")
        if(j>0):
            total += data[x][j]
    print(total)
    data[x].append(total)

for i in range(40):
    print("=",end  = "")
print()
print("合計  ",end = "\t")
for y in range(1,len(data[0])):
    tot = 0
    for x in range(len(data)):
        tot += data[x][y]
    print(tot,end="\t")