from person import Person


class Professor(Person):

    def __init__(self, first, last, dob, address, salary):
        super().__init__(first, last, dob, address)
        self.salary = salary
        self.course = []
        self.got_raise = False

    def get_salary(self):
        return self.salary

    def add_course(self, course):
        from course import Course
        if isinstance(course, Course):
            self.course.append(course)
        else:
            raise TypeError("Invalid course parameter")

        if len(self.course) >= 3 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def get_name(self):
        return self.firstName + " " + self.lastName
