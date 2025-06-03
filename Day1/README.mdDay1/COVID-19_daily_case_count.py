# COVID-19 Daily Case Counter

days = 14
cases = []

print("Enter daily COVID-19 case numbers for 14 days:")

for day in range(1, days + 1):
    while True:
        try:
            daily_cases = int(input(f"Day {day} cases: "))
            if daily_cases < 0:
                print("Case number cannot be negative. Try again.")
                continue
            cases.append(daily_cases)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

average_cases = sum(cases) / days
max_cases = max(cases)
min_cases = min(cases)

# Find days with max and min cases
max_days = [i + 1 for i, c in enumerate(cases) if c == max_cases]
min_days = [i + 1 for i, c in enumerate(cases) if c == min_cases]

print(f"\nAverage cases per day: {average_cases:.2f}")
print(f"Maximum cases ({max_cases}) occurred on day(s): {', '.join(map(str, max_days))}")
print(f"Minimum cases ({min_cases}) occurred on day(s): {', '.join(map(str, min_days))}")
