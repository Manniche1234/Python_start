class student():

    def __init__(self, data_sheet, gender, image_url):
        self.data_sheet = data_sheet
        self.gender = gender
        self.image_url = image_url


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

    sheet = Data_sheet([first_course,second_course,third_course])
    print(sheet.course[0].grade)
    print(sheet.get_grades())
    