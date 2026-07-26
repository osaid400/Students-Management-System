# SCHOOL MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python

import json
import os
import sys

class Student:
    def __init__(self, student_id, name, age, grade, date_of_birth):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.date_of_birth = date_of_birth

    def __str__(self):
        return (
            f"{'-' * 50}\n"
            f"Student ID     : {self.student_id}\n"
            f"Name           : {self.name}\n"
            f"Age            : {self.age}\n"
            f"Grade          : {self.grade}\n"
            f"Date of Birth  : {self.date_of_birth}\n"
            f"{'-' * 50}"
        )

    def to_dict(self):
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Age": self.age,
            "Grade": self.grade,
            "Date of Birth": self.date_of_birth,
        }

    def update(self, name=None, age=None, grade=None, date_of_birth=None):
        if name and name.strip():
            self.name = name.strip()
        if age and str(age).strip():
            self.age = age
        if grade and grade.strip():
            self.grade = grade.strip()
        if date_of_birth and date_of_birth.strip():
            self.date_of_birth = date_of_birth.strip()


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.students = [
                        Student(
                            student_id = item["Student ID"],
                            name = item["Name"],
                            age = item["Age"],
                            grade = item["Grade"],
                            date_of_birth = item["Date of Birth"],
                        )
                        for item in data
                    ]
            except (json.JSONDecodeError, KeyError):
                print("Warning: Failed to parse students file. Starting fresh.")
                self.students = []
        else:
            self.students = []

    def save_students(self):
        with open(self.filename, "w") as file:
            data = [student.to_dict() for student in self.students]
            json.dump(data, file, indent=2)

    def add_student(self):
        try:
            student_id = int(input("Enter the new Student ID: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            return

        if student_id <= 0:
            print("Enter a valid Student ID!")
            return

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter the student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        grade = input("Enter the student Grade: ").strip()
        if not grade:
            print("Grade cannot be empty!")
            return

        try:
            age = int(input("Enter the student age: "))
        except ValueError:
            print("Invalid Age! Please enter a number.")
            return

        if age <= 0:
            print("Age must be a positive number!")
            return

        date_of_birth = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
        if not date_of_birth:
            print("Date of Birth cannot be empty!")
            return

        new_student = Student(student_id, name, age, grade, date_of_birth)
        self.students.append(new_student)
        self.save_students()
        print("Student Added Successfully!")

    def view_students(self):
        if not self.students:
            print("-" * 60)
            print("No students in record!")
            print("-" * 60)
            return
        for student in self.students:
            print(student)

    def search_student(self):
        search_choice = input("Search by 'ID' or 'Name': ").strip().lower()

        if search_choice == "id":
            try:
                search_id = int(input("Enter the Student ID: "))
            except ValueError:
                print("Invalid Student ID! Please enter a number.")
                return

            found = False
            for student in self.students:
                if student.student_id == search_id:
                    print(student)
                    found = True
                    break
            if not found:
                print("Student Not Found!")

        elif search_choice == "name":
            search_name = input("Enter the Name: ").strip()
            if not search_name:
                print("Name cannot be empty!")
                return

            found = False
            for student in self.students:
                if student.name.lower() == search_name.lower():
                    print(student)
                    found = True
                    break
            if not found:
                print("Student Not Found!")

        else:
            print("Invalid choice! Please enter 'ID' or 'Name'.")

    def update_student(self):
        try:
            search_id = int(input("Enter the Student ID to update: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            return

        found = False
        for student in self.students:
            if student.student_id == search_id:
                print("-" * 50)
                print("Current Student Details:")
                print(student)

                name = input("Enter new name (leave blank to keep current): ").strip()
                grade = input("Enter new Grade (leave blank to keep current): ").strip()
                age_input = input("Enter new age (leave blank to keep current): ").strip()
                date_of_birth = input("Enter new Date of Birth (leave blank to keep current): ").strip()

                parsed_age = None
                if age_input:
                    try:
                        parsed_age = int(age_input)
                        if parsed_age <= 0:
                            print("Age must be positive! Keeping current age.")
                            parsed_age = None
                    except ValueError:
                        print("Invalid Age! Keeping current age.")

                student.update(
                    name=name if name else None,
                    age=parsed_age,
                    grade=grade if grade else None,
                    date_of_birth=date_of_birth if date_of_birth else None,
                )

                self.save_students()
                print("Student Updated Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found!")

    def delete_student(self):
        try:
            search_id = int(input("Enter the Student ID to delete: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            return

        found = False
        for student in self.students:
            if student.student_id == search_id:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ").strip().lower()
                if confirm != "y":
                    print("Deletion cancelled.")
                    return
                self.students.remove(student)
                self.save_students()
                print("-" * 60)
                print("Student Deleted Successfully!")
                print("-" * 60)
                found = True
                break

        if not found:
            print("Student Not Found!")

# ---------------- Main Menu ----------------

def main():
    print("============ Welcome to School Management System ============")
    manager = StudentManager()

    while True:
        print("\n=============== Select the Option (0-5) ===============")
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
            manager.add_student()
        elif choice == 2:
            manager.view_students()
        elif choice == 3:
            manager.search_student()
        elif choice == 4:
            manager.update_student()
        elif choice == 5:
            manager.delete_student()
        elif choice == 0:
            print("---------------------------------------------------")
            print("Exiting the School Management System.")
            print("Thank you for using the system. Goodbye!")
            print("---------------------------------------------------")
            sys.exit()
        else:
            print("Invalid Choice! Choose between 0 to 5")

main()