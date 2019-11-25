class Employee:
    raise_amt = 1.15

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

    def get_email(self):
        return '{},{}@gmail.com'.format(self.firstname, self.lastname)

    def get_fullname(self):
        return '{},{}'.format(self.firstname, self.lastname)

    def get_pay(self):
        return int(self.pay * self.raise_amt)

    