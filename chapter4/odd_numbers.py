odd_numbers = list(range(1,21,2))

for n in odd_numbers:
    print(n)

multiples_three = list(range(3,31,3))

print("\n")

for n in multiples_three:
    print(n)

print("\n")

cubes = [n**3 for n in range(1,10)]
for n in cubes:
    print(n)