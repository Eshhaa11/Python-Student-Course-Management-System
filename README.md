# Student Course Management System

This is a Capstone Project built with Python and SQLAlchemy. It simulates a basic student-course management system using OOP, a linked list for course history, and a SQLite database for storage.

## 💡 Features

- Object-Oriented design for `Student` and `Course`
- Linked List to track student course history
- SQLAlchemy ORM to store and retrieve data
- Unit tests using `unittest`

## 🏗️ Folder Structure

models/ # Contains Student, Course, and Base model
linkedlist/ # Linked list class for course history
tests/ # Unit tests
main.py # Entry point to test logic

## ⚙️ How to Run

1. **Install dependencies** (in a virtual env is recommended):

   ```bash
   pip install -r requirements.txt

   ```

2. **Run the app:**

   python main.py

3. **Run the tests:**

   python -m unittest tests/test_enrollment.py

## 📁 Database

A local SQLite database (student_course.db) is created automatically.

## 👤 Author

Esha Patel
