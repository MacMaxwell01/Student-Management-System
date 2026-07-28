from database import create_table
from crud import *
from export import export_to_txt



create_table()


while True:

    print("""
===============================
          WELCOME TO 
 THE STUDENT MANAGEMENT SYSTEM
===============================
What option would you like to pick:
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Export to TXT
7. Exit

""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        export_to_txt()

    elif choice == "7":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice.")