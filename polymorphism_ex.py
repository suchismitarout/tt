class Student:
    def get_name(self):
        self.__name = "xyz"
        print(self.__name)

    def get_age(self):
        self.__age = 17
        print(self.__age)

class Teacher:
    def get_name(self):
        self.__name = "abc"
        print(self.__name)

    def get_age(self):
        self.__age = 46
        print(self.__age)
def get_name(faculty):
    faculty.get_name()

s = Student()
t = Teacher()
get_name(s)
get_name(t)

