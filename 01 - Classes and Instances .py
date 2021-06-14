# Methods are functions associated with a class 
# Classes are blueprints for creating instances, hence each unique employee we create using 
# the employee class would be an instance of that class.  

class Employee:
    pass

# Each of these will be their own unique instances of the employee class
emp1 = Employee()
emp2 = Employee() 

print(emp1)
print(emp2)

# Instance variables contains data that is unique to each instance 
emp1.first = 'ife'
emp1.last = 'oye'
emp1.email = 'oyeife@gmail.com'
emp1.pay = '$50,000'

emp2.first = 'efi'
emp2.last = 'eyo'
emp2.email = 'efieyo@gmail.com'
emp2.pay = '$80,000'

print(emp1.email)
print(emp2.email)