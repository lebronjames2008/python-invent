print('How many names do you want in your list')
total_names_string = input()    #4

# converting string to int
total_names = int(total_names_string)

# creating an empty
names_list = []

#
for x in range (total_names):
    print('Enter a name')
    user_name = input()
    names_list.append(user_name)

# print(names_list)


for y in range (total_names):
    print(names_list[y].upper()+' Farted')
