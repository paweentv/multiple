x = input("โปรแกรมสูตรคูณ กรุณากรอกตัวเลขที่ต้องการ: ")
for a in range(2, int(x)+1):
    for b in range(1, 13):
        result = a * b
        print(str(a) +"x"+ str(b) +"="+ str(result))
    print(" ")