from address import Address
from course import Course
from enroll import Enroll
from professor import Professor
from school import School
from student import Student

# ADDRESS
address1 = Address("India", "UP", "Allahabad", "no. 234", "234344")
address2 = Address("India", "UP", "Allahabad", "no. 234", "234344")
address3 = Address("India", "UP", "Allahabad", "no. 234", "234344")
address4 = Address("India", "UP", "Allahabad", "no. 234", "234344")

# STUDENT
ram = Student("ram", "singh", "26-Nov-1996", address1)
shyam = Student("shyam", "singh", "26-Nov-1996", address2)
mohan = Student("mohan", "singh", "26-Nov-1996", address3)

# PROF
prof1 = Professor("ram", "singh", "26-Nov-1996", address2, 100000)
prof2 = Professor("shyam", "singh", "26-Nov-1996", address3, 200000)

# COURSE
course1 = Course("PHY", "122", 1, 8, [prof1, prof2])
course2 = Course("CHEM", "1324", 3, 5, [prof1])

school = School()
school.add_prof(prof2)
school.add_prof(prof1)
school.add_course(course2)
school.add_course(course1)
school.add_student(ram)
school.add_student(shyam)
school.add_student(mohan)

# ENROLL
enroll1 = Enroll(ram, course1)
enroll2 = Enroll(ram, course2)
enroll3 = Enroll(shyam, course2)

# prof marks grades
enroll1.set_grade(89)
enroll2.set_grade(35)
enroll3.set_grade(75)

print("Get All Course - " + str(school.get_all_courses()))
print("Who Teaches which course" + str(school.course_teaches()))
print("Get active course - " + str(school.get_active_course()))
print("Prof1 salary- "+str(prof1.get_salary()))
print("Prof2 salary- "+str(prof2.get_salary()))
print("Get Part Time students" + str(school.get_part_time()))
print("Get percentage of students "+str(school.get_marks_list()))

