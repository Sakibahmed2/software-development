import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1, 100)


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    def final_grade(self):
        total = 0

        for grade in self.subject_grade.values():
            total += School.grade_to_value(grade)

        if len(self.subject_grade) == 0:
            self.grade = "F"
            return self.grade

        gpa = total / len(self.subject_grade)
        self.grade = School.value_to_grade(gpa)

        return self.grade

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value
    
        