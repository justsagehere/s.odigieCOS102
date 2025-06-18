import math

def quadratic():
    print("\nQuadratic Equation: Ax^2 + Bx + C = 0")
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))

    D = B**2 - 4*A*C

    if D > 0:
        root1 = (-B + math.sqrt(D)) / (2*A)
        root2 = (-B - math.sqrt(D)) / (2*A)
        print("Two Real Roots:", root1, "and", root2)
    elif D == 0:
        root = -B / (2*A)
        print("One Real Root:", root)
    else:
        print("No real roots")

def cubic():
    print("\nCubic Equation: Ax^3 + Bx^2 + Cx + D = 0")
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))
    D = float(input("Enter D: "))

    # Try simple values from -10 to 10
    print("Checking for simple real roots...")
    found = False
    for x in range(-10, 11):
        value = A*x**3 + B*x**2 + C*x + D
        if abs(value) < 0.0001:
            print("Found a real root at x =", x)
            found = True
            break
    if not found:
        print("No simple real roots found")

def quartic():
    print("\nQuartic Equation: Ax^4 + Cx^2 + E = 0")
    A = float(input("Enter A: "))
    C = float(input("Enter C: "))
    E = float(input("Enter E: "))

    # Let y = x^2, solve Ay^2 + Cy + E = 0
    D = C**2 - 4*A*E

    if D < 0:
        print("No real roots")
        return

    y1 = (-C + math.sqrt(D)) / (2*A)
    y2 = (-C - math.sqrt(D)) / (2*A)

    roots = []
    if y1 >= 0:
        roots.append(math.sqrt(y1))
        roots.append(-math.sqrt(y1))
    if y2 >= 0:
        roots.append(math.sqrt(y2))
        roots.append(-math.sqrt(y2))

    if roots:
        print("Real roots are:", roots)
    else:
        print("No real roots")

def main():
    print("Choose type of equation to solve:")
    print("1. Quadratic")
    print("2. Cubic")
    print("3. Quartic (biquadratic only)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        quadratic()
    elif choice == '2':
        cubic()
    elif choice == '3':
        quartic()
    else:
        print("Invalid choice")

main()
