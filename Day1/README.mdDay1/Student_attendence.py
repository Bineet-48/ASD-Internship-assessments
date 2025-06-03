# Online Student Attendance Tracker

students = []
attendance = {}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Step 1: Enter student names
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    name = input(f"Enter name of student #{i+1}: ")
    students.append(name)
    attendance[name] = []  # Initialize empty attendance list

# Step 2: Record attendance for each day
print("\nEnter 'P' for Present and 'A' for Absent.")

for day in days:
    print(f"\n--- {day} ---")
    for student in students:
        status = input(f"Is {student} present? (P/A): ").strip().upper()
        if status == 'P':
            attendance[student].append(1)
        else:
            attendance[student].append(0)

# Step 3: Show summary
print("\nAttendance Summary:")
print("------------------------")
for student in students:
    present_days = sum(attendance[student])
    print(f"{student}: Present {present_days} days out of {len(days)}")

print("\nAttendance tracking complete.")
