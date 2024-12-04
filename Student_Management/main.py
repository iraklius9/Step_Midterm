from student import *


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Grade")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        choice = input("Enter your choice: ")
        students = Student.load_data()

        if choice == "1":
            try:
                name = input("\nEnter student's name: ").strip()
                grade = input("Enter grade: ").strip()
                if not name or not grade:
                    raise ValueError("Name and grade cannot be empty.")
                student = Student(name, grade)
                student.add_student(students)
            except ValueError as e:
                print(f"\nInvalid input: {e}\n")

        elif choice == "2":
            try:
                roll_number = int(input("\nEnter roll number to search: "))
                student = Student.search_student(roll_number, students)
                if student:
                    print(f"\nFound Student:\n{json.dumps(student, indent=4)}\n")
                else:
                    print("\nStudent not found.\n")
            except ValueError:
                print("\nRoll number must be an integer.\n")

        elif choice == "3":
            try:
                roll_number = int(input("\nEnter roll number to update grade: "))
                new_grade = input("Enter new grade: ").strip()
                if not new_grade:
                    raise ValueError("Grade cannot be empty.")
                Student.update_grade(roll_number, new_grade, students)
            except ValueError as e:
                print(f"\nInvalid input: {e}\n")

        elif choice == "4":
            try:
                roll_number = int(input("\nEnter roll number to delete: "))
                Student.delete_student(roll_number, students)
            except ValueError:
                print("\nRoll number must be an integer.\n")

        elif choice == "5":
            try:
                if not students:
                    print("\nNo students found.\n")
                else:
                    print("\nAll Students:")
                    Student.display_all(students)
            except AttributeError as e:
                print(
                    f"\nError: {e}. The 'display_all' method might not be defined correctly in the 'Student' class.\n")
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}\n")

        elif choice == "6":
            print("\nExiting the program.\n")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


main()
