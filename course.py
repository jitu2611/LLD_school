from professor import Professor
from enroll import Enroll


class Course:
    def __init__(self, name, course_id, min_student, max_student, professor):
        self.name = name
        self.id = course_id
        self.minStudent = min_student
        self.maxStudent = max_student
        self.professor = []
        self.enrolls = []

        if isinstance(professor, Professor):
            self.professor.append(professor)
        elif isinstance(professor, list):
            for prof in professor:
                if not isinstance(prof, Professor):
                    raise TypeError("Prof Type error")
                else:
                    prof.add_course(self)

            self.professor = professor
        else:
            raise TypeError("Prof Type Error")

    def add_professor(self, prof):
        if isinstance(prof,Professor):
            self.professor.append(prof)
        else:
            raise TypeError("Prof Type Error")

    def add_enroll(self, enroll):
        if isinstance(enroll, Enroll):
            if len(self.enrolls) == self.maxStudent:
                raise Exception("Maximum no. of Student reached")
            self.enrolls.append(enroll)
        else:
            raise TypeError("Enroll type error")

    def is_active(self):
        return len(self.enrolls) >= self.minStudent

    def get_name(self):
        return self.name

    def get_profs(self):
        return self.professor
