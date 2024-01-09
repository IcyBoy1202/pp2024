'''
class Student:
    def __init__(self):
        self.sname = []
        self.sid = []
        self.sDoB = []

class Course:
    def __init__(self):
        self.cname = []
        self.cid = []

def student_info(s):
    num_of_student = int(input("Number of students: "))
    for i in range(num_of_student):
        s.sname.append(str(input("Student name here: ")))
        s.sid.append(str(input("Student id here: ")))
        s.sDoB.append(str(input("Student DoB here: ")))
    print(s.sname, s.sid, s.sDoB)

def course_info(c):
    num_of_courses = int(input("Number of courses: "))
    for i in range(num_of_courses):
        c.cname.append(str(input("Course name here: ")))
        c.cid.append(str(input("Course id here: ")))
    print(c.cname, c.cid)

def student_call(self):
    search_student = input("Student you want to call: ")
    if search_student := self.sname:
      search_course = input("Enter the course to type that student mark: ")
      if search_course := self.cname:
          input_mark = input("Enter the mark: ")
          print ("The student mark is: ", input_mark)
    else:
      print("failure")

# Create instances of Student and Course classes
student_data = Student()
course_data = Course()


# Call functions with instances as arguments
student_info(student_data)
course_info(course_data)
student_call(student_data) '''
class Student:
    def __init__(self):
        self.sname = []
        self.sid = []
        self.sDoB = []

class Course:
    def __init__(self):
        self.cname = []
        self.cid = []

def student_info(s):
    num_of_student = int(input("Number of students: "))
    for i in range(num_of_student):
        s.sname.append(str(input("Student name here: ")))
        s.sid.append(str(input("Student id here: ")))
        s.sDoB.append(str(input("Student DoB here: ")))
    print(s.sname, s.sid, s.sDoB)

def course_info(c):
    num_of_courses = int(input("Number of courses: "))
    for i in range(num_of_courses):
        c.cname.append(str(input("Course name here: ")))
        c.cid.append(str(input("Course id here: ")))
    print(c.cname, c.cid)

def student_call(s, c):
    search_student = input("Student you want to call: ")
    if search_student in s.sname:
        search_course = input("Enter the course to type that student mark: ")
        if search_course in c.cname:
            input_mark = input("Enter the mark: ")
            print("The student mark is:", input_mark)
        else:
            print("Course not found.")
    else:
        print("Student not found.")

# Create instances of Student and Course classes
student_data = Student()
course_data = Course()

# Call functions with instances as arguments
student_info(student_data)
course_info(course_data)
student_call(student_data, course_data)
