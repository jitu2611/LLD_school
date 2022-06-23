from student import Student


class Enroll:
    def __init__(self, student, course):
        from course import Course
        if not isinstance(course, Course):
            raise TypeError("Course error")

        if not isinstance(student, Student):
            raise TypeError("Student error")

        self.course = course
        self.grade = None
        self.student = student
        student.enrol_course(self)
        course.add_enroll(self)

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade if self.grade else 0

