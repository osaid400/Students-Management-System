# src/manager.py

import json
import os
from datetime import datetime
from src.models import Student

class StudentManager:
    def __init__(self, filename="data/students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.students = [Student.from_dict(item) for item in data]
            except (json.JSONDecodeError, KeyError):
                print("Warning: Failed to parse students file. Starting fresh.")
                self.students = []
        else:
            self.students = []

    def save_students(self):
        with open(self.filename, "w") as file:
            data = [student.to_dict() for student in self.students]
            json.dump(data, file, indent=4)

    def _get_next_id(self):
        if not self.students:
            return 1
        return max(student.student_id for student in self.students) + 1

    def _get_attendance_filename(self, year=None):
        if year is None:
            year = datetime.now().year
        return f"data/attendance_{year}.json"

    def load_yearly_attendance(self, year=None):
        if year is None:
            year = datetime.now().year
        att_file = self._get_attendance_filename(year)
        if os.path.exists(att_file):
            try:
                with open(att_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_yearly_attendance(self, attendance_data, year=None):
        if year is None:
            year = datetime.now().year
        att_file = self._get_attendance_filename(year)
        with open(att_file, "w") as file:
            json.dump(attendance_data, file, indent=4)

    def mark_attendance_date(self, student_id, date_str, status, year=None):
        if year is None:
            year = datetime.now().year
        att_data = self.load_yearly_attendance(year)
        s_id_str = str(student_id)
        
        if s_id_str not in att_data:
            att_data[s_id_str] = {}
            
        att_data[s_id_str][date_str] = status.upper()
        self.save_yearly_attendance(att_data, year)
        return True

    def add_student(self, name, age, grade, date_of_birth):
        student_id = self._get_next_id()
        new_student = Student(student_id, name, age, grade, date_of_birth)
        self.students.append(new_student)
        self.save_students()
        return student_id

    def view_students(self):
        return self.students

    def search_by_id(self, search_id):
        for student in self.students:
            if student.student_id == search_id:
                return student
        return None

    def search_by_name(self, search_name):
        return [s for s in self.students if search_name.lower() in s.name.lower()]

    def search_by_grade(self, search_grade):
        return [s for s in self.students if s.grade.lower() == search_grade.lower()]

    def update_student(self, search_id, name=None, age=None, grade=None, date_of_birth=None):
        student = self.search_by_id(search_id)
        if student:
            student.update(name=name, age=age, grade=grade, date_of_birth=date_of_birth)
            self.save_students()
            return True
        return False

    def delete_student(self, search_id):
        student = self.search_by_id(search_id)
        if student:
            self.students.remove(student)
            self.save_students()
            return student
        return None

    def get_remarks(self, marks):
        if marks >= 90: return "Excellent"
        if marks >= 80: return "Very Good"
        if marks >= 70: return "Good"
        return "Need Improvement"

    def update_marks(self, search_id, subject, score):
        student = self.search_by_id(search_id)
        if student:
            student.update_marks(subject, score)
            self.save_students()
            return True
        return False