class Parent():
    def mymethod(self):
        print("calling from parent")


class Child(Parent):
    def my_method(self):
        print("calling from child")


c = Child()
c.my_method()
c.mymethod()


