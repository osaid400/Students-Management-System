# src/models.py

from datetime import datetime

class Student:

    def __init__(self, student_id, name, age, grade, date_of_birth, marks=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.date_of_birth = date_of_birth
        self.marks = marks if marks else {}

    @classmethod
    def from_dict(cls, item):
        s_id = item.get("Student ID")
        name = item.get("Name")
        age = item.get("Age", 0)
        grade = item.get("Grade", "Unknown")
        dob = item.get("Date of Birth", "")
        marks = item.get("Marks", {})
        return cls(s_id, name, age, grade, dob, marks)

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

    def update_marks(self, subject, score):
        self.marks[subject] = score

    def generate_report_card(self):
        """Encapsulates report card text formatting inside the model."""
        if not self.marks:
            return None
        
        report = (
            f"{'='*65}\n"
            f"                     REPORT CARD: {self.name.upper()}          \n"
            f"{'='*65}\n"
            f"Student ID : {self.student_id}\n"
            f"Grade/Class: {self.grade}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"{'-'*65}\n"
            f"|   {'Subject':<12} {'Obtained Marks':<16} {'Total Marks':<13} {'Grade':<7} {'Remarks'}\n"
        )
        
        total_marks = 0
        max_marks = len(self.marks) * 100
        
        for sub, score in self.marks.items():
            total_marks += score
            if score >= 80: grade = "A+"
            elif score >= 70: grade = "A"
            elif score >= 60: grade = "B"
            elif score >= 50: grade = "C"
            else: grade = "F"
            
            rem = "Good" if score >= 60 else "Needs Improvement"
            report += f"  - {sub:<12} {score:<16} {100:<13} {grade:<7} {rem}\n"
        
        percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
        if percentage >= 80: overall_grade = "A+"
        elif percentage >= 70: overall_grade = "A"
        elif percentage >= 60: overall_grade = "B"
        elif percentage >= 50: overall_grade = "C"
        else: overall_grade = "F"

        report += (
            f"{'-'*65}\n"
            f"Total Marks: {total_marks}/{max_marks}\n"
            f"Percentage : {percentage:.2f}%\n"
            f"Overall Grade: {overall_grade}\n"
            f"{'='*65}"
        )
        return report