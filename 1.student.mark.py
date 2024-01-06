def student_call():
    s_name = []
    s_id = []
    s_DoB = []
    num_of_student = int(input())
    for i in range(num_of_student):
       s_name += [str(input())]
       s_id += [str(input())]
       s_DoB += [str(input())]
    print(s_name, s_id, s_DoB)

def course_call():
     c_name = []
     c_id = []
     num_of_courses = int(input())
     for i in range(num_of_courses):
       c_name += [str(input())]
       c_id += [str(input())]
     print(c_name, c_id)
student_call()
course_call()