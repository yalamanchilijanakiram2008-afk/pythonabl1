distance = float(input("Enter journey distance (km): "))
reserve_percent = float(input("Enter required fuel reserve (%): "))
number_of_vehicles = int(input("Enter number of vehicles to compare: "))

if distance <= 0:
    print("Journey distance must be greater than zero.")
    exit()

if reserve_percent < 0:
    print("Reserve percentage cannot be negative.")
    exit()

if number_of_vehicles <= 0:
    print("Enter at least one vehicle.")
    exit()

feasible_options = []

for vehicle_number in range(1, number_of_vehicles + 1):
    print(f"\nVehicle {vehicle_number}")
    vehicle_name = input("Vehicle name: ")
    mileage = float(input("Mileage (km per litre): "))
    fuel_price = float(input("Fuel price per litre: Rs. "))
    tank_capacity = float(input("Tank capacity (litres): "))

    if mileage <= 0 or fuel_price < 0 or tank_capacity < 0:
        print("Mileage must be positive; price and capacity cannot be negative.")
        exit()

    trip_fuel = distance / mileage
    reserve_fuel = trip_fuel * reserve_percent / 100
    total_fuel_required = trip_fuel + reserve_fuel
    trip_cost = trip_fuel * fuel_price
    cost_with_reserve = total_fuel_required * fuel_price
    is_feasible = total_fuel_required <= tank_capacity

    print(f"\n{vehicle_name}")
    print(f"Fuel for journey:         {trip_fuel:.2f} litres")
    print(f"Required reserve:         {reserve_fuel:.2f} litres")
    print(f"Fuel needed in tank:      {total_fuel_required:.2f} litres")
    print(f"Fuel capacity:            {tank_capacity:.2f} litres")
    print(f"Journey fuel cost:        Rs. {trip_cost:.2f}")
    print(f"Cost including reserve:   Rs. {cost_with_reserve:.2f}")

    if is_feasible:
        print("Status: FEASIBLE")
        feasible_options.append((cost_with_reserve, vehicle_name))
    else:
        print("Status: NOT FEASIBLE (tank cannot hold trip fuel plus reserve)")

print("\n====== ROUTE COMPARISON ======")

if feasible_options:
    lowest_cost, best_vehicle = min(feasible_options)
    print(f"Lowest-cost feasible vehicle: {best_vehicle}")
    print(f"Estimated cost including reserve: Rs. {lowest_cost:.2f}")
else:
    print("No vehicle has enough tank capacity for the trip and reserve.")

print("Note: Cost includes the reserve fuel; all values are estimates.")
print("==============================")