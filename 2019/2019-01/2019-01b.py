import math

total_fuel = 0

def fuel_for_mass( mass ):
    return math.floor(mass / 3) - 2

def fuel_for_fuel( fuel , level):
    extra_fuel = fuel_for_mass(fuel)
    if (extra_fuel > 0):
        print(f'For fuel {fuel}, extra fuel needed: {extra_fuel}, Level {level}')
        even_more_fuel = fuel_for_fuel(extra_fuel, level + 1)
        return extra_fuel + even_more_fuel
    else:
        print(f'Fuel Wishes')
        return 0


input_file = open("2019/2019-01/input.txt")

for line in input_file:
    module_mass = int(line)
    module_fuel = fuel_for_mass(module_mass)
    total_fuel += module_fuel
    print(f'Mass: {module_mass} ==> Fuel: {module_fuel}')
    total_fuel += fuel_for_fuel(module_fuel, 1)

print(f'Total Fuel: {total_fuel}')

input_file.close()




