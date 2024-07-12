weight = input("請輸入體重(公斤) : ")
height = input("請輸入身高(公尺) : ")
BMI = (float(weight)/(float(height)*float(height)))
print("BMI值 : %.2f"%BMI)
if(BMI<18.5):
    print("體重過輕")
elif(BMI>=18.5 and BMI<=24.9):
    print("正常")
elif(BMI>=25 and BMI<=29.9):
    print("體重過重")
else:
    print("體重肥胖")