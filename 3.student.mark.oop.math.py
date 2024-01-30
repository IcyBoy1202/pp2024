import numpy as np
import math

class Student:
    def __init__(self):
        self.students = []

    def input(self):
        num_of_students = int(input("Number of students: "))
        for _ in range(num_of_students):
            name = input("Student name here: ")
            sid = input("Student id here: ")
            dob = input("Student DoB here: ")
            mark = float(input("Student mark here: "))
            mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
            self.students.append({"name": name, "id": sid, "dob": dob, "mark": mark})

    def list(self):
        for student in self.students:
            print("Name:", student["name"])
            print("ID:", student["id"])
            print("DoB:", student["dob"])
            print("Mark:", student["mark"])
            print()

    def find_student(self, name):
        for student in self.students:
            if student["name"] == name:
                return student
        return None

    def sort_by_gpa(self):
        gpa_list = [(student["name"], student["mark"]) for student in self.students]
        gpa_list.sort(key=lambda x: x[1], reverse=True)
        return gpa_list


class Course:
    def __init__(self):
        self.courses = []

    def input(self):
        num_of_courses = int(input("Number of courses: "))
        for _ in range(num_of_courses):
            name = input("Course name here: ")
            cid = input("Course id here: ")
            self.courses.append({"name": name, "id": cid})

    def list(self):
        for course in self.courses:
            print("Name:", course["name"])
            print("ID:", course["id"])
            print()


class MarkSystem:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses

    def mark_student(self):
        student_name = input("Enter the name of the student: ")
        student = self.students.find_student(student_name)
        if student:
            course_name = input("Enter the course name: ")
            for course in self.courses.courses:
                if course["name"] == course_name:
                    mark = float(input("Enter the mark: "))
                    mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
                    print("Mark {} recorded for student {} in course {}.".format(mark, student_name, course_name))
                    return
            print("Course not found.")
        else:
            print("Student not found.")


# Usage
students = Student()
courses = Course()

# Input students and courses
students.input()
courses.input()

# List students and courses
print("\nList of Students:")
students.list()
print("\nList of Courses:")
courses.list()

# Mark a student
mark_system = MarkSystem(students, courses)
mark_system.mark_student()

# Calculate and print average GPA for a given student
student_name = input("\nEnter the name of the student to calculate GPA: ")
student = students.find_student(student_name)
if student:
    total_marks = student["mark"]
    gpa = total_marks / len(student["mark"])  # Assuming all marks have equal weight
    print("Average GPA for student {}: {:.2f}".format(student_name, gpa))

# Sort students by GPA descending
sorted_students = students.sort_by_gpa()
print("\nStudents sorted by GPA (descending):")
for student in sorted_students:
    print("Name:", student[0])
    print("GPA:", student[1])
