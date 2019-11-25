class Student:
    def __init__(self, name, age, loc, salary):
        self.name = name
        self.age = age
        self.loc = loc
        self.salary = salary
    def display_show(self):
        print(self.name)
        print(self.age)
        print(self.loc)
        print(self.salary)

st = Student("xyz", 28, "blr", 34000)
print(vars(st))
print(dir(st))