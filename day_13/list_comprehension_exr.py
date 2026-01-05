
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)  # [-4, -3, -2, -1, 0]

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list =  [num for row in list_of_lists for sublist in row for num in sublist]
print(flattened_list) 

# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
tuples_list = [(i, i**2, i**3, i**4, i**5, i**6, i**7) for i in range(11)]
print(tuples_list)  

# Flatten the following list to a new list: 
# output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_list = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(flat_list)  

#Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country.upper(), 'city': capital.upper()} for sublist in countries for country, capital in sublist]
print(countries_dict)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_strings = [' '.join(name).upper() for sublist in names for name in sublist]
print(concatenated_strings)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'undefined'
print(slope(2, 3, 4, 7))  # Output: 2.0
print(slope(1, 2, 1, 5))  # Output: 'undefined'