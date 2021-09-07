'''
# What is a Decorator?

A function that take a function as an argument adds some 
functionality and then returns another function, without altering 
the origina function passed in as the argument.

{Intro} 

def outer_function(msg):
	def inner_function():
		print(msg)
	return inner_function

hi_func = outer_function('hi')
bye_func = outer_function('bye')

hi_func()
bye_func( )
'''
 
def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*args, **kwargs) 
	return wrapper_function

@decorator_function
def display():
	print('display function ran')


'''
@decorator_function 
def display():
	print('display function ran')

display()

-- The function and decorator above is the same as 
display = decorator_function(display)
decorated_display()
'''

@decorator_function
def display_info(name, age):
	print('display info ran with arguments ({}, {})'.format(name, age))

display_info('Ife',21)
display()

'''
Class Decorators 
class decorator_class(object):

	def __init__(self, original_function): 
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print('call method executed this before {}'.format(self. original_function.__name__))
		return self. original_function(*args, **kwargs) 
'''

