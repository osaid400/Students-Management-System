# School Management System

A console-based School Management System built with Python. This project demonstrates the use of functions, lists, dictionaries, loops, conditional statements, exception handling, and JSON-based file persistence to manage student records.

## Features

* Add a new student (with Student ID, Name, Class, Age, and Date of Birth)
* View all students
* Search a student by Student ID or Name
* Update student details
* Delete a student
* Prevent duplicate Student IDs
* Validate user input
* Persistent storage — student records are saved to a JSON file and reload automatically on the next run

## Technologies Used

* Python 3

## Concepts Covered

* Functions
* Lists
* Dictionaries
* Loops (`for`, `while`)
* Conditional Statements (`if`, `elif`, `else`)
* Exception Handling
* User Input
* Data Validation
* CRUD Operations
* String Methods (`strip()`, `lower()`)
* File Handling with JSON (`json.load()`, `json.dump()`)
* `os.path.exists()` for safe file loading

## Project Structure

```text
School-Management-System/
│
├── School Management System.py
├── .gitignore
└── README.md
```

> Note: `students.json` is created automatically when the program runs and stores student data locally. It is excluded from the repository via `.gitignore` since it holds runtime/test data rather than source code.

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

```text
============ Welcome to School Management System ============

=============== Select the Option (0-5) ===============
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
0. Exit
Enter the number: 3
Search by 'ID' or 'Name': ID
Enter the Student ID: 1
==================================================
Student ID: 1
Name: Ali
Class: 9th
Age: 15
Date of Birth: 12-03-2011
==================================================
```

## How Data Persistence Works

* On startup, the program checks if `students.json` exists using `os.path.exists()`.
* If it exists, all student records are loaded into memory using `json.load()`.
* If it doesn't exist, the program starts with a default set of sample students and saves them to `students.json`.
* Every time a student is added, updated, or deleted, the full student list is saved back to `students.json` using `json.dump()`, so no data is lost between runs.

## Future Improvements

* Add student marks and grades
* Sort students by class or age
* Export and import student records
* Migrate from JSON file storage to SQLite
* Implement Object-Oriented Programming (OOP)

## Learning Outcomes

This project helped me practice:

* Writing modular code using functions
* Managing data with lists and dictionaries
* Performing CRUD operations
* Searching records using different criteria
* Handling exceptions and validating user input
* Building a menu-driven console application
* Persisting data between program runs using JSON file handling

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400