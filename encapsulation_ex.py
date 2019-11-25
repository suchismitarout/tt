class Student:
    def __init__(self):
        self.__name = "vijay"

    def get_name(self):
        print("student's name is {}".format(self.__name))

    def set_name(self, name):
        self.__name = name



c = Student()
c.get_name()
c.set_name("priya")
c.get_name()
c.__name = "ramesh"
c.get_name()