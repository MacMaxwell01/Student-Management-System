from database import connect


def export_to_txt():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    with open("students.txt", "w") as file:

        file.write("STUDENT RECORDS\n")
        file.write("=" * 60 + "\n\n")

        for row in rows:
            file.write(f"""
Matric Number : {row[0]}
Name          : {row[1]}
Email         : {row[2]}
Department    : {row[3]}
Faculty       : {row[4]}
Age           : {row[5]}
--------------------------------------------------
""")

    conn.close()

    print("\nData exported successfully to students.txt\n")