def calculate_bill(units):
    """Calculate a household bill using progressive electricity slabs."""
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 500:
        energy_charge = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    else:
        energy_charge = (
            100 * 1.50 + 100 * 2.50 + 300 * 4.00 + (units - 500) * 6.00
        )

    fixed_charge = 50
    surcharge = energy_charge * 0.05
    rebate = 20 if units <= 100 else 0
    total = energy_charge + fixed_charge + surcharge - rebate
    return total


number_of_months = int(input("Enter the number of months: "))
monthly_bills = []

for month in range(1, number_of_months + 1):
    units = float(input(f"Enter units used in month {month}: "))
    bill = calculate_bill(units)
    monthly_bills.append(bill)

    print(f"Month {month}: Bill = Rs. {bill:.2f}")

    if month > 1:
        previous_bill = monthly_bills[month - 2]
        increase = bill - previous_bill

        if previous_bill == 0:
            increase_percent = 100 if increase > 0 else 0
        else:
            increase_percent = (increase / previous_bill) * 100

        if increase_percent > 20:
            print(f"  Unusual increase: {increase_percent:.1f}%")
        elif increase > 0:
            print(f"  Increase from previous month: {increase_percent:.1f}%")
        else:
            print("  No increase from previous month.")