class Student:
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

courses_1 = ['Python', 'Node', 'Javascript']
course_2 = ['Java', 'Rails', 'C']
richie = Student('Richie', 'Young', courses_1)
# john = Student()
# john.first_name = 'Jon'
# john.last_name = 'Smith'
print(richie.first_name, richie.last_name, richie.courses)
