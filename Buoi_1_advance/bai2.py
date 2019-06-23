
Str = input("Nhap vao 1 chuoi?\n")
new = []
temp = set(Str)
temp = list(temp)
temp.sort()
# print(temp[0])
for i in range(0,len(temp)):
    new.append(Str.count(temp[i]))
for i in range(0,len(temp)):
    print(f"({temp[i]}) : {new[i]}")