number_of_products = int(input("Enter number of products: "))

if number_of_products <= 0:
    print("Enter at least one product.")
    exit()

print("\n====== WAREHOUSE INVENTORY RECONCILIATION ======")

for product_number in range(1, number_of_products + 1):
    print(f"\nProduct {product_number}")
    product_name = input("Product name: ")
    opening_stock = int(input("Opening stock: "))
    incoming_quantity = int(input("Incoming quantity: "))
    dispatched_quantity = int(input("Dispatched quantity: "))
    actual_closing_stock = int(input("Counted closing stock: "))
    minimum_stock = int(input("Minimum stock level: "))

    quantities = [
        opening_stock,
        incoming_quantity,
        dispatched_quantity,
        actual_closing_stock,
        minimum_stock,
    ]

    if any(quantity < 0 for quantity in quantities):
        print("Stock quantities cannot be negative. Please run the program again.")
        exit()

    expected_closing_stock = opening_stock + incoming_quantity - dispatched_quantity
    discrepancy = actual_closing_stock - expected_closing_stock
    replenishment = max(0, minimum_stock - actual_closing_stock)

    print(f"\nInventory report for {product_name}")
    print(f"Expected closing stock: {expected_closing_stock}")
    print(f"Counted closing stock:  {actual_closing_stock}")

    if discrepancy == 0:
        print("Stock status:          No discrepancy")
    elif discrepancy > 0:
        print(f"Stock status:          {discrepancy} extra in count")
    else:
        print(f"Stock status:          {abs(discrepancy)} missing in count")

    print(f"Replenishment needed:  {replenishment}")

print("\n================================================")