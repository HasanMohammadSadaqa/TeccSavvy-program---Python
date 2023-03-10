a = int(input("please enter the first number: "))
b = int(input("please enter the second number: "))
c = int(input("please enter the third number: "))

if a<=b<=c:
    print(f"{a}, {b}, {c}")
elif a<=c<=b:
    print(f"{a}, {c}, {b}")
elif a>=c>b:
    print(f"{b}, {c}, {a}")
elif b<=a<=c:
    print(f"{b}, {a}, {c}")
elif c<=b<=a:
    print(f"{c}, {b}, {a}")
else:
    print(f"{c}, {a}, {b}")
