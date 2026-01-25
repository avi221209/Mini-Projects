# Student Record Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No records found!")
        return
    for roll, data in students.items():
        print(f"Roll: {roll}, Name: {data['Name']}, Marks: {data['Marks']}")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found!")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter New Name: ")
        marks = input("Enter New Marks: ")
        students[roll] = {"Name": name, "Marks": marks}
        print("Record updated!")
    else:
        print("Student not found!")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Record deleted!")
    else:
        print("Student not found!")

while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
# tiny update
