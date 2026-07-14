# SCHOOL MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner (File Handling Upgrade)

import json
import os

print("============ Welcome to School Management System ============")

# ---------------- File Handling ----------------

def load_students():
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

if not students:
    students = [
        {"Student ID": 1, "Name": "Ali", "Class": "9th", "Age": 15, "Date of Birth": "12-03-2011"},
        {"Student ID": 2, "Name": "Abdullah", "Class": "9th", "Age": 15, "Date of Birth": "24-07-2011"},
        {"Student ID": 3, "Name": "Ahmed", "Class": "10th", "Age": 16, "Date of Birth": "05-01-2010"},
        {"Student ID": 4, "Name": "Baqar", "Class": "8th", "Age": 14, "Date of Birth": "18-09-2012"},
        {"Student ID": 5, "Name": "Bilal", "Class": "9th", "Age": 15, "Date of Birth": "02-11-2011"},
        {"Student ID": 6, "Name": "Rida", "Class": "8th", "Age": 14, "Date of Birth": "30-04-2012"},
        {"Student ID": 7, "Name": "Sohiba", "Class": "11th", "Age": 17, "Date of Birth": "14-06-2009"},
        {"Student ID": 8, "Name": "Fabiha", "Class": "9th", "Age": 15, "Date of Birth": "22-02-2011"},
        {"Student ID": 9, "Name": "Hassan", "Class": "10th", "Age": 16, "Date of Birth": "09-08-2010"},
        {"Student ID": 10, "Name": "Zainab", "Class": "8th", "Age": 14, "Date of Birth": "17-12-2012"},
        {"Student ID": 11, "Name": "Usman", "Class": "11th", "Age": 17, "Date of Birth": "03-05-2009"},
        {"Student ID": 12, "Name": "Maryam", "Class": "9th", "Age": 15, "Date of Birth": "27-10-2011"},
        {"Student ID": 13, "Name": "Hamza", "Class": "10th", "Age": 16, "Date of Birth": "11-01-2010"},
        {"Student ID": 14, "Name": "Ayesha", "Class": "8th", "Age": 14, "Date of Birth": "06-07-2012"},
        {"Student ID": 15, "Name": "Saad", "Class": "11th", "Age": 17, "Date of Birth": "19-03-2009"},
        {"Student ID": 16, "Name": "Noor", "Class": "9th", "Age": 15, "Date of Birth": "25-09-2011"},
        {"Student ID": 17, "Name": "Umer", "Class": "10th", "Age": 16, "Date of Birth": "08-02-2010"},
        {"Student ID": 18, "Name": "Sana", "Class": "8th", "Age": 14, "Date of Birth": "16-11-2012"},
        {"Student ID": 19, "Name": "Zain", "Class": "11th", "Age": 17, "Date of Birth": "29-06-2009"},
        {"Student ID": 20, "Name": "Hina", "Class": "9th", "Age": 15, "Date of Birth": "04-04-2011"},
    ]
    save_students()

# ---------------- Helper ----------------

def display_student(student):
    print("==================================================")
    print("Student ID:", student["Student ID"])
    print("Name:", student["Name"])
    print("Class:", student["Class"])
    print("Age:", student["Age"])
    print("Date of Birth:", student["Date of Birth"])
    print("==================================================")

# ---------------- CRUD Functions ----------------

def add_student():
    try:
        student_id = int(input("Enter the new Student ID: "))
    except ValueError:
        print("Invalid Student ID! Please enter a number.")
        return

    if student_id <= 0:
        print("Enter a valid Student ID!")
        return

    for student in students:
        if student["Student ID"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter the student name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return

    student_class = input("Enter the student class: ").strip()
    if student_class == "":
        print("Class cannot be empty!")
        return

    try:
        age = int(input("Enter the student age: "))
    except ValueError:
        print("Invalid Age! Please enter a number.")
        return

    if age <= 0:
        print("Age must be a positive number!")
        return

    dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
    if dob == "":
        print("Date of Birth cannot be empty!")
        return

    new_student = {
        "Student ID": student_id,
        "Name": name,
        "Class": student_class,
        "Age": age,
        "Date of Birth": dob
    }

    students.append(new_student)
    save_students()
    print("Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("No students in record!")
        return
    for student in students:
        display_student(student)


def search_student():
    search_choice = input("Search by 'ID' or 'Name': ").strip().lower()

    if search_choice == "id":
        try:
            search_id = int(input("Enter the Student ID: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            return

        found = False
        for student in students:
            if student["Student ID"] == search_id:
                display_student(student)
                found = True
                break
        if not found:
            print("Student Not Found!")

    elif search_choice == "name":
        search_name = input("Enter the Name: ").strip()
        if search_name == "":
            print("Name cannot be empty!")
            return

        found = False
        for student in students:
            if student["Name"].lower() == search_name.lower():
                display_student(student)
                found = True
                break
        if not found:
            print("Student Not Found!")

    else:
        print("Invalid choice! Please enter 'ID' or 'Name'.")


def update_student():
    try:
        search_id = int(input("Enter the Student ID to update: "))
    except ValueError:
        print("Invalid Student ID! Please enter a number.")
        return

    found = False
    for student in students:
        if student["Student ID"] == search_id:
            print("-" * 50)
            print("Current Student Details:")
            display_student(student)

            name = input("Enter new name (leave blank to keep current): ").strip()
            student_class = input("Enter new class (leave blank to keep current): ").strip()
            age_input = input("Enter new age (leave blank to keep current): ").strip()
            dob = input("Enter new Date of Birth (leave blank to keep current): ").strip()

            if name:
                student["Name"] = name
            if student_class:
                student["Class"] = student_class
            if age_input:
                try:
                    age = int(age_input)
                    if age <= 0:
                        print("Age must be positive! Keeping current age.")
                    else:
                        student["Age"] = age
                except ValueError:
                    print("Invalid Age! Keeping current age.")
            if dob:
                student["Date of Birth"] = dob

            save_students()
            print("Student Updated Successfully!")
            found = True
            break

    if not found:
        print("Student Not Found!")


def delete_student():
    try:
        search_id = int(input("Enter the Student ID to delete: "))
    except ValueError:
        print("Invalid Student ID! Please enter a number.")
        return

    found = False
    for student in students:
        if student["Student ID"] == search_id:
            confirm = input(f"Are you sure you want to delete {student['Name']}? (y/n): ").strip().lower()
            if confirm != "y":
                print("Deletion cancelled.")
                return
            students.remove(student)
            save_students()
            print("Student Deleted Successfully!")
            found = True
            break

    if not found:
        print("Student Not Found!")


def exit_system():
    print("---------------------------------------------------")
    print("Exiting the School Management System.")
    print("Thank you for using the system. Goodbye!")
    print("---------------------------------------------------")
    import sys
    sys.exit()

# ---------------- Main Menu ----------------

while True:
    print()
    print("=============== Select the Option (0-5) ===============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("0. Exit")

    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 0:
        exit_system()
    else:
        print("Invalid Choice! Choose between 0 to 5")