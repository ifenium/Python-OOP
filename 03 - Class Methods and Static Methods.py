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

    # To turn a regular method to a class method, you use the decorator `@classmethod`  
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount  

    # Instead of parsing the string for each employee string, this class method take the string, 
    # parses it automatically and returns the new empl oyee object 
    @classmethod
    def  from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True 

emp1 = Employee('ife', 'oye', 50000)
emp2 = Employee('efi',  'eyo', 80000)   

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Updates the class variable `raise_amount` using the classmethod 
Employee.set_raise_amount(1.05 )

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email) 
print(new_emp_1.pay)

# REM: When working with classes regular methods automatically pass the instance as 
# the first argument which we call `self`, while class methods automatically pass the class as his
# the first argument which we call `cls`. Static Methods don't pass anything automatically (
# instance or class)

import datetime
my_date = datetime.date(2021, 6, 16)

print(Employee.is_workday(my_date))