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

'''
@decorator_function 
def display(): 
	print('display function ran')

display()

-- The function and decorator above is the same as 
display = decorator_function(display)
decorated_display()
'''

'''
@decorator_function
def display_info(name, age):
	print('display info ran with arguments ({}, {})'.format(name, age))

display_info('Ife',21)
display()
'''

'''
Class Decorators 
class decorator_class(object):

	def __init__(self, original_function): 
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print('call method executed this before {}'.format(self. original_function.__name__))
		return self. original_function(*args, **kwargs) 
'''

from functools import wraps

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		logging.info(
			'Ran with args: {}, and kwargs: {}'.format(args,kwargs))
		return orig_func(*args, **kwargs)
	
	return wrapper

def my_timer(orig_func):
	import time 

	@wraps(orig_func)
	def wrapper (*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in: {} sec'.format(orig_func.__name__, t2))
		return result

	return wrapper


import time		

@my_timer
@my_logger
def display_info(name, age):
	time.sleep(1)
	print('display info ran with arguments ({}, {})'.format(name, age))


display_info('ife', 41)