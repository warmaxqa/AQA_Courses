class Student:

    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_score

    def update_average_score(self, new_grade):
        self.average_grade = new_grade

    def display_student_info(self):
        print(f"Student: {self.name} {self.surname}")
        print(f"Years: {self.age}")
        print(f"Average score: {self.average_grade}")

student1 = Student("Max", "Kudriavskyy", 31, 95.3)

student1.display_student_info()

student1.update_average_score(13.5)

print("After update average score:")

student1.display_student_info()
