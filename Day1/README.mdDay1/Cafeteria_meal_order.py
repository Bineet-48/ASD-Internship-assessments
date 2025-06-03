# Cafeteria Meal Order Calculator

menu = {
    1: {"item": "Burger", "price": 5.0},
    2: {"item": "Pizza", "price": 8.0},
    3: {"item": "Salad", "price": 4.5},
    4: {"item": "Soda", "price": 1.5},
    5: {"item": "Coffee", "price": 2.0}
}

total_cost = 0.0

print("Welcome to the Cafeteria!")
print("Menu:")
for key, value in menu.items():
    print(f"{key}. {value['item']} - ${value['price']:.2f}")

while True:
    try:
        choice = int(input("\nEnter the item number to order (0 to finish): "))
        if choice == 0:
            break
        if choice not in menu:
            print("Invalid choice. Please select a valid item number.")
            continue

        quantity = int(input(f"Enter quantity for {menu[choice]['item']}: "))
        if quantity < 1:
            print("Quantity must be at least 1.")
            continue

        item_cost = menu[choice]['price'] * quantity
        total_cost += item_cost
        print(f"Added {quantity} x {menu[choice]['item']} to your order. Item cost: ${item_cost:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

print(f"\nYour total meal cost is: ${total_cost:.2f}")
print("Thank you for your order!")
