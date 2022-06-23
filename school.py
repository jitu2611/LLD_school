from student import Student
from professor import Professor
from course import Course


class School:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = []

    def add_student(self,student):
        if not isinstance(student, Student):
            raise TypeError
        self.students.append(student)

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError
        self.courses.append(course)

    def add_prof(self, prof):
        if not isinstance(prof, Professor):
            raise TypeError("error")
        self.professors.append(prof)

    def get_all_courses(self):
        course_list = []
        for courses in self.courses:
            course_list.append(courses.get_name())
        return course_list

    def course_teaches(self):
        course_prof = {}
        for course in self.courses:
            prof_list = course.get_profs()
            course_prof[course.get_name()] = []
            for prof in prof_list:
                course_prof[course.get_name()].append(prof.get_name())

        return course_prof

    def get_active_course(self):
        active_course = []
        for course in self.courses:
            if course.is_active():
                active_course.append(course.get_name())

        return active_course

    def get_part_time(self):
        part_time_list=[]
        for student in self.students:
            if student.is_part_time():
                part_time_list.append(student.get_name())

        return part_time_list

    def get_marks_list(self):
        mark_list = {}
        for student in self.students:
            mark_list[student.get_name()] = student.get_average_grade()

        return mark_list

