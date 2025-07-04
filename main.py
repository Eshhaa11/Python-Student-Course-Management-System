from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.students import Student
from models.course import Course


engine = create_engine('sqlite:///student_course.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

# 3. Create some test data
student1 = Student(name="Esha", email="eshaptl1212@gmail.com")
student2 = Student(name="Kripa", email="kripa345@gmail.com")

course1 = Course(title="Python Basics", instructor="Dr. Smith")
course2 = Course(title="Data Structures", instructor="Prof. Lee")


session.add_all([student1, student2, course1, course2])
session.commit()


print("Students:")
for student in session.query(Student).all():
    print(student)

print("\nCourses:")
for course in session.query(Course).all():
    print(course)

from linkedlist.history import CourseHistory

# Create course history for Alice
alice_history = CourseHistory()


alice_history.add_course("Python Basics")
alice_history.add_course("Data Structures")
alice_history.add_course("Databases")


print("\nEsha's Course History:")
for course in alice_history.get_history():
    print(course)

