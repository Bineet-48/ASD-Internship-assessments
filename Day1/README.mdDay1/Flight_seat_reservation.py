# Flight Seat Reservation System

total_seats = 10  # Total seats on the flight
available_seats = total_seats
booked_seats = []

print(f"Welcome to the Flight Seat Reservation System!")
print(f"Total seats available: {total_seats}")

while available_seats > 0:
    name = input("\nEnter passenger name to book a seat (or type 'exit' to stop): ").strip()
    if name.lower() == 'exit':
        break

    if name == "":
        print("Name cannot be empty. Please try again.")
        continue

    # Book the seat
    booked_seats.append(name)
    available_seats -= 1
    print(f"Seat successfully booked for {name}.")
    print(f"Seats remaining: {available_seats}")

if available_seats == 0:
    print("\nAll seats are booked. Flight is full.")

print("\nBooked Seats List:")
for i, passenger in enumerate(booked_seats, start=1):
    print(f"{i}. {passenger}")

print("\nThank you for using the Flight Seat Reservation System.")
