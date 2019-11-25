class Employee:
    def __init__(self, name, age, emp_id, address):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.address = address

    def __repr__(self):
        return '"name":{}, "age":{}, "emp_id":{}, "address":{}'.format(self.name, self.age, self.emp_id, self.address)


emp1 = Employee("abc", 27, 2134, "blr")
emp2 = Employee("xyz", 26, 2341, "dlh")
emp3 = Employee("klm", 28, 2786, "rkl")

emp_list = [emp1, emp2, emp3]
emp_dict = {}
for i in emp_list:
    emp_dict[i] = i.

# print(emp_list)
