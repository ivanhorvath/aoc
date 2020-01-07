import math

with open('input') as file:
    modulez = file.readlines()

total_fuel = 0
total_with_fuel = 0

def calc_fuel(fuel):
    x = 0
    while fuel > 0:
        x += fuel
        new_mass = math.floor(fuel / 3) - 2

        fuel = new_mass

    return x

for modul in modulez:
    mass_of_modul = int(modul)
    fuel_for_mass = math.floor(mass_of_modul / 3) - 2
    
    total_fuel += fuel_for_mass
    total_with_fuel += calc_fuel(fuel_for_mass)


print(total_fuel)
print(total_with_fuel)
