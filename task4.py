quantity = int(input("Enter number of items produced: "))
if quantity <= 0:
    print("Quantity must be greater than zero.")
    exit()

material_cost_per_item = float(input("Material cost per item: Rs. "))
labour_cost_per_item = float(input("Labour cost per item: Rs. "))
wastage_percent = float(input("Material wastage percentage: "))
machine_cost = float(input("Total machine cost: Rs. "))
selling_price_per_item = float(input("Selling price per item: Rs. "))
target_profit_percent = float(input("Target profit percentage on cost: "))

material_cost = quantity * material_cost_per_item
wastage_cost = material_cost * wastage_percent / 100
labour_cost = quantity * labour_cost_per_item
total_cost = material_cost + wastage_cost + labour_cost + machine_cost

total_sales = quantity * selling_price_per_item
profit = total_sales - total_cost
profit_percent = (profit / total_cost) * 100 if total_cost > 0 else 0
target_profit = total_cost * target_profit_percent / 100

print("\n====== MANUFACTURING COST REPORT ======")
print(f"Quantity produced:          {quantity}")
print(f"Material cost:              Rs. {material_cost:,.2f}")
print(f"Wastage cost:               Rs. {wastage_cost:,.2f}")
print(f"Labour cost:                Rs. {labour_cost:,.2f}")
print(f"Machine cost:               Rs. {machine_cost:,.2f}")
print(f"Total production cost:      Rs. {total_cost:,.2f}")
print(f"Cost per item:              Rs. {total_cost / quantity:,.2f}")
print("---------------------------------------")
print(f"Selling price per item:     Rs. {selling_price_per_item:,.2f}")
print(f"Total sales:                Rs. {total_sales:,.2f}")
print(f"Profit / loss:              Rs. {profit:,.2f}")
print(f"Profit percentage on cost:  {profit_percent:.2f}%")
print(f"Target profit:              Rs. {target_profit:,.2f}")

if profit >= target_profit:
    print("Result: Production meets the profit target.")
else:
    print("Result: Production does not meet the profit target.")

print("=======================================")