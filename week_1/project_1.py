
P = float(input("Enter a principal: "))
R = float(input("Enter the rate: "))
T = float(input("Enter the time: "))
N = float(input("Enter number of terms: "))


w = R / 100
s = w * T
d = 1 + s
A = P * d

print(f"Simple Interest = {A}")

f = R / N
r = N * T
t = 1 + f
y = t ** r
a = P * y

print(f"Compound Interest = {a}")

z = y - 1
x = z / f
h = P * R * T
G = h * x

print(f"Annunity plan = {G}")