from sqlalchemy import Column, Integer, String
from models.base import Base

class Student(Base):
    __tablename__ = 'students'