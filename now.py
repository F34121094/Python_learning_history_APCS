import time as t
timer = t.localtime()
year = timer.tm_year
mon = timer.tm_mon
day = timer.tm_mday
hour = timer.tm_hour
min = timer.tm_min
second = timer.tm_sec
print("現在是 %s-%s-%s  %s:%s:%s"%(year,mon,day,hour,min,second))