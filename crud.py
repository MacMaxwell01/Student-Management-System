from database import connect


def add_student():
    matric = input("Matric Number: ")
    name = input("Full Name: ")
    email = input("Email: ")
    department = input("Department: ")
    faculty = input("Faculty: ")
    age = input("Age: ")

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO students VALUES(?,?,?,?,?,?)
        """, (matric, name, email, department, faculty, age))

        conn.commit()
        print("\nStudent added successfully.\n")

    except:
        print("\nMatric Number already exists.\n")

    conn.close()


def view_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("\nNo records found.\n")
    else:
        print("\n========== STUDENT RECORDS ==========")
        for row in rows:
            print(f"""
Matric     : {row[0]}
Name       : {row[1]}
Email      : {row[2]}
Department : {row[3]}
Faculty    : {row[4]}
Age        : {row[5]}
-----------------------------------------
""")

    conn.close()


def search_student():
    matric = input("Enter Matric Number: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE matric=?", (matric,))
    row = cursor.fetchone()

    if row:
        print(f"""
Matric     : {row[0]}
Name       : {row[1]}
Email      : {row[2]}
Department : {row[3]}
Faculty    : {row[4]}
Age        : {row[5]}
""")
    else:
        print("Student not found.")

    conn.close()


def update_student():
    matric = input("Enter Matric Number to update: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE matric=?", (matric,))
    row = cursor.fetchone()

    if row:

        name = input("New Name: ")
        email = input("New Email: ")
        department = input("New Department: ")
        faculty = input("New Faculty: ")
        age = input("New Age: ")

        cursor.execute("""
        UPDATE students
        SET
        name=?,
        email=?,
        department=?,
        faculty=?,
        age=?
        WHERE matric=?
        """, (name, email, department, faculty, age, matric))

        conn.commit()
        print("Record updated.")

    else:
        print("Student not found.")

    conn.close()


def delete_student():
    matric = input("Enter Matric Number: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE matric=?", (matric,))
    row = cursor.fetchone()

    if row:

        cursor.execute("DELETE FROM students WHERE matric=?", (matric,))
        conn.commit()

        print("Record deleted.")

    else:
        print("Student not found.")

    conn.close()