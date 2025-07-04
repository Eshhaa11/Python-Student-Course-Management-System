import unittest
from models.student import Student
from models.course import Course
from linkedlist.history import CourseHistory

class TestStudentCourseSystem(unittest.TestCase):

    def test_student_creation(self):
        student = Student(name="Esha Patel", email="john@example.com")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.email, "john@example.com")

    def test_course_creation(self):
        course = Course(title="Math 101", instructor="Prof. X")
        self.assertEqual(course.title, "Math 101")
        self.assertEqual(course.instructor, "Prof. X")

    def test_course_history(self):
        history = CourseHistory()
        history.add_course("Math 101")
        history.add_course("English 102")
        self.assertEqual(history.get_history(), ["Math 101", "English 102"])

if __name__ == '__main__':
    unittest.main()
