# src/UI.py

import sys
import calendar
import os
from src.models import Student
from src.manager import StudentManager

class SchoolUI:

    def __init__(self):
        self.manager = StudentManager()

    def run(self):
        print("============ Welcome to School Management System ============")
        while True:
            print("\n=============== Select the Option (0-8) ===============")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student (ID / Name / Grade)")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Attendance Calendar View")
            print("7. Marks & Report Card")
            print("8. Export Report Card (.txt)")
            print("0. Exit")

            try:
                choice = int(input("Enter the number: "))
            except ValueError:
                print("Invalid Choice! Please enter a number.")
                continue

            if choice == 1:
                self.handle_add_student()
            elif choice == 2:
                self.handle_view_students_table()
            elif choice == 3:
                self.handle_search_student()
            elif choice == 4:
                self.handle_update_student()
            elif choice == 5:
                self.handle_delete_student()
            elif choice == 6:
                self.handle_attendance_calendar()
            elif choice == 7:
                self.handle_marks()
            elif choice == 8:
                self.handle_export_report_card()
            elif choice == 0:
                print("---------------------------------------------------")
                print("Exiting the School Management System. Goodbye!")
                print("---------------------------------------------------")
                sys.exit()
            else:
                print("Invalid Choice! Choose between 0 to 8")

    def handle_add_student(self):
        name = input("Enter the student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        grade = input("Enter the student Grade/Class: ").strip()
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

        new_id = self.manager.add_student(name, age, grade, date_of_birth)
        print(f"Student Added Successfully! Auto-assigned ID: {new_id}")

    def handle_view_students_table(self):
        students = self.manager.view_students()
        if not students:
            print("-" * 60)
            print("No students in record!")
            print("-" * 60)
            return

        print("\nView Options: 1. All Classes  2. Specific Class")
        choice = input("Enter option: ")

        if choice == "2":
            grade_input = input("Enter Grade to filter: ").strip()
            filtered = [s for s in students if grade_input.lower() in s.grade.lower()]
            if not filtered:
                print("No students found in this grade.")
                return
            self._print_student_table({grade_input: filtered})
        else:
            grades_dict = {}
            for s in students:
                grades_dict.setdefault(s.grade, []).append(s)
            self._print_student_table(grades_dict)

    def _print_student_table(self, grades_dict):
        for grade, std_list in grades_dict.items():
            print(f"\n=========================== Grade {grade} =========================")
            print(f"{'Student ID':<15} {'Student Name':<20} {'Age':<10} {'Date of Birth':<15}")
            print("=" * 64)
            for s in std_list:
                print(f"{str(s.student_id):<15} {s.name:<20} {str(s.age):<10} {s.date_of_birth:<15}")
            print("=" * 64)

    def handle_search_student(self):
        search_choice = input("Search by 'ID', 'Name', or 'Grade': ").strip().lower()

        if search_choice == "id":
            try:
                search_id = int(input("Enter the Student ID: "))
            except ValueError:
                print("Invalid Student ID! Please enter a number.")
                return
            student = self.manager.search_by_id(search_id)
            if student:
                self._print_student_table({student.grade: [student]})
            else:
                print("-" * 64)
                print("Student Not Found!")
                print("-" * 64)

        elif search_choice == "name":
            search_name = input("Enter the Name: ").strip()
            if not search_name:
                print("Name cannot be empty!")
                return
            results = self.manager.search_by_name(search_name)
            if results:
                grades_dict = {}
                for student in results:
                    grades_dict.setdefault(student.grade, []).append(student)
                self._print_student_table(grades_dict)
            else:
                print("-" * 64)
                print("Student Not Found!")
                print("-" * 64)

        elif search_choice == "grade":
            search_grade = input("Enter the Grade/Class: ").strip()
            if not search_grade:
                print("Grade cannot be empty!")
                return
            all_students = self.manager.view_students()
            results = [s for s in all_students if search_grade.lower() in s.grade.lower()]
            
            if results:
                grades_dict = {}
                for student in results:
                    grades_dict.setdefault(student.grade, []).append(student)
                self._print_student_table(grades_dict)
            else:
                print("-" * 64)
                print("No students found in this grade!")
                print("-" * 64)
        else:
            print("Invalid choice!")

    def handle_update_student(self):
        try:
            search_id = int(input("Enter the Student ID to update: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            return

        student = self.manager.search_by_id(search_id)
        if not student:
            print("Student Not Found!")
            return

        print("-" * 50)
        print(f"Current -> ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")
        print("-" * 50)

        confirm = input("Do you want to update this student? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Update cancelled.")
            return

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

        success = self.manager.update_student(
            search_id,
            name=name if name else None,
            age=parsed_age,
            grade=grade if grade else None,
            date_of_birth=date_of_birth if date_of_birth else None,
        )
        if success:
            print("Student Updated Successfully!")

    def handle_delete_student(self):
        try:
            search_id = int(input("Enter the Student ID to delete: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            return

        student = self.manager.search_by_id(search_id)
        if not student:
            print("Student Not Found!")
            return

        print(f"ID: {student.student_id} | Name: {student.name} | Grade: {student.grade}")
        confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ").strip().lower()
        if confirm != "y":
            print("Deletion cancelled.")
            return

        deleted = self.manager.delete_student(search_id)
        if deleted:
            print("-" * 60)
            print(f"Student '{deleted.name}' Deleted Successfully!")
            print("-" * 60)

    def handle_attendance_calendar(self):
        try:
            s_id = int(input("Enter Student ID for Attendance: "))
        except ValueError:
            print("Invalid ID format!")
            return

        student = self.manager.search_by_id(s_id)
        if not student:
            print("Student not found!")
            return

        try:
            month = int(input("Enter Month number (1 for Jan, 2 for Feb, ..., 12 for December): "))
            if month < 1 or month > 12:
                print("Invalid month!")
                return
        except ValueError:
            print("Invalid month format!")
            return

        year = 2026
        month_name = calendar.month_name[month].upper()
        
        yearly_data = self.manager.load_yearly_attendance(year)
        student_records = yearly_data.get(str(s_id), {})

        print(f"\n======================= {month_name} {year} ============================")
        print(f"Student: {student.name} (ID: {student.student_id})           (P = Present, A = Absent, L = Leave)")
        print("-" * 85)
        print(f"{'Mon':<12} {'Tues':<10} {'Wed':<10} {'Thurs':<10} {'Fri':<11} {'Sat':<10} {'Sun':<10}")
        print("-" * 85)

        cal = calendar.monthcalendar(year, month)
        for week in cal:
            row_str = ""
            for day in week:
                if day == 0:
                    row_str += f"{'':<12}"
                else:
                    date_str = f"{year}-{month:02d}-{day:02d}"
                    status = student_records.get(date_str, "-")
                    cell = f"{day} {status}"
                    row_str += f"{cell:<12}"
            print(row_str)
        print("=" * 85)

        month_prefix = f"{year}-{month:02d}-"
        monthly_records = {k: v for k, v in student_records.items() if k.startswith(month_prefix)}

        total_days = list(monthly_records.values())
        present = total_days.count("P")
        absent = total_days.count("A")
        leave = total_days.count("L")
        
        print("\n----------------- Monthly Attendance Summary -----------------")
        print(f"Total Days Opened: {len(total_days)}")
        print(f"Present: {present} | Absent: {absent} | Leave: {leave}")
        print("=================================================================")

    def handle_marks(self):
        # Narrowed try-except scope exclusively around input parsing
        try:
            s_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID format!")
            return

        student = self.manager.search_by_id(s_id)
        if not student:
            print("Student not found!")
            return
        
        report_output = student.generate_report_card()
        if not report_output:
            print("No marks record found for this student!")
            return
            
        print(report_output)

    def handle_export_report_card(self):
        try:
            s_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID format!")
            return

        student = self.manager.search_by_id(s_id)
        if not student:
            print("Student not found!")
            return

        report_output = student.generate_report_card()
        if not report_output:
            print("No marks record found for this student!")
            return

        grade_folder = student.grade.replace(" ", "_").lower()
        output_dir = os.path.join("reports", grade_folder)
        os.makedirs(output_dir, exist_ok=True)

        clean_name = student.name.replace(" ", "_").lower()
        filename = f"{clean_name}_{student.student_id}_result.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(report_output)
        
        print(f"\n[Success] Report Card saved at: {filepath}")