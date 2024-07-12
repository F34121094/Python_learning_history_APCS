a = input("請輸入期中考成績 : ")
print("輸入的成績是 : %s" %a)
if(int(a) > 100 or int(a) < 0):
    print("成績不合理，請重新確認")
else:
    print("成績在合理範圍之內")