import streamlit as st
import mysql.connector

# ----------------- Connect to MySQL -----------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saksham",
    database="school"
)
cursor = mydb.cursor()

# ----------------- App Title -----------------
st.title("shool Management app")

# ----------------- Sidebar Menu -----------------
menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

# ----------------- Add Student -----------------
if choice == "Add Student":
    st.subheader("Add New Student")
    
    with st.form("add_student_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=100)
        grade = st.text_input("Grade")
        submit = st.form_submit_button("Add Student")
        
        if submit:
            if not name or not grade:
                st.error("Name and Grade cannot be empty!")
            else:
                sql = "INSERT INTO school1 (name, age, grade) VALUES (%s, %s, %s)"
                val = (name, age, grade)
                cursor.execute(sql, val)
                mydb.commit()
                st.success(f"Student '{name}' added successfully!")

# ----------------- View Students -----------------
elif choice == "View Students":
    st.subheader("view All Students")
    cursor.execute("SELECT * FROM school1")
    data = cursor.fetchall()
    
    if data:
        students = [{"ID": row[0], "Name": row[1], "Age": row[2], "Grade": row[3]} for row in data]
        st.table(students)
    else:
        st.warning(" No students found!")

# ----------------- Update Student -----------------
elif choice == "Update Student":
    st.subheader("️ Update Student Info")
    
    with st.form("update_student_form"):
        student_id = st.number_input("Student ID", min_value=1)
        new_name = st.text_input("New Name")
        new_age = st.number_input("New Age", min_value=1, max_value=100)
        new_grade = st.text_input("New Grade")
        submit = st.form_submit_button("Update Student")
        
        if submit:
            if not new_name or not new_grade:
                st.error("️ Name and Grade cannot be empty!")
            else:
                sql = "UPDATE school1 SET name=%s, age=%s, grade=%s WHERE id=%s"
                val = (new_name, new_age, new_grade, student_id)
                cursor.execute(sql, val)
                mydb.commit()
                st.success(f" Student ID {student_id} updated successfully!")

# ----------------- Delete Student -----------------
elif choice == "Delete Student":
    st.subheader("Delete Student")
    
    with st.form("delete_student_form"):
        student_id = st.number_input("Student ID to Delete", min_value=1)
        submit = st.form_submit_button("Delete Student")
        
        if submit:
            confirm = st.checkbox("Confirm deletion")
            if confirm:
                sql = "DELETE FROM school1 WHERE id=%s"
                cursor.execute(sql, (student_id,))
                mydb.commit()
                st.success(f" Student ID {student_id} deleted successfully!")
            else:
                st.warning("️ Please confirm deletion by checking the box.")
