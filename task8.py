capacity = float(input("Enter tank capacity (litres): "))
water_level = float(input("Enter initial water level (litres): "))
number_of_days = int(input("Enter number of days to simulate: "))
threshold = float(input("Enter water-level threshold (litres): "))

if capacity <= 0:
    print("Tank capacity must be greater than zero.")
    exit()

if water_level < 0 or water_level > capacity:
    print("Initial water level must be between 0 and tank capacity.")
    exit()

if number_of_days < 0:
    print("Number of days cannot be negative.")
    exit()

if threshold < 0 or threshold > capacity:
    print("Threshold must be between 0 and tank capacity.")
    exit()

first_threshold_day = 0 if water_level >= threshold else None
total_overflow = 0
total_shortage = 0

print("\n====== WATER TANK SIMULATION ======")
print(f"Initial water level: {water_level:.2f} litres")

for day in range(1, number_of_days + 1):
    print(f"\nDay {day}")
    inflow = float(input("  Enter inflow (litres): "))
    outflow = float(input("  Enter outflow (litres): "))

    if inflow < 0 or outflow < 0:
        print("Inflow and outflow cannot be negative.")
        exit()

    available_water = water_level + inflow
    overflow = max(0, available_water - capacity)
    available_water = min(available_water, capacity)
    shortage = max(0, outflow - available_water)
    water_level = max(0, available_water - outflow)

    total_overflow += overflow
    total_shortage += shortage

    print(f"  Overflow: {overflow:.2f} litres")
    print(f"  Unmet outflow (shortage): {shortage:.2f} litres")
    print(f"  Water level at end of day: {water_level:.2f} litres")

    if first_threshold_day is None and water_level >= threshold:
        first_threshold_day = day

print("\n====== SIMULATION SUMMARY ======")
print(f"Final water level: {water_level:.2f} litres")
print(f"Total overflow: {total_overflow:.2f} litres")
print(f"Total shortage: {total_shortage:.2f} litres")

if first_threshold_day == 0:
    print("Threshold was already reached at the start (day 0).")
elif first_threshold_day is not None:
    print(f"Threshold first reached at the end of day {first_threshold_day}.")
else:
    print("Threshold was not reached during the simulation.")

print("================================")