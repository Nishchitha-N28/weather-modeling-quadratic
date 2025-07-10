with open("file1.txt", "r") as f:
    line = f.readline()
    a, b, c = map(float, line.split())
D = b**2 - 4*a*c
if D < 0:
    print("No real roots")
else:
    root1 = (-b + D**0.5) / (2*a)
    root2 = (-b - D**0.5) / (2*a)
    print(f"Roots: {root1}, {root2}")
