# Student Result Management System

# Store student data in a list
students = []

# Add new student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    cls = input("Enter Class: ")
    subjects = {}
    
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        sub = input(f"Enter subject {i+1} name: ")
        marks = int(input(f"Enter marks for {sub}: "))
        subjects[sub] = marks
    
    total = sum(subjects.values())
    percentage = total / n
    
    student = {
        "Roll No": roll,
        "Name": name,
        "Class": cls,
        "Subjects": subjects,
        "Total": total,
        "Percentage": percentage
    }
    
    students.append(student)
    print("✔ Student record added successfully!\n")

# View all students
def view_students():
    if not students:
        print("⚠ No student records found!\n")
        return
    
    for s in students:
        print(f"Roll No: {s['Roll No']}, Name: {s['Name']}, Class: {s['Class']}")
        print("Subjects & Marks:")
        for sub, marks in s['Subjects'].items():
            print(f"  {sub}: {marks}")
        print(f"Total: {s['Total']}, Percentage: {s['Percentage']:.2f}%")
        print("-"*40)

# Search student by roll number
def search_student():
    roll = input("Enter Roll Number to search: ")
    found = False
    for s in students:
        if s['Roll No'] == roll:
            print(f"\nRoll No: {s['Roll No']}, Name: {s['Name']}, Class: {s['Class']}")
            print("Subjects & Marks:")
            for sub, marks in s['Subjects'].items():
                print(f"  {sub}: {marks}")
            print(f"Total: {s['Total']}, Percentage: {s['Percentage']:.2f}%")
            found = True
    if not found:
        print("⚠ Student not found!\n")

# Main menu
def menu():
    while True:
        print("\n=== Student Result Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting... Bye 👋")
            break
        else:
            print("⚠ Invalid choice!\n")

# Run the system
menu()
