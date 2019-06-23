
Str  = input("Nhap vao 1 chuoi?\n")
ls = list(Str)
ls.sort()

kq  = ''
for i in range(0,len(ls)):
    kq = kq + str(ls[i])
print(kq)