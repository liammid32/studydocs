class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        Student.count += 1
        gpa = sum(grades) / len(grades)
        Student.total_gpa += gpa
        self.gpa = gpa

    def get_info(self):
        return f"{self.name}'s GPA is {self.gpa:.2f}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

        
Student1 = Student("Clarke", [90, 80, 85])
Student2 = Student("Martha", [70, 75, 80])
Student3 = Student("John", [60, 65, 70])

print(Student.get_count())
print(Student1.get_info())
print(Student2.get_info())
print(Student3.get_info())