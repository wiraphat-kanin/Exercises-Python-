a = int(input("A :"))
while a<0 or a>30:
    a= int(input("A :"))

b = int(input("B :"))
while b<0 or b>30:
    b= int(input("B :"))

c = int(input("C :"))
while c<=0 or c>40:
    c= int(input("C :"))

score =a+b+c

if score >= 80:
    print("A")
elif score >= 75:
    print("B+")
elif score >= 70:
    print("B")
elif score >= 65:
    print("C+")
elif score >= 60:
    print("C")
elif score >= 55:
    print("D+")
elif score >= 50:
    print("D")
else:
    print("F")

"""
อธิบาย สมมุติ a = 55 ตรวจสอบ while จะเป็น true วน loop 
กรอกอีกรอบ a = 24 ตรวจสอบ while จะเป็น false ออก loop
เหตุผลใช้ or เพราะ ว่าถ้าใช้ and เงื่อนไขจะเป็น false ทุกกรณีเพราะกำหนด a <= 0
"""
