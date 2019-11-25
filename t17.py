class Employee:
    "common base classes for all"
    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def display_employee(self):
        print("name :", self.name, ", salary :", self.salary)

    def employee_count(self):
        print("no. of employees is : {}".format(Employee.empcount))


emp1 = Employee("abc", 56000)
emp2 = Employee("xyz", 63000)
emp3 = Employee("klm", 45000)
emp1.display_employee()
emp2.display_employee()
print(Employee.empcount)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__bases__)
print(Employee.__dict__)



