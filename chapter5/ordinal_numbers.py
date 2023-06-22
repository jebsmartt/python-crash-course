numbers = []

for i in range(1,10):
    numbers.append(i)

for n in numbers:
    if n == 1:
        print("1st")
    elif n == 2:
        print("2nd")
    elif n == 3:
        print("3rd")
    else:
        print(f"{n}th")
    print("")