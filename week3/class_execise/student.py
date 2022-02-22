import random
import csv

class Student():

    def __init__(self, name, data_sheet, gender, image_url):
        self.name = name
        self.data_sheet = data_sheet
        self.gender = gender
        self.image_url = image_url

    def get_avg_grade(self):
        avg_grades_list = []
        avg_grade = 0
        for g in self.data_sheet.courses:
            avg_grades_list.append(g.grade)
            avg_grade += g.grade
        return avg_grade/len(avg_grades_list)

    def __str__(self):
        return f"Student name: {self.name}. Gender: {self.gender}. Course name: {self.data_sheet}."

class Data_sheet():
    
    def __init__(self, courses):
        self.courses = courses

    def get_grades(self):
        return [g.grade for g in self.courses]

class Course():
    
    def __init__(self,name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

    def __str__(self):
        return f"Course name: {self.name}. Teacher: {self.teacher}. ETCS: {self.ETCS}. Classroom: {self.classroom}. Grade: {self.grade}."

def random_generate(courses, numbers_of_students):
    list_of_names = ["August","Peter","Bo","Jens"]
    list_of_genders = ["Male","Female","Another"]
    list_of_students = []

    for student in range(numbers_of_students):
        number_of_courses = random.randint(1,len(courses))
        student = Student(random.choice(list_of_names), random.sample(courses,number_of_courses), random.choice(list_of_genders), "")
        list_of_students.append(student)
        
    return list_of_students

def write_students_to_csv(list_of_students):

    with open('list_of_students.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Gender", "Course name","Course teacher", "ETCS","Classroom","Grade" ], )
        writer.writeheader() 

        for student in list_of_students:
            for course in student.data_sheet:
                writer.writerow({"Name":student.name,"Gender":student.gender,"Course name": course.name, "Course teacher": course.teacher, "ETCS": course.ETCS, "Classroom": course.classroom, "Grade": course.grade})

if __name__ == '__main__':
    first_course = Course("August", "L1.05", "Thomas", 10, 12)
    second_course = Course("asd", "L1.321", "Daniel", 10, 7)
    third_course = Course("dqwe", "L1.23", "Kim", 10, 10)

    course_list = [first_course, second_course, third_course]

    sheet = Data_sheet([first_course,second_course,third_course])

    person = Student("August", sheet, "Male", "as")

    print(sheet.get_grades())
    print(person.get_avg_grade())
    students = random_generate(course_list,5)
    write_students_to_csv(students)
    