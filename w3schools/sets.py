thisset = {"sibi", "rahul", "santha"}
print(thisset)

# Sets are unordered, so you cannot be sure in which order the items will appear.
# Once a set is created, you cannot change its items, but you can add new items.

thisset = {"sibi", "rahul", "santha"}

thisset.add("bantha")

print(thisset)
# Using the add method to add another item

thisset = {"sibi", "rahul", "santha"}

thisset.update(["Nadndhini", "ragul", "Sibilooo"])

print(thisset)
# Using the update method to update thisset with more items


thisset = {"sibi", "rahul", "santha"}

thisset.remove("rahul")

print(thisset)
# Removing an item


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
# Discarding an item which is the same thing as Removing an item

# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# union() method returns a new set with all items from both sets:



