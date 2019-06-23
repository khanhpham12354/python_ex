# Ax^2+Bx+C = 0
# a = 0
# a != 0
import math

A = float(input("Nhap A?\n"))
B = float(input("Nhap B?\n"))
C = float(input("Nhap C?\n"))

X = 0.0
print(f"{A}X^2 + {B}X + {C} = 0")

if(A==0):
    if(B==0):
        if(C==0):
            print("PTVSN")
        else:
            print("PTVN")
    else:
        X = float(-C/B)
        print(f"X = {X}")
else:
    delta = B**2-4*A*C
    print(delta)
    if(delta<0):
        print("PTVN")
    elif(delta==0):
        X = float(-B/(2*A))
        print(f"PT co nghiem kep {X}")
    else:
        X1 = (-B-math.sqrt(delta))/(2*A)
        X2 = (-B+math.sqrt(delta))/(2*A)
        print(f"PT co 2 nghiem phan biet X1 = {X1} va X2 = {X2}")