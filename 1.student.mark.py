def student_call():
    s_name = []
    s_id = []
    s_DoB = []
    num_of_student = int(input())
    for i in range(num_of_student):
       s_name += [str(input("Your name here: "))]
       s_id += [str(input("Your student id here:"))]
       s_DoB += [str(input("Your DoB here:"))]
    print(s_name, s_id, s_DoB)

def course_call():
     c_name = []
     c_id = []
     num_of_courses = int(input())
     for i in range(num_of_courses):
       c_name += [str(input("Your course name here:" ))]
       c_id += [str(input("Your course id here:"))]
     print(c_name, c_id)
student_call()
course_call()