from person import Person


class Student(Person):
    def __init__(self, first, last, dob, address, international=False):
        super().__init__(first, last, dob, address)
        self.internation = international
        self.enrolled = []

    def enrol_course(self, enroll):
        from enroll import Enroll
        if isinstance(enroll, Enroll):
            self.enrolled.append(enroll)
        else:
            raise TypeError("Invalid Enroll parameter passed")

    def is_part_time(self):
        return len(self.enrolled) < 2

    def isOnProbation(self):
        pass

    def get_name(self):
        return self.firstName+" "+self.lastName

    def get_average_grade(self):
        total_marks = 0
        for enroll in self.enrolled:
            total_marks += enroll.get_grade()

        return total_marks/len(self.enrolled) if len(self.enrolled) != 0 else 0
