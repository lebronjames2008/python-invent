# A variable is only available from inside the region it is created. This is called scope.
def myfunc():
  x = 300
  print(x)

myfunc()
# A variable created inside a function is available inside that function

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
# Printing 2 300's

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
# The function will print the local x, and then the code will print the global x:

def myfunc():
  global x
  x = 300

myfunc()

print(x)
# Another way to print with global
# Also, use the global keyword if you want to make a change to a global variable inside a function.

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
