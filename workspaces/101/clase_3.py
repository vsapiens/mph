x = 10.4
y = 2.5
z = 1.5

if x > y and x > z:
    print("x es el mayor")
    if y > z:
        print("y es el segundo mayor")
        print("z es el menor")
    else:
        print("z es el segundo mayor")
        print("y es el menor")
elif y > x and y > z:
    print("y es el mayor")
    if x > z:
        print("x es el segundo mayor")
        print("z es el menor")
    else:
        print("z es el segundo mayor")
        print("x es el menor")
elif z > x and z > y:
    print("z es el mayor")
    if x > y:
        print("x es el segundo mayor")
        print("y es el menor")
    else:
        print("y es el segundo mayor")
        print("x es el menor")
else:
    print("hay un empate")