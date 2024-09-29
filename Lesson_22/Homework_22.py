from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

student_course = Table('student_course', Base.metadata,
                       Column('student_id', ForeignKey('students.id'), primary_key=True),
                       Column('course_id', ForeignKey('courses.id'), primary_key=True))


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship('Course', secondary=student_course, back_populates='students')

    def __repr__(self):
        return f"<Student(name={self.name})>"


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship('Student', secondary=student_course, back_populates='courses')

    def __repr__(self):
        return f"<Course(name={self.name})>"


engine = create_engine('sqlite:///students.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create Student and Courses

course_1 = Course(name="Music")
course_2 = Course(name="Art")
course_3 = Course(name="Management")
course_4 = Course(name="Sport")
course_5 = Course(name="Computer Science")

session.add_all([course_1, course_2, course_3, course_4, course_5])
session.commit()

students = [Student(name=f"Student {i}") for i in range(1, 21)]

session.add_all(students)
session.commit()

import random

for student in students:
    random_courses = random.sample([course_1, course_2, course_3, course_4, course_5], k=2)
    student.courses.extend(random_courses)

session.commit()

print("Students from these courses have been successfully added to the database.")


# Added new student and registration for the course

def add_student_to_course(student_name, course_name):
    student = Student(name=student_name)
    course = session.query(Course).filter_by(name=course_name).first()

    if not course:
        print(f"Course with name {course_name} not found.")
        return

    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"Student {student_name} added to course {course_name}.")


add_student_to_course("New Student", "Music")


# Database queries :

# Get students

def get_students_for_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()

    if course:
        return [student.name for student in course.students]
    return []


students_in_music = get_students_for_course("Music")
print(f"Students, registered on course Music: {students_in_music}")


# Get Course

def get_courses_for_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()

    if student:
        return [course.name for course in student.courses]
    return []


courses_for_student_1 = get_courses_for_student("Student 1")
print(f"Courses for Student 1: {courses_for_student_1}")


# Update info

def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()

    if student:
        student.name = new_name
        session.commit()
        print(f"Student name change for {new_name}.")
    else:
        print(f"Student with name {old_name} not found.")


update_student_name("Student 1", "Updated Student 1")


# Delete student

def delete_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()

    if student:
        session.delete(student)
        session.commit()
        print(f"Student {student_name} successfully deleted.")
    else:
        print(f"Student with name {student_name} not found.")


delete_student("Updated Student 1")
