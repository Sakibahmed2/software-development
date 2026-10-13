class Student:
    def __init__(self, name, cls, id):
        self.name = name
        self.cls = cls
        self.id = id

    def __repr__(self) -> str:
        return f"Student with name {self.name}, class {self.cls}, id: {self.id}"

class Teacher:
    def __init__(self, name, id, subject):
        self.name = name
        self.id = id
        self.subject = subject

    def __repr__(self) -> str:
        return f"Teacher: {self.name}, id: {self.id}, subject: {self.subject}"

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teacher = []
        self.students = []

    def add_teacher(self, teacher, subject):
        id = len(self.teacher) + 101
        teacher = Teacher(teacher, subject, id)
        self.teacher.append(teacher)

    def enroll(self, name, fee):
        if fee < 5000:
            return 'not enough money'
        else:
            id = len(self.students) + 1
            student = Student(name, 12, id)
            self.students.append(student)
            return f"{name} is enrolled with id: {id}"

    def __repr__(self):
        print(f"Welcome to {self.name}")
        print("----------OUR TEACHERS-------------")
        for t in self.teacher:
            print(t)
        print("----------OUR STUDENTS-------------")
        for s in self.students:
            print(s)
        return "All done for now"

        


phitron = School("Phitron")

phitron.enroll("Sakib", 5000)
phitron.enroll("Rahim", 5000)
phitron.enroll("Karim", 5000)

phitron.add_teacher("Tom", 'Physics')
phitron.add_teacher("Srk", 'ALgo')
phitron.add_teacher("Zoro", 'DS')

print(phitron)
