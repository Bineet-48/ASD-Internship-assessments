# E-commerce Order Summary Generator

order_list = []  # To store each product's order
total_amount = 0

print("Welcome to the E-commerce Order Summary Generator!")
print("--------------------------------------------------")

while True:
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    subtotal = quantity * price
    total_amount += subtotal

    order_list.append((name, quantity, price, subtotal))

    more = input("Add another product? (yes/no): ")
    if more.lower() != 'yes':
        break

# Print the final bill
print("\nFinal Order Summary:")
print("{:<20} {:<10} {:<10} {:<10}".format("Product", "Qty", "Price", "Subtotal"))
print("-" * 50)

for item in order_list:
    print("{:<20} {:<10} ${:<9.2f} ${:<9.2f}".format(item[0], item[1], item[2], item[3]))

print("-" * 50)
print(f"Total Bill: ${total_amount:.2f}")
