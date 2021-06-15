# Methods are functions associated with a class 
# Classes are blueprints for creating instances, hence each unique employee we create using 
# the employee class would be an instance of that class.  

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    # Each method within a class  automatically takes 
    # the instance as the first argument which is always called self 
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


# Each of these will be their own unique instances of the employee class
emp1 = Employee('ife', 'oye', 50000)
emp2 = Employee('efi', 'eyo', 80000) 

# print(emp1)
# print(emp2)

# The paranthesis are needed below because this is a method(function defined in a class) 
# and not an attribute(instance variable defined in a class)
print(emp2.fullname())   

# The two lines of code below do the same thing but,

# this calls the method `fullname()` on the instance `emp2`, passing `self` isn't needed 
emp2.fullname() 

# this calls the method `fullname()` on the class `Employee` while passing the instance `emp1`
Employee.fullname(emp1)