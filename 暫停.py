import time as t
a = t.time()
print("暫停前電腦時間 : "+str(a))
t.sleep(6)
b = t.time()
print("暫停後電腦時間 : "+str(b))
print("程式暫停了 "+str(b-a)+" 秒")