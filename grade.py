a = input("第一場比賽結果(1.勝 2.敗) : ")
b = input("第二場比賽結果(1.勝 2.敗) : ")
if(a == '1'):
    if(b == '1'):
        print("得到的獎項 :　",end='')
        print("金牌")
    if (b == '2'):
        print("得到的獎項 :　", end='')
        print("銀牌")
if (a == '2'):
    if (b == '1'):
        print("得到的獎項 :　", end='')
        print("銅牌")
    if (b == '2'):
        print("得到的獎項 :　", end='')
        print("沒有獎牌")