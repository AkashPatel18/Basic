side1= 4
side2= 5
side3= 7


if side1== side2 and side2 == side3:
	print("equilateral")
elif side1 == side2 or side3 == side2 or side1 == side3:
	print("isosceles")
else :
	print("scalene")