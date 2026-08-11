# src/UI.py

import sys
import calendar
import json
from src.models import Student
from src.manager import StudentManager

class SchoolUI:

    def __init__(self):
        self.manager = StudentManager()

    def run(self):
        print("============ Welcome to School Management System ============")
        while True:
            print("\n=============== Select the Option (0-7) ===============")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student (ID / Name / Grade)")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Attendance Calendar View")
            print("7. Marks & Report Card")
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
            elif choice == 0:
                print("---------------------------------------------------")
                print("Exiting the School Management System. Goodbye!")
                print("---------------------------------------------------")
                sys.exit()
            else:
                print("Invalid Choice! Choose between 0 to 7")

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

        grades_dict = {}
        for student in students:
            grade = student.grade
            if grade not in grades_dict:
                grades_dict[grade] = []
            grades_dict[grade].append(student)

        for grade, std_list in grades_dict.items():
            print(f"\n========================== Grade {grade} ========================")
            print(f"{'Student ID':<15} {'Student Name':<20} {'Age':<10} {'Date of Birth':<15}")
            print("=" * 60)
            for student in std_list:
                print(f"{str(student.student_id):<15} {student.name:<20} {str(student.age):<10} {student.date_of_birth:<15}")
            print("=" * 60)

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
                # Single student ko bhi table format mein print karne ke liye
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
            # Flexible search taake '10' likhne par '10th' ya 'Grade 10' bhi aa jaye
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

        # Filter records specifically for the chosen month
        month_prefix = f"{year}-{month:02d}-"
        monthly_records = {k: v for k, v in student_records.items() if k.startswith(month_prefix)}

        # Monthly Attendance Summary
        total_days = list(monthly_records.values())
        present = total_days.count("P")
        absent = total_days.count("A")
        leave = total_days.count("L")
        
        print("\n----------------- Monthly Attendance Summary -----------------")
        print(f"Total Days Opened: {len(total_days)}")
        print(f"Present: {present} | Absent: {absent} | Leave: {leave}")
        print("=================================================================")

    def handle_view_students_table(self):
        students = self.manager.view_students()
        if not students:
            print("No students found!")
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
            # All classes
            grades_dict = {}
            for s in students:
                grades_dict.setdefault(s.grade, []).append(s)
            self._print_student_table(grades_dict)

    def _print_student_table(self, grades_dict):
        for grade, std_list in grades_dict.items():
            print(f"\n============================ Grade {grade} ===========================")
            print(f"{'Student ID':<15} {'Student Name':<20} {'Age':<10} {'Date of Birth':<15}")
            print("=" * 64)
            for s in std_list:
                print(f"{str(s.student_id):<15} {s.name:<20} {str(s.age):<10} {s.date_of_birth:<15}")
            print("=" * 64)

    def handle_marks(self):
        try:
            s_id = input("Enter Student ID: ")
            student = self.manager.search_by_id(int(s_id))
            if not student:
                print("Student not found!")
                return
            
            # Load marks from JSON
            with open("data/marks.json", "r") as f:
                all_marks = json.load(f)
            
            student_marks = all_marks.get(s_id, {})
            
            for exam in ["First Term Exam", "Mid Term Exam", "Final Term Exam"]:
                data = student_marks.get(exam)
                if not data:
                    continue
                
                print(f"\n===================== {exam.upper()} ======================")
                
                if isinstance(data, str): # For Final Term if stored as a status string
                    print(f"Status: {data}")
                else:
                    print(f"{'Subject':<15} {'Marks':<10} {'Grade':<10} {'Remarks'}")
                    print("-" * 60)
                    
                    total_marks = 0
                    max_marks = len(data) * 100 # Har subject 100 marks ka hai
                    
                    for sub, score in data.items():
                        total_marks += score
                        
                        # Individual Subject Grade logic
                        if score >= 80:
                            grade = "A+"
                        elif score >= 70:
                            grade = "A"
                        elif score >= 60:
                            grade = "B"
                        elif score >= 50:
                            grade = "C"
                        else:
                            grade = "F"
                            
                        # Remarks logic
                        if score >= 60: 
                            rem = "Good"
                        else: 
                            rem = "Needs Improvement"
                            
                        print(f"{sub:<15} {score:<10} {grade:<10} {rem}")
                        
                    # Calculate Percentage and Overall Grade
                    percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
                    
                    if percentage >= 80:
                        overall_grade = "A+"
                    elif percentage >= 70:
                        overall_grade = "A"
                    elif percentage >= 60:
                        overall_grade = "B"
                    elif percentage >= 50:
                        overall_grade = "C"
                    else:
                        overall_grade = "F"
                        
                    print("-" * 60)
                    print(f"Percentage: {percentage:.2f}%                    Overall Grade: {overall_grade}")
                    print("============================================================")
                    
        except FileNotFoundError:
            print("Marks data file not found!")