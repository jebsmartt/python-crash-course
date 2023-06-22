age = 11
life_stage = None

if age < 2:
    life_stage = 'a baby'
elif age < 4:
    life_stage = 'a toddler'
elif age < 13:
    life_stage = 'a kid'
elif age < 20:
    life_stage = 'a teenager'
elif age < 65:
    life_stage = 'an adult'
elif age >= 65:
    life_stage = 'an elder'

print(f"You are {life_stage}")