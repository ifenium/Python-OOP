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

# Class variables are variables that are shared amongst all variables in a class, which are the
# same for each instance unlike instance variables which are unique to each instance. 


# The class variable `raise_amount` can be accessed from the class `Employee` and both instances 'emp1` and `emp2`
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

print(Employee.num_of_emp)