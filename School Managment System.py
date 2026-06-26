# SCHOOL MANAGEMENT SYSTEM: 

print("============ Welcome to School Managment System ============")

students = [
    {"Name" : "Ali", "Age": 15, "Roll Number": 3011},
    {"Name" : "Abdullah", "Age": 15, "Roll Number": 3012},
    {"Name" : "Ahmed", "Age": 16, "Roll Number": 3013},
    {"Name" : "Baqar", "Age": 14, "Roll Number": 3014},
    {"Name" : "Bilal", "Age": 15, "Roll Number": 3015},
    {"Name" : "Rida", "Age": 14, "Roll Number": 3016},
    {"Name" : "Sohiba", "Age": 17, "Roll Number": 3017},
    {"Name" : "Fabiha", "Age": 15, "Roll Number": 3018},
]


def add_student():
    name = input("Enter the new student name: ")
    age = int(input("Enter the new student age: "))
    roll_number = int(input("Enter the new student roll number: "))
    
    new_student = {
        "Name" : name,
        "Age" : age,
        "Roll Number" : roll_number
    }
    
    students.append(new_student)
    
    print("Student Added Successfully!")


def view_student():
    for student in students:
        print("==================================================")
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Roll Number:", student["Roll Number"])
        print("==================================================")


def search_student():
    search = int(input("Enter the roll number: "))
    found = False

    for student in students:
        if student["Roll Number"] == search:
            print("==================================================")
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Roll Number:", student["Roll Number"])
            print("==================================================")
            found = True
            break
    if found == False:
        print("Student Not Found")

     
def delete_student():
    search = int(input("Enter the roll number: "))
    found = False

    for student in students:
        if student["Roll Number"] == search:
            students.remove(student)
            print ("Student Delete Successfully!")
            found = True
            break
    if found == False:
        print("Student Not Found")

while True:
    print()
    print("=============== Select the Option ===============")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("0. Exit Student")

    choice = int(input("Enter the number: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 0:
        print("Good Bye!")
        break
    else:
        print("Invalid Choice!")