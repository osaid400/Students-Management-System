# School Management System

A console-based **School Management System** built with Python using **Object-Oriented Programming (OOP)**. This project demonstrates clean class design, modular file structure, JSON-based data persistence, CRUD operations, attendance tracking, marks and report card generation, input validation, and exception handling — managing student records through dedicated classes.

## Features

* Add a new student (Student ID, Name, Grade, Age, and Date of Birth)
* View all students (filter by all classes or a specific grade)
* Search students by **Student ID**, **Name**, or **Grade**
* Update student details
* Delete a student
* Auto-assign Student IDs
* Attendance Calendar View (monthly, Present/Absent/Leave tracking)
* Marks & Report Card generation
* Export Report Card as a `.txt` file, organized into per-grade folders
* Validate user input
* Persistent storage using JSON
* Automatically reload saved student and attendance records on startup
* Clean Object-Oriented design using separate `Student`, `StudentManager`, and `SchoolUI` classes

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
* String Methods (`strip()`, `lower()`, `replace()`)
* File Handling with JSON (`json.load()`, `json.dump()`)
* `os.path.exists()`, `os.makedirs()`
* Working with the `calendar` module (`monthcalendar()`, `month_name`)
* Modules & Packages (multi-file project structure)

### Object-Oriented Programming (OOP)

* Classes & Objects
* Constructors (`__init__`)
* Instance Methods
* Class Methods (`@classmethod`)
* Encapsulation
* Object Serialization (`to_dict()` / `from_dict()`)
* Composition (`SchoolUI` uses `StudentManager`, which manages `Student` objects)

## Project Structure

```text
School-Management-System/
│
├── src/
│   ├── models.py       # Student class - data model, serialization, report card generation
│   ├── manager.py       # StudentManager class - CRUD, persistence, attendance logic
│   └── UI.py            # SchoolUI class - menu-driven user interaction
├── data/
│   ├── students.json          # Auto-created, stores student records
│   └── attendance_<year>.json # Auto-created, stores yearly attendance records
├── reports/                   # Auto-created, stores exported report card .txt files by grade
├── main.py                    # Entry point
├── .gitignore
└── README.md
```

> **Note:** `data/students.json` and `data/attendance_<year>.json` are automatically created when the program runs. They store runtime data locally and are excluded from the repository via `.gitignore`. The `reports/` folder is similarly auto-generated when report cards are exported.

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
python main.py
```

## Example Output

### Main Menu

```text
============ Welcome to School Management System ============

=============== Select the Option (0-8) ===============
1. Add Student
2. View All Students
3. Search Student (ID / Name / Grade)
4. Update Student
5. Delete Student
6. Attendance Calendar View
7. Marks & Report Card
8. Export Report Card (.txt)
0. Exit
```

### Searching a Student

```text
Search by 'ID', 'Name', or 'Grade': id

Enter the Student ID: 1

=========================== Grade 9th =========================
Student ID      Student Name         Age        Date of Birth
================================================================
1               Ali                  15         12-03-2010
================================================================
```

### Adding a Student

```text
Enter the student name: Ali
Enter the student Grade/Class: 9th
Enter the student age: 15
Enter Date of Birth (DD-MM-YYYY): 12-03-2010

Student Added Successfully! Auto-assigned ID: 1
```

### Viewing All Students

```text
View Options: 1. All Classes  2. Specific Class
Enter option: 1

=========================== Grade 9th =========================
Student ID      Student Name         Age        Date of Birth
================================================================
1               Ali                  15         12-03-2010
2               Sara                 14         05-07-2011
================================================================

=========================== Grade 10th ========================
Student ID      Student Name         Age        Date of Birth
================================================================
3               Bilal                16         21-01-2010
================================================================
```

### Updating a Student

```text
Enter the Student ID to update: 1
--------------------------------------------------
Current -> ID: 1, Name: Ali, Grade: 9th
--------------------------------------------------
Do you want to update this student? (y/n): y
Enter new name (leave blank to keep current): 
Enter new Grade (leave blank to keep current): 10th
Enter new age (leave blank to keep current): 
Enter new Date of Birth (leave blank to keep current): 

Student Updated Successfully!
```

### Deleting a Student

```text
Enter the Student ID to delete: 2
ID: 2 | Name: Sara | Grade: 9th
Are you sure you want to delete Sara? (y/n): y
------------------------------------------------------------
Student 'Sara' Deleted Successfully!
------------------------------------------------------------
```

### Attendance Calendar View

```text
Enter Student ID for Attendance: 1
Enter Month number (1 for Jan, 2 for Feb, ..., 12 for December): 3

=================================== MARCH 2026 ===================================
Student: Ali (ID: 1)           (P = Present, A = Absent, L = Leave)
----------------------------------------------------------------------------------
Mon         Tues      Wed       Thurs     Fri        Sat       Sun       
----------------------------------------------------------------------------------
                                          1 P        2 P       3 -       
4 P         5 P       6 A       7 P       8 P        9 -       10 -      
11 P        12 L      13 P      14 P      15 P       16 -      17 -      
18 P        19 P      20 P      21 A      22 P       23 -      24 -      
25 P        26 P      27 P      28 P      29 P       30 -      31 -      
==================================================================================

----------------- Monthly Attendance Summary -----------------
Total Days Opened: 22
Present: 19 | Absent: 2 | Leave: 1
=================================================================
```

### Marks & Report Card

```text
Enter Student ID: 1

=================================================================
                     REPORT CARD: ALI
=================================================================
Student ID : 1
Grade/Class: 9th
Date of Birth: 12-03-2010
-----------------------------------------------------------------
|   Subject       Obtained Marks   Total Marks   Grade   Remarks
  - Math           85               100           A+      Good
  - Science        78               100           A       Good
-----------------------------------------------------------------
Total Marks: 163/200
Percentage : 81.50%
Overall Grade: A+
=================================================================
```

### Exporting a Report Card

```text
Enter Student ID: 1

[Success] Report Card saved at: reports/9th/ali_1_result.txt
```

## How Data Persistence Works

* When the application starts, `StudentManager` checks whether `data/students.json` exists.
* If the file exists, all student records are loaded and converted into `Student` objects using `from_dict()`.
* If the file does not exist, an empty student list is created.
* Whenever a student is added, updated, or deleted, all `Student` objects are converted into dictionaries using `to_dict()` and saved back to `data/students.json`.
* Attendance data is stored separately, per year, in `data/attendance_<year>.json`, and loaded/saved on demand when marking or viewing attendance.
* This ensures that student, marks, and attendance records remain available even after closing and reopening the application.

## Future Improvements

* Prevent duplicate Student IDs on manual entry
* Sort students by Grade or Age
* Export full class list to CSV, not just individual report cards
* Confirmation prompt before overwriting an existing exported report card
* Track attendance trends across multiple months
* Store student records using SQLite
* Build a GUI version using Tkinter
* Add unit tests for `StudentManager` methods

## Learning Outcomes

This project helped me practice:

* Designing applications using Object-Oriented Programming
* Creating reusable classes and objects across multiple files (modules/packages)
* Applying Composition between classes
* Performing CRUD operations
* Managing persistent data using JSON across multiple data files
* Building scalable, menu-driven applications
* Implementing calendar-based attendance tracking
* Generating and exporting formatted report cards to text files
* Handling exceptions and validating user input
* Writing clean, maintainable, and modular Python code

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400