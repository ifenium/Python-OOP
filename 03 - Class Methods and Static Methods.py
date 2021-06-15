class Employee:
    
    num_of_emp = 0 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
 
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp1 = Employee('ife', 'oye', 50000)
emp2 = Employee('efi', 'eyo', 80000)  
