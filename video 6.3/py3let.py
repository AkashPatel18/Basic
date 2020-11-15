x= 10
y=6
z=8


max1 = max(x,y,z)

if max1 == x:
    max2=y
    max3=z
elif max1 == y:
    max2=z
    max3=x
else:
    max2=x
    max3=y


if max1**2 ==  max2**2 + max3**2:
    print("py tip")
else:
    ("not")


