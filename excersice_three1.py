str1 = input()
count = 1 #ตัวนับจำนวนตัวอักษร
str2 = ""
for i in range(len(str1)):
    if i != len(str1)-1: #เปรียบเทียบ i (index) ตัวปัจจุบัน กับ len(str1[i+1) (index) ตัวถัดไป
        if str1[i] == str1[i+1]:
            count += 1
        elif str1[i] != str1[i+1] and str1[i+1] == str1[i+2]: #ถ้ามีตัวอักษร 1 ตัวไม่ต้องแสดงตัวเลข
            str2 += str1[i]
            count = 1 #เซ็ตให้กลับไปเริ่มใหม่ถ้าตัวอักษรไม่เหมือนกัน
        else:
            str2 += str(count)
            str2 += str1[i]
            count = 1  # เซ็ตให้กลับไปเริ่มใหม่ถ้าตัวอักษรไม่เหมือนกัน


    elif i == len(str1)-1:
        str2 += str(count)
        str2 += str1[i]

print(str2)