def calculate_distance_fare(distance):
    """Calculate fare using progressive distance slabs."""
    if distance <= 100:
        return distance * 1.50
    elif distance <= 300:
        return 100 * 1.50 + (distance - 100) * 2.00
    else:
        return 100 * 1.50 + 200 * 2.00 + (distance - 300) * 2.50


number_of_passengers = int(input("Enter number of passengers: "))
distance = float(input("Enter journey distance in km: "))

print("\nTravel classes:")
print("1. Sleeper (fare multiplier 1.0, reservation Rs. 20)")
print("2. AC      (fare multiplier 2.0, reservation Rs. 50)")
print("3. First   (fare multiplier 3.0, reservation Rs. 80)")
travel_class = input("Choose class (1/2/3): ")

if travel_class == "1":
    class_name = "Sleeper"
    class_multiplier = 1.0
    reservation_fee = 20
elif travel_class == "2":
    class_name = "AC"
    class_multiplier = 2.0
    reservation_fee = 50
elif travel_class == "3":
    class_name = "First"
    class_multiplier = 3.0
    reservation_fee = 80
else:
    print("Invalid class. Please run the program again and choose 1, 2, or 3.")
    exit()

base_fare = calculate_distance_fare(distance) * class_multiplier
total_tickets = 0
total_refund = 0

for passenger in range(1, number_of_passengers + 1):
    age = int(input(f"\nEnter age of passenger {passenger}: "))

    if age <= 12:
        concession = 0.50
    elif age >= 60:
        concession = 0.40
    else:
        concession = 0

    passenger_fare = base_fare * (1 - concession)
    ticket_total = passenger_fare + reservation_fee
    total_tickets += ticket_total

    print(f"\nPassenger {passenger} ({age} years)")
    print(f"Class: {class_name}")
    print(f"Fare after concession: Rs. {passenger_fare:.2f}")
    print(f"Reservation fee:       Rs. {reservation_fee:.2f}")
    print(f"Total ticket fare:     Rs. {ticket_total:.2f}")

    cancel_ticket = input("Cancel this ticket? (yes/no): ").lower()
    if cancel_ticket == "yes":
        hours_before_departure = float(
            input("Hours before departure: ")
        )

        if hours_before_departure >= 48:
            penalty_rate = 0.25
        elif hours_before_departure >= 12:
            penalty_rate = 0.50
        else:
            penalty_rate = 0.75

        penalty = passenger_fare * penalty_rate
        refund = passenger_fare - penalty
        total_refund += refund
        print(f"Cancellation penalty ({penalty_rate * 100:.0f}%): Rs. {penalty:.2f}")
        print(f"Refund (reservation fee is not returned): Rs. {refund:.2f}")

print("\n========== RESERVATION SUMMARY ==========")
print(f"Passengers:              {number_of_passengers}")
print(f"Class:                   {class_name}")
print(f"Distance:                {distance:.1f} km")
print(f"Total original fare:     Rs. {total_tickets:.2f}")
print(f"Total cancellation refund: Rs. {total_refund:.2f}")
print("=========================================")
print("Note: All rates, concessions, and penalties are examples.")