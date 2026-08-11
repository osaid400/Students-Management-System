# src/ models.py

class Student:
    def __init__(self, student_id, name, age, grade, date_of_birth, marks=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.date_of_birth = date_of_birth
        self.marks = marks if marks else {}

    def to_dict(self):
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Age": self.age,
            "Grade": self.grade,
            "Date of Birth": self.date_of_birth,
            "Marks": self.marks
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

    def generate_report_card(self):
        if not self.marks:
            return "No marks available to generate report card."
        
        total_marks = sum(self.marks.values())
        max_marks = len(self.marks) * 100
        percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
        
        if percentage >= 80:
            grade_letter = "A+"
        elif percentage >= 70:
            grade_letter = "A"
        elif percentage >= 60:
            grade_letter = "B"
        elif percentage >= 50:
            grade_letter = "C"
        else:
            grade_letter = "F"

        report = (
            f"\n{'='*40}\n"
            f"          REPORT CARD: {self.name.upper()}          \n"
            f"{'='*40}\n"
            f"Student ID : {self.student_id}\n"
            f"Grade/Class: {self.grade}\n"
            f"----------------------------------------\n"
        )
        for sub, score in self.marks.items():
            report += f"  - {sub:<15}: {score}/100\n"
        report += (
            f"----------------------------------------\n"
            f"Total Marks: {total_marks}/{max_marks}\n"
            f"Percentage : {percentage:.2f}%\n"
            f"Overall Grade: {grade_letter}\n"
            f"{'='*40}"
        )
        return report