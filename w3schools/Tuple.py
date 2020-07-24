# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("sibi", "rahul", "santha")
print(thistuple)

thistuple = ("sibi", "rahul", "santha")
print(thistuple[1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable.

x = ("sibi", "rahul", "santha")
y = list(x)
y[1] = "bantha"
x = tuple(y)

print(x)

thistuple = ("sibi", "rahul", "santha")
if "sibi" in thistuple:
  print("Yes, 'sibi' is in the family tuple")

# count() Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# Tuples are lists but they can't be changed, and tuples have parentheses





