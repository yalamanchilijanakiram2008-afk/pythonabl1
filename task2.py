
print("EMPLOYEE SALARY STATEMENT")

employee_name = input("Enter employee name: ")

basic_pay = float(input("Enter basic pay: Rs. "))
allowances = float(input("Enter total allowances: Rs. "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

# Calculate overtime pay
overtime_pay = overtime_hours * overtime_rate

# Calculate gross salary
gross_salary = basic_pay + allowances + overtime_pay + incentives

# Calculate provident fund
provident_fund = basic_pay * 0.12

# Calculate income tax using if-else
if gross_salary <= 25000:
    income_tax = 0

elif gross_salary <= 50000:
    income_tax = (gross_salary - 25000) * 0.05

elif gross_salary <= 100000:
    income_tax = (25000 * 0.05) + ((gross_salary - 50000) * 0.10)

else:
    income_tax = (25000 * 0.05) + (50000 * 0.10) + ((gross_salary - 100000) * 0.20)

# Calculate total deductions
total_deductions = provident_fund + income_tax

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display salary statement
print("\n========== SALARY STATEMENT ==========")

print("Employee:", employee_name)

print("\nEARNINGS")
print("Basic Pay: Rs.", basic_pay)
print("Allowances: Rs.", allowances)
print("Overtime Pay: Rs.", overtime_pay)
print("Incentives: Rs.", incentives)
print("Gross Salary: Rs.", gross_salary)

print("\nDEDUCTIONS")
print("Provident Fund: Rs.", provident_fund)
print("Income Tax: Rs.", income_tax)
print("Total Deductions: Rs.", total_deductions)

print("\nNET SALARY: Rs.", round(net_salary, 2))

print("======================================")
print("Note: Tax rates are examples.")
