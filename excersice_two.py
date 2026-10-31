
y1,m1,d1 = map(int,input().split())  #รับค่าตัวแปลหลายตัวแบบ .split() เป็นฟังชันก์เเนวนอน
y2,m2,d2 = map(int,input().split())

if y1>y2:
    print("1")
elif y1<y2:
    print("2")
elif y1==y2:
    if m1>m2:
        print("1")
    elif m1<m2:
        print("2")
    elif m1==m2:
        if d2>d2:
            print("1")
        elif d2<d2:
            print("2")


