from datetime import datetime
def checkYear(year):  
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))
count = 0
year = input("Nhap vao nam hien tai:?\n")
if(year == ''):
    year = datetime.now().year
print(year)

while(count<10):
    if(checkYear(year)): 
        print(f" {count} :{year}") 
        count = count + 1
    year = year + 1
