__author__ = "khanh pham"

import math
sum  = 0
n = int(input("Plese enter 1 number?\n"))

for i in range(1,n+1):
    if(i%3 == 0 or i%5 == 0):
        sum = sum + i
print(sum)