# Methods are functions associated with a class 
# Classes are blueprints for creating instances, hence each unique employee we create using 
# the employee class would be an instance of that class.  

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


# Each of these will be their own unique instances of the employee class
emp1 = Employee('ife', 'oye', '$50,000')
emp2 = Employee('efi', 'eyo', '$80,000') 

# print(emp1)
# print(emp2)

print(emp1.fullname()) 