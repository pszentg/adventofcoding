with open("masses.txt") as f:
    masses = f.readlines()
    masses = [x.strip() for x in masses]

    fuel_required_for_modules = 0
    total_fuel_required = 0
    for mass in masses:
        fuel = (int(int(mass) / 3)) - 2
        fuel_required_for_modules += fuel
        total_fuel_required += fuel
        while fuel > 0:
            fuel = (int(int(fuel) / 3)) - 2
            if fuel > 0:
                total_fuel_required += fuel

    print(fuel_required_for_modules)
    print(total_fuel_required)