from sqlalchemy import Column, Integer, String
from models.base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Student(id={self.id},name='{self.name}', email='{self.email}')>"
