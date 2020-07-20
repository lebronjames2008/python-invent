names_list = ['sibi', 'rahul', 'santha', 'scott', 'james']

# print all the elements in the list
print(names_list)

# print the 4th index of the list
print(names_list[4])

print(names_list[-5])

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# find the size of the list
print(len(names_list))

# append is adding a new element to the end of the list
names_list.append('rishi')
print(names_list)

names_list.insert(3, 'jeremy')
print(names_list)

# The pop() method removes the specified index, (or the last item if index is not specified):
names_list.pop()
print(names_list)
