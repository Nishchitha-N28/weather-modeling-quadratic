with open("file2.txt", "r") as f:
    for l in f:
        a, b, c = map(float, l.split())
        D = b**2 - 4*a*c
        if D < 0:
            print(f"For {a}, {b}, {c}: No real roots")
        else:
            root1 = (-b + D**0.5) / (2*a)
            root2 = (-b - D**0.5) / (2*a)
            print(f"For {a}, {b}, {c}: Roots are {root1}, {root2}")
