ticket_adult = int(input("ตั๋วผู้ใหญ่จำนวน (ใบ) : "))
ticket_child = int(input("ตั๋วเด็กจำนวน (ใบ) : "))
ticket_all = ticket_child + ticket_adult
member = input("คุณเป็นสมาชิกหรือไม่ (yes/no) : ")

if member.lower() == "yes" and int(ticket_child) !=0 :
    if ticket_all >= 10 :
        total_price =(ticket_child * 50)+(ticket_adult * 100) * ((100-50)/100)
        print("รวมราคาเป็นจำนวนเงิน",total_price,"บาท")
    elif ticket_all >= 5 :
        total_price =(ticket_child * 50)+(ticket_adult * 100) * ((100-30)/100)
        print("รวมราคาเป็นจำนวนเงิน",total_price,"บาท")
    else :
        total_price = (ticket_child * 50) + (ticket_adult * 100) * ((100-20)/100)
        print("รวมราคาเป็นจำนวนเงิน", total_price, "บาท")
elif member.lower() == "yes" and int(ticket_child) == 0:
    total_price = ((ticket_adult * 100) * ((100-10)/100))
    print("รวมราคาเป็นจำนวนเงิน", total_price, "บาท")
else:
    total_price = (ticket_child * 50) + (ticket_adult * 100) * ((100-50)/100)
    print("รวมราคาเป็นจำนวนเงิน", total_price, "บาท")


