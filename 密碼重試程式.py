# 密碼重試程式 
# password = "a123456"
# 讓使用者重複輸入密碼
# 最多三次
# 如果正確 print "登入成功"
# 如果布正確 print "密碼錯誤！ 還有__此機會！"
password = "a123456"
x = 3
while True:
    pwd = input("請輸入密碼: ")
    if pwd == password:
        print("登入成功")
        break
    else:
        x = x - 1
        print("密碼錯誤！ 還有", x,"此機會！")
        if x == 0:
           break