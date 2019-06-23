__author__ = "khanh pham"

number  = 99
count  = 1
a = []
x = int(input("Press 1 number?\n"))
while(x!= number):
    if(x>number):
        print("Too lagre")
    elif(x<number):
        print("Too small")
    a.append(x)
    x = int(input("Press 1 number agian?\n"))
    if(x not in a):
        count = count + 1
print(number,count)
