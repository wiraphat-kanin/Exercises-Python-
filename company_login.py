# บริษัทรต้องการเข้าสู่ระบบพนักงานโดยออกเเบบให้กรอกรหัสผ่านเพียง 3 ครั้ง
count = 0
while True:
    password = input("Enter password : ")

    if password == "123":
        print("Login Successful")
        break
    else:
        count +=1
        if count == 3:
            print("Incorrect Password")
            break