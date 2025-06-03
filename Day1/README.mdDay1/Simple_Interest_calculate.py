# Simple Interest Calculation for Multiple Customers

print("Simple Interest Calculator")

while True:
    try:
        name = input("\nEnter customer name: ")
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time period (in years): "))

        if principal < 0 or rate < 0 or time < 0:
            print("Principal, rate, and time must be non-negative. Please try again.")
            continue

        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest

        print(f"{name}'s Simple Interest: ${simple_interest:.2f}")
        print(f"{name}'s Total Amount after {time} years: ${total_amount:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values for principal, rate, and time.")
        continue

    more = input("Calculate for another customer? (yes/no): ").strip().lower()
    if more != 'yes':
        break

print("\nThank you for using the Simple Interest Calculator.")
