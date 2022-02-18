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
        for g in self.data_sheet.course:
            avg_grades_list.append(g.grade)
            avg_grade += g.grade
        return avg_grade/len(avg_grades_list)

    def __str__(self):
        return f"Student name: {self.name}. Gender: {self.gender}. Course name: {self.data_sheet.name}. Teacher: {self.data_sheet.teacher}. ETCS: {self.data_sheet.ETCS}. Classroom: {self.data_sheet.classroom}. Grade: {self.data_sheet.grade}. "

    def random_generate(self, course, numbers_of_students):
        list_of_names = ["August","Peter","Bo","Jens"]
        list_of_genders = ["Male","Female","Another"]
        list_of_students = []

        f = open('list_of_students.csv', 'w', newline='')
        writer = csv.writer(f)

        for student in range(numbers_of_students):
            student = Student(random.choice(list_of_names), random.choice(course), random.choice(list_of_genders), "")
            list_of_students.append(student)

        writer.writerow(list_of_students) 
        f.close()
        return list_of_students

    
class Data_sheet():
    
    def __init__(self, course):
        self.course = course

    def get_grades(self):
        grades = [] 
        for g in self.course:
            grades.append(g.grade)     
        return grades

class Course():
    
    def __init__(self,name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

if __name__ == '__main__':
    first_course = Course("August", "L1.05", "Thomas", 10, 12)
    second_course = Course("asd", "L1.321", "Daniel", 10, 7)
    third_course = Course("dqwe", "L1.23", "Kim", 10, 10)

    course_list = [first_course, second_course, third_course]

    sheet = Data_sheet([first_course,second_course,third_course])

    person = Student("August", sheet, "Male", "as")

    print(sheet.get_grades())
    print(person.get_avg_grade())
    print(person.random_generate(course_list,5))
    
    