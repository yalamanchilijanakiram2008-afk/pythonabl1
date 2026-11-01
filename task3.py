
print("RAILWAY RESERVATION AND FARE CALCULATION")

number_of_passengers = int(input("Enter number of passengers: "))
distance = float(input("Enter journey distance in km: "))

# Distance-based fare calculation
if distance <= 100:
    base_fare = distance * 1.50
elif distance <= 300:
    base_fare = 100 * 1.50 + (distance - 100) * 2.00
else:
    base_fare = 100 * 1.50 + 200 * 2.00 + (distance - 300) * 2.50

# Select travel class
print("\n1. Sleeper")
print("2. AC")
print("3. First")

travel_class = input("Choose class (1/2/3): ")

if travel_class == "1":
    class_name = "Sleeper"
    multiplier = 1
    reservation_fee = 20
elif travel_class == "2":
    class_name = "AC"
    multiplier = 2
    reservation_fee = 50
elif travel_class == "3":
    class_name = "First"
    multiplier = 3
    reservation_fee = 80
else:
    print("Invalid class")
    exit()

base_fare = base_fare * multiplier

total_tickets = 0
total_refund = 0

# Passenger details
for passenger in range(1, number_of_passengers + 1):

    age = int(input("\nEnter passenger age: "))

    if age <= 12:
        concession = 0.50
    elif age >= 60:
        concession = 0.40
    else:
        concession = 0

    passenger_fare = base_fare * (1 - concession)
    ticket_total = passenger_fare + reservation_fee

    total_tickets = total_tickets + ticket_total

    print("\nPassenger:", passenger)
    print("Class:", class_name)
    print("Fare:", passenger_fare)
    print("Reservation fee:", reservation_fee)
    print("Total ticket fare:", ticket_total)

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel == "yes":

        hours = float(input("Hours before departure: "))

        if hours >= 48:
            penalty_rate = 0.25
        elif hours >= 12:
            penalty_rate = 0.50
        else:
            penalty_rate = 0.75

        penalty = passenger_fare * penalty_rate
        refund = passenger_fare - penalty

        total_refund = total_refund + refund

        print("Cancellation penalty:", penalty)
        print("Refund amount:", refund)

# Final summary
print("\n========== RESERVATION SUMMARY ==========")
print("Passengers:", number_of_passengers)
print("Class:", class_name)
print("Distance:", distance, "km")
print("Total original fare:", total_tickets)
print("Total cancellation refund:", total_refund)
print("=========================================")
