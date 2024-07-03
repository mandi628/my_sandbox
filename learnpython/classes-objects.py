# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.
class MyClass:
	variable = "blah"

	def function(self):
		print("This is a message inside the class.")

myobjectx = MyClass()
# To access the variable inside of the newly created object "myobjectx"
print(myobjectx.variable)
# output = 'blah'

#You can create multiple different object that are of the same class (have the same variables
# and functions defined). However, each object contains independent copies of the variables
# defined in the class. For instance, if we were to define another object with the "MyClass"
# class and then change the string in the variable...
class MyClass:
	variable = "blah"

	def function(self):
		print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)
