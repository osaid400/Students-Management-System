# School Management System

A console-based **School Management System** built with Python using **Object-Oriented Programming (OOP)**. This project demonstrates clean class design, JSON-based data persistence, CRUD operations, input validation, exception handling, and composition by managing student records through dedicated classes.

## Features

* Add a new student (Student ID, Name, Grade, Age, and Date of Birth)
* View all students
* Search students by **Student ID** or **Name**
* Update student details
* Delete a student
* Prevent duplicate Student IDs
* Validate user input
* Persistent storage using JSON
* Automatically reload saved student records on startup
* Clean Object-Oriented design using separate `Student` and `StudentManager` classes

## Technologies Used

* Python 3
* JSON

## Concepts Covered

### Python Fundamentals

* Functions
* Loops (`for`, `while`)
* Conditional Statements
* Exception Handling
* User Input
* Data Validation
* CRUD Operations
* String Methods (`strip()`, `lower()`)
* File Handling with JSON (`json.load()`, `json.dump()`)
* `os.path.exists()`

### Object-Oriented Programming (OOP)

* Classes & Objects
* Constructors (`__init__`)
* Instance Methods
* Encapsulation
* Object Serialization (`to_dict()`)
* Magic Method (`__str__()`)
* Composition

## Project Structure

```text
School-Management-System/
│
├── School Management System.py
├── .gitignore
└── README.md
```

> **Note:** `students.json` is automatically created when the program runs. It stores student records locally and is excluded from the repository via `.gitignore` because it contains runtime data rather than source code.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/osaid400/School-Management-System.git
```

2. Navigate to the project folder:

```bash
cd School-Management-System
```

3. Run the program:

```bash
python "School Management System.py"
```

## Example Output

### Main Menu

```text
============ Welcome to School Management System ============

=============== Select the Option (0-5) ===============
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
0. Exit
```

### Searching a Student

```text
Search by 'ID' or 'Name': ID

Enter the Student ID: 1

--------------------------------------------------
Student ID     : 1
Name           : Ali
Age            : 15
Grade          : 9th
Date of Birth  : 12-03-2010
--------------------------------------------------
```

## How Data Persistence Works

* When the application starts, it checks whether `students.json` exists.
* If the file exists, all student records are loaded and converted into `Student` objects.
* If the file does not exist, an empty student list is created.
* Whenever a student is added, updated, or deleted, all student objects are converted into dictionaries using `to_dict()` and saved back to `students.json`.
* This ensures that student records remain available even after closing and reopening the application.

## Future Improvements

* Search students by Grade
* Sort students by Grade or Age
* Export student records to CSV
* Import student records from CSV
* Store student records using SQLite
* Build a GUI version using Tkinter
* Add attendance management
* Add marks and report card generation

## Learning Outcomes

This project helped me practice:

* Designing applications using Object-Oriented Programming
* Creating reusable classes and objects
* Applying Composition between classes
* Using the `__str__()` magic method
* Performing CRUD operations
* Managing persistent data using JSON
* Building scalable menu-driven applications
* Handling exceptions and validating user input
* Writing clean, maintainable, and modular Python code

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
