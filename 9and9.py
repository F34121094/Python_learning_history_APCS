print(" |\t 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9")
for i in range(40):
    print("=",end = "")
print()
for a in  range(1,10):
    print(a,end=" ")
    print("|",end="")
    for b in range(1,10):
        print("\t",a*b,end ="")
    print()
