def cal(n1,n2,n3):
    end = n1 + (n3-1)*n2
    total = ((n1+end)/2)*n3
    return end,total
a = eval(input("請輸入數列首項 : "))
b = eval(input("請輸入數列公差 : "))
c = eval(input("請輸入數列項數 : "))
end ,total = cal(a,b,c)
print("等差數列的末項為 %d ，和為 %d"%(end,total))