# Hotel Room Booking Tracker

room_rate_per_night = 100  # Fixed price per night in dollars

print("Welcome to the Hotel Room Booking Tracker!")

while True:
    customer = input("\nEnter customer name: ")
    try:
        nights = int(input(f"Enter number of nights {customer} will stay: "))
        if nights < 1:
            print("Number of nights must be at least 1. Try again.")
            continue
    except ValueError:
        print("Please enter a valid number for nights.")
        continue

    total_bill = nights * room_rate_per_night
    print(f"Total bill for {customer} is: ${total_bill}")

    more = input("Book another room? (yes/no): ").strip().lower()
    if more != 'yes':
        break

print("\nThank you for using the Hotel Room Booking Tracker.")
