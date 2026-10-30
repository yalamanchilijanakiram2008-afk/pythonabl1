
print("HOUSEHOLD ELECTRICITY BILL")

number_of_months = int(input("Enter the number of months: "))

previous_bill = 0

for month in range(1, number_of_months + 1):

    units = float(input("Enter units used: "))

    # Calculate energy charge
    if units <= 100:
        energy_charge = units * 1.50

    elif units <= 200:
        energy_charge = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 500:
        energy_charge = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    else:
        energy_charge = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

    # Calculate additional charges
    fixed_charge = 50
    surcharge = energy_charge * 0.05

    if units <= 100:
        rebate = 20
    else:
        rebate = 0

    total_bill = energy_charge + fixed_charge + surcharge - rebate

    print("\nMonth:", month)
    print("Units Used:", units)
    print("Energy Charge: Rs.", energy_charge)
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", surcharge)
    print("Rebate: Rs.", rebate)
    print("Total Bill: Rs.", round(total_bill, 2))

    # Compare previous month bill
    if month > 1:

        increase = total_bill - previous_bill

        if previous_bill == 0:
            increase_percent = 0
        else:
            increase_percent = (increase / previous_bill) * 100

        if increase_percent > 20:
            print("Unusual increase:", round(increase_percent, 2), "%")

        elif increase > 0:
            print("Increase from previous month:", round(increase_percent, 2), "%")

        elif increase < 0:
            print("Bill decreased from previous month.")

        else:
            print("No change in bill.")

    previous_bill = total_bill
