total = 45
a = input("請輸入消費金額 : ")
if (int(a) > total):
    print("餘額不足")
    print("自動加值500元")
    total += 500
total -= int(a)
print("儲值卡餘額 = %d"%total)