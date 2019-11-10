import math

x = int(input("Enter a number between 1-10"))
y = int(input("ENter another number between 1-10"))

cal = x ** y
print(cal)

cal2 = math.sqrt(cal)
print(cal2)

while cal2<100000:
	cal2 = cal2+1
	if cal2 == 100000:
		print(cal2)