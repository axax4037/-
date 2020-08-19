# 密碼重試程式 
# password = "a123456"
# 讓使用者重複輸入密碼
# 最多三次
# 如果正確 print "登入成功"
# 如果布正確 print "密碼錯誤！ 還有__此機會！"
password = "a123456"
x = 3
while x > 0:
    x = x - 1
    pwd = input("請輸入密碼: ")
    if pwd == password:
        print("登入成功")
        break
    else:
        print("密碼錯誤！")
        if x > 0:
            print("還有", x,"次機會")
        else:
            print("沒有機會了，再見")
            break