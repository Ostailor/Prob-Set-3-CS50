fuel = input("Fraction: ")
x = fuel[0: fuel.find("/")]
y = fuel[fuel.find("/") + 1:]
while True:
    try:
        x = int(x)
        y = int(y)
        if x <= y:
            z = float(x/y)
        else:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        while True:
            fuel = input("Fraction: ")
            x = fuel[0: fuel.find("/")]
            y = fuel[fuel.find("/") + 1:]
            if x.isnumeric() and y.isnumeric():
                x = int(x)
                y = int(y)
                if y > 0:
                    z = float(x/y)
                    break
    else:
        break

if 0.99 <= z <= 1:
    print("F", end="")
elif 0 <= z <= 0.01:
    print("E", end="")
else:
    print(f"{round(float(z * 100))}%", end="")
