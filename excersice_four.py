num1 ,num2 = [int (e) for e in input().split()] #การรับตัวเลขแนวนอนอีกรูปแบบ
calculate = int(input())

if calculate == 1:
    result = num1 + num2
elif calculate == 2:
    result = num1 - num2
elif calculate == 3:
    result = num1 * num2
elif calculate == 4:
    result = num1 / num2
elif calculate == 5:
    result = num1 % num2
elif calculate == 6:
    result = pow(num1,num2)
elif calculate == 7:
    result = (num1 + num2) / 2

if calculate == 5:
    print(result)

else:
   # result = float(result)
   print(f"{result:.5f}")