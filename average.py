#宣告擁有5個元素的串來讓使用者存放，待5個元素填完，輸出平均
arr = [0 for x in range(5)]
total = 0
for i in range(5):
    arr[i] = int(input("輸入第"+str(i+1)+"個整數 : "))
    total += arr[i]
total /= 5
print("----------")
print("平均 : %.2f"%total)