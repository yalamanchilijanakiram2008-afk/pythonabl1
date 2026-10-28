def calculate_tax(gross_salary):
    """Calculate monthly income tax using progressive example slabs."""
    if gross_salary <= 25000:
        tax = 0
    elif gross_salary <= 50000:
        tax = (gross_salary - 25000) * 0.05
    elif gross_salary <= 100000:
        tax = 25000 * 0.05 + (gross_salary - 50000) * 0.10
    else:
        tax = 25000 * 0.05 + 50000 * 0.10 + (gross_salary - 100000) * 0.20

    return tax


employee_name = input("Enter employee name: ")
basic_pay = float(input("Enter basic pay: Rs. "))
allowances = float(input("Enter total allowances: Rs. "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

overtime_pay = overtime_hours * overtime_rate
gross_salary = basic_pay + allowances + overtime_pay + incentives

# Example deduction: provident fund is 12% of basic pay.
provident_fund = basic_pay * 0.12
income_tax = calculate_tax(gross_salary)
total_deductions = provident_fund + income_tax
net_salary = gross_salary - total_deductions

print("\n========== SALARY STATEMENT ==========")
print(f"Employee:                 {employee_name}")
print("--------------------------------------")
print("EARNINGS")
print(f"Basic pay:                Rs. {basic_pay:,.2f}")
print(f"Allowances:               Rs. {allowances:,.2f}")
print(f"Overtime pay:             Rs. {overtime_pay:,.2f}")
print(f"Incentives:               Rs. {incentives:,.2f}")
print(f"Gross salary:             Rs. {gross_salary:,.2f}")
print("--------------------------------------")
print("DEDUCTIONS")
print(f"Provident fund (12%):     Rs. {provident_fund:,.2f}")
print(f"Progressive income tax:   Rs. {income_tax:,.2f}")
print(f"Total deductions:         Rs. {total_deductions:,.2f}")
print("--------------------------------------")
print(f"NET SALARY:               Rs. {net_salary:,.2f}")
print("======================================")
print("Note: Tax slabs and deduction rates are examples.")