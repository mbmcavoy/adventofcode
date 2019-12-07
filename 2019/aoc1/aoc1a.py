import math

def fuel_for_mass( mass ):
    return math.floor(mass / 3) - 2

total_fuel = 0

input_file = open("2019/aoc1/input.txt")

for line in input_file:
    module_mass = int(line)
    module_fuel = fuel_for_mass(module_mass)
    total_fuel = total_fuel + module_fuel

    print(f'Mass: {module_mass} ==> Fuel: {module_fuel}')

print(f'Total Fuel: {total_fuel}')

input_file.close()