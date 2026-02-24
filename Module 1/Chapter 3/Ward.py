class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student- Name: {self.name}- YoB: {self.yob}- Grade: {self.grade}")

class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Teacher- Name: {self.name}- YoB: {self.yob}- Subject: {self.subject}")

class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"Doctor- Name: {self.name}- YoB: {self.yob}- Specialist: {self.specialist}")

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []
    
    def addPerson(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.people:
            person.describe()

    def countDoctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count
    
    def sortAge(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)
    
    def aveTeacherYearOfBirth(self):
        total = 0
        count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                total += person.yob
                count += 1
        if count == 0:
            return 0
        return total/count

student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
