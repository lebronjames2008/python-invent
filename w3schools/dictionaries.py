# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

sibidic =	{
  "sibi": "Awesome",
  "rahul": "Sibi's brother",
  "Nandhini":"Best Mom",
}
print(sibidic)
# Creating and Printing a Dictionary

sibidic =	{
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}
x = sibidic["sibi"]
print(x)
# You can access the items of a dictionary by referring to its key name, inside square brackets
# There is also a method called get() that will give you the same result

sibidic =	{
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}

sibidic["rahul"] = 'Bad Brother'

print(sibidic)
# You can change the value of a specific item by referring to its key name

sibidic =	{
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}
for x in sibidic:
  print(x)
# Print all key names in the dictionary, one by one

sibidic =	{
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}
for x in sibidic:
  print(sibidic[x])
# You can also use the values() method to return values of a dictionary

sibidic =	{
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}
for x, y in sibidic.items():
  print(x, y)
# Loop through both keys and values, by using the items() method

sibidic = {
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}
if "Nandhini" in sibidic:
  print("Yes, 'Nandhini' is one of the keys in the thisdict dictionary")
# Check if "Nandhini" is present in the dictionary

sibidic =	{
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}

print(len(sibidic))
# Print the number of items in the dictionary:

sibidic =	{
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}
sibidic["Pizza"] = "Unhealthy"
print(sibidic)
# Adding an item to the Dictionary

sibidic = {
    "sibi": "Awesome",
    "rahul": "Sibi's brother",
    "Nandhini": "Best Mom",
}
mydict = dict(sibidic)
print(mydict)
# Make a copy of a dictionary with the dict() function


sibifamily = {
  "child1" : {
    "name" : "Sibi",
    "year" : 2008
  },
  "child2" : {
    "name" : "Rahul",
    "year" : 2006
  }
},
print(sibifamily)
# Create a dictionary that contain 2 dictionaries

child1 = {
  "name" : "Sibi",
  "year" : 2008
}
child2 = {
  "name" : "Rahul",
  "year" : 2006
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
}

print(myfamily)
# Creating 2 dictionaries, then creating one dictionary that will contain the other 2 dictionaries

sibidic = dict(Sibi="Awesome", Rahul="Sibi's Brother", Nandhini="Best Mom")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(sibidic)





















