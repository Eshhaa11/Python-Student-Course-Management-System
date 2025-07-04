from sqlalchemy import Column, Integer, String
from models.base import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    instructor = Column(String, nullable=False)

    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}', instructor='{self.instructor}')>"
