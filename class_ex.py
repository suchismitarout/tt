class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Teacher(Student):
    def __init__(self, loc):
        super().__init__("sima", 27)
        self.loc = loc

    def get_loc(self):
        return self.loc

teacher_obj = Teacher("blr")
print(teacher_obj.get_loc())
print(teacher_obj.get_name())
print(teacher_obj.get_age())

