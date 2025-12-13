#Declare an empty list
empty_list = []

#Declare a list with more than 5 items
more_than_five = ['well', 'it', 'was', 'great', 'cool']

#Find the length of your list
print(len(more_than_five))

# Get the first item, the middle item and the last item of the list
more_than_fivel = more_than_five[0::2]
print(more_than_fivel)


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['jay', 24, 5.9, 'single', 'las']
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
print(f'this are it_companies {it_companies}')

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print(it_companies[0::3])

#Print the list after modifying one of the companies
it_companies.remove('Oracle')
print(f'this are it_companies {it_companies}')

#Add an IT company to it_companies
it_companies.append('Netflix')
print(f'this are it_companies {it_companies}')

#Insert an IT company in the middle of the companies list
it_companies.insert(3, 'AWS')
print(f'this are it_companies {it_companies}')

# # Change one of the it_companies names to uppercase (IBM excluded!)
# it_companies.upper()
# print(f'this are it_companies {it_companies}')

#Join the it_companies with a string '#;  '
join_it_companies = '# '.join(it_companies)
print(join_it_companies)

# Check if a certain company exists in the it_companies list.
exist_it_companies = 'AWS' in it_companies
print(exist_it_companies)

#Sort the list using sort() method
it_companies.sort()
print(f'this are it_companies {it_companies}')

#Reverse the list in descending order using reverse() method
reverse_it_companies = it_companies[::-1]
print(reverse_it_companies)

#Slice out the first 3 companies from the list
slice_it_companies = it_companies[0:3]
print(slice_it_companies)

#Slice out the last 3 companies from the list
slicel_it_companies = it_companies[5:]
print(slicel_it_companies)


it_companies.append('Oracle')
print(it_companies)

#Slice out the middle IT company or companies from the list
slicem_it_companies = it_companies[4]
print(slicem_it_companies)

#Remove the first IT company from the list
removef_it_companies = it_companies.pop(0)
print(removef_it_companies)
print(it_companies)

# Remove the last IT company from the list
removel_it_companies = it_companies.pop(-1)
print(removel_it_companies)
print(it_companies)

# Remove all IT companies from the list
removeall_it_companies = it_companies.clear()
print(removeall_it_companies)
print(it_companies)

# Destroy the IT companies list
del it_companies

#Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(5,'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

students_ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

# Add the min age and the max age again to the list

# Find the median age (one middle item or two middle items divided by two)

# Find the average age (sum of all items divided by their number )

# Find the range of the ages (max minus min)

# Compare the value of (min - average) and (max - average), use abs() method

