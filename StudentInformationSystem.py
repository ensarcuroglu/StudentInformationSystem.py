import tkinter as tk
from tkinter import messagebox

student_list = []

class Student():
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.grades = {}

    def add_grade(self, lesson, grade):
        self.grades[lesson] = grade

    def get_average_grade(self):
        if not self.grades:
            return "No grades available."
        return sum(self.grades.values()) / len(self.grades)

class StudentInfoSystem:
    def __init__(self):
        self.student_list = []

    def add_student(self, first_name, last_name, number):
        student = Student(first_name, last_name, number)
        self.student_list.append(student)
        print("--------------------\nStudent added successfully.\n--------------------")

    def add_student_grade(self, number, lesson, grade):
        for student in self.student_list:
            if student.number == number:
                student.add_grade(lesson, grade)
                print(f"Grade added for {student.first_name} {student.last_name}.")
                break
        else:
            print("--------------------\nStudent not found.\n--------------------")

    def update_student(self, number):
        for student in self.student_list:
            if student.number == number:
                print("Student found.")
                student.first_name = input("Enter new name: ")
                student.last_name = input("Enter new lastname: ")
                print("Student information updated.")
                break
        else:
            print("--------------------\nStudent not found.\n--------------------")

    def show_students(self):
        print("\nStudent Informations:\n--------------------")
        for i, student in enumerate(self.student_list, start=1):
            print(f"{i}. Student:")
            print("First Name:", student.first_name)
            print("Last Name:", student.last_name)
            print("Number:", student.number)
            print("-" * 20)

    def delete_Student(self, number):
        for student in self.student_list:
            if student.number == number:
                self.student_list.remove(student)
                print(f"Student with number {number} deleted successfully.")
                break
        else:
            print("--------------------\nStudent not found.\n--------------------")

    def show_student_grades(self, number):
        for student in self.student_list:
            if student.number == number:
                print(f"\nGrades for {student.first_name} {student.last_name}:")
                for course, grade in student.grades.items():
                    print(f"{course}: {grade}")
                print(f"Average Grade: {student.get_average_grade()}")
                break
        else:
            print("--------------------\nStudent not found.\n--------------------")

    def show_class_average(self):
        if not self.student_list:
            print("There are no students in the system.")
            return

        grades = []
        for student in self.student_list:
            if student.grades:
                grades.extend(student.grades.values())

        if not grades:
            print("There is no note in the system.")
            return

        class_average = sum(grades) / len(grades)
        print(f"Class Average: {class_average}")
class StudentInformationSystemGUI:
    def __init__(self, master, information_system):
        self.master = master
        master.title("Student Information System")

        self.information_system = information_system

        self.label = tk.Label(master, text="Student Information System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.button_add_student = tk.Button(master, text="Add New Student", command=self.add_student)
        self.button_add_student.pack()

        self.button_add_grade = tk.Button(master, text="Add Grade", command=self.add_grade)
        self.button_add_grade.pack()

        self.button_delete_student = tk.Button(master, text="Delete Student", command=self.delete_student)
        self.button_delete_student.pack()

        self.button_exit = tk.Button(master, text="Exit", command=master.quit)
        self.button_exit.pack()

    def add_student(self):
        first_name = input("Enter the student's name: ")
        last_name = input("Enter the student's last name: ")
        number = input("Enter the student's number: ")

        self.information_system.add_student(first_name, last_name, number)
        messagebox.showinfo("Info", "Student added successfully.")

    def add_grade(self):
        number = input("Enter the student's number: ")
        lesson = input("Enter the lesson name: ")
        grade = float(input("Enter the grade: "))

        self.information_system.add_student_grade(number, lesson, grade)
        messagebox.showinfo("Info", "Grade added successfully.")

    def delete_student(self):
        number = input("Enter the number of the student you want to delete: ")
        message = self.information_system.delete_student(number)
        messagebox.showinfo("Info", message)





info_system = StudentInfoSystem()

root = tk.Tk()
app = StudentInformationSystemGUI(root, info_system)
root.mainloop()


while True:
    preference = int(input("\n1-Adding a New Student\n"
                           "2-Student Information Update\n"
                           "3-Showing Student Information\n"
                           "4-Add Student Grade\n"
                           "5-Delete Student\n"    
                           "6-Show Student Grades\n"
                           "7-Show Class Average\n"
                           "8-Exit\n"
                           "Please select the action you want to perform:\n"))

    if preference == 1:
        first_name = input("Enter the student's name: ")
        last_name = input("Enter the student's last name: ")
        number = int(input("Enter the student's number: "))
        info_system.add_student(first_name, last_name, number)
    elif preference == 2:
        number = int(input("Enter the number of the student you want to update: "))
        info_system.update_student(number)
    elif preference == 3:
        info_system.show_students()
    elif preference == 4:
        number = int(input("Enter the number of the student: "))
        lesson = input("Enter the lesson name: ")
        grade = float(input("Enter the grade: "))
        info_system.add_student_grade(number, lesson, grade)
    elif preference == 5:
        number = int(input("Enter the number of the student you want to delete:"))
        info_system.delete_Student(number)
    elif preference == 6:
        number = int(input("Enter the number of the student:"))
        info_system.show_student_grades(number)
    elif preference == 7:
        info_system.show_class_average()
    elif preference == 8:
        print("The program is terminating.")
        break
    else:
        print("Invalid selection. Please try again.")


