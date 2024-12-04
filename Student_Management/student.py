import json
import os


class Student:
    data_file = "students.json"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.roll_number = self.generate_roll_number()

    @staticmethod
    def load_data():
        if os.path.exists(Student.data_file):
            with open(Student.data_file, "r") as file:
                return json.load(file)
        return []

    @staticmethod
    def save_data(data):
        with open(Student.data_file, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def generate_roll_number():
        students = Student.load_data()
        if students:
            max_roll_number = max(student["roll_number"] for student in students)
        else:
            max_roll_number = 0
        return max_roll_number + 1

    def add_student(self, students):
        if any(student["roll_number"] == self.roll_number for student in students):
            print(f"\nError: A student with roll number {self.roll_number} already exists.\n")
            return

        students.append({
            "name": self.name,
            "roll_number": self.roll_number,
            "grade": self.grade
        })
        Student.save_data(students)
        print(f"\nStudent {self.name} added successfully with roll number {self.roll_number}.\n")

    @staticmethod
    def search_student(roll_number, students):
        for student in students:
            if student["roll_number"] == roll_number:
                return student
        return None

    @staticmethod
    def update_grade(roll_number, new_grade, students):
        for student in students:
            if student["roll_number"] == roll_number:
                student["grade"] = new_grade
                Student.save_data(students)
                print(f"\nGrade updated to {new_grade} for student {student['name']}.\n")
                return
        print(f"\nStudent with roll number {roll_number} not found.\n")

    @staticmethod
    def delete_student(roll_number, students):
        for student in students:
            if student["roll_number"] == roll_number:
                students.remove(student)
                Student.save_data(students)
                print(f"\nStudent with roll number {roll_number} deleted successfully.\n")
                return
        print(f"\nStudent with roll number {roll_number} not found.\n")

    @staticmethod
    def display_all(students):
        if not students:
            print("\nNo students to display.\n")
        else:
            print()
            for student in students:
                print(
                    f"Name: {student['name']:<8} Roll Number: {student['roll_number']:<5} Grade: {student['grade']:<5}")
            print()
