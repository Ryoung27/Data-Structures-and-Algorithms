class Student:
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.course:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.course:
            self.courses.pop(course)
        else:
            print(f"{course} not found.")


courses_1 = ['Python', 'Node', 'Javascript']
course_2 = ['Java', 'Rails', 'C']
richie = Student('Richie', 'Young', courses_1)
# john = Student()
# john.first_name = 'Jon'
# john.last_name = 'Smith'
print(richie.first_name, richie.last_name, richie.courses)
