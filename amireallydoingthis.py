x = 1
y = 1
x^3
while True:
    x -= 0.000000000000000000000000000000001
    y -= 0.000000000000000000000000000000000000001
    result = (x**3 + y**3)/(x**2 + y**2)
    print(result)