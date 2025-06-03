# Supermarket Inventory Manager

products = []
total_items = 0
total_value = 0.0

print("Supermarket Inventory Manager")

while True:
    name = input("\nEnter product name: ")
    try:
        quantity = int(input("Enter stock quantity: "))
        price = float(input("Enter price per item: "))
        if quantity < 0 or price < 0:
            print("Quantity and price must be non-negative. Try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter numbers for quantity and price.")
        continue

    products.append({"name": name, "quantity": quantity, "price": price})

    total_items += quantity
    total_value += quantity * price

    more = input("Add another product? (yes/no): ").strip().lower()
    if more != 'yes':
        break

# Display summary
print("\nInventory Summary:")
print(f"Total number of items in stock: {total_items}")
print(f"Total inventory value: ${total_value:.2f}")
