#1
class MyClass:
    x = 5
print(MyClass)

#2
p1 = MyClass()
print(p1.x)

# The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Person:
  def __init__(sibiawesome, name, age):
    sibiawesome.name = name
    sibiawesome.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# You can modify properties on objects like this:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)



