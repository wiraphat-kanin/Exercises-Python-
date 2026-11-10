product_price = int(input("Enter product price: "))

while True :
    payment_product = int(input("Enter payment: "))
    product_price -= payment_product #ใช้การสะสมค่าเอา เเทนที่ จะเอาตัวแปรอื่นมารับค่าลบ 
    if product_price == 0 :
        print("Payment Completed")
        break
    elif product_price > 0 :
        print(f"Remaining {product_price}")

