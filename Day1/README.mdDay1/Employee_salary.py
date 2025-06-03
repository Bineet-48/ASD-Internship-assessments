# Constants
HOURLY_RATE = 20  # Base hourly rate in dollars
STANDARD_HOURS = 160  # Standard monthly hours (e.g., 40 hours/week * 4 weeks)
OVERTIME_MULTIPLIER = 1.5  # Overtime bonus rate (e.g., 1.5x)

def calculate_salary(hours_worked):
    if hours_worked <= STANDARD_HOURS:
        salary = hours_worked * HOURLY_RATE
        overtime = 0
    else:
        overtime_hours = hours_worked - STANDARD_HOURS
        salary = (STANDARD_HOURS * HOURLY_RATE) + (overtime_hours * HOURLY_RATE * OVERTIME_MULTIPLIER)
        overtime = overtime_hours
    return salary, overtime

def main():
    print("Employee Salary Processing")
    print("---------------------------")
    
    employee_id = 1
    while True:
        try:
            hours = float(input(f"\nEnter working hours for employee #{employee_id}: "))
            salary, overtime = calculate_salary(hours)
            print(f"Employee #{employee_id} - Total Salary: ${salary:.2f} (Overtime Hours: {overtime})")
            
            cont = input("Do you want to enter details for another employee? (y/n): ").strip().lower()
            if cont != 'y':
                break
            employee_id += 1
        except ValueError:
            print("Invalid input. Please enter a numeric value for hours.")

    print("\nSalary processing complete.")

if __name__ == "__main__":
    main()
