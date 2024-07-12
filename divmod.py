money = 12500
person = 28
x,y = divmod(money,person)
print("班費剩餘 %d 元，學生有 %d 人"%(money,person))
print("每位學生平均分得 %d 元"%x)
print("班費仍剩餘 %d 元"%y)