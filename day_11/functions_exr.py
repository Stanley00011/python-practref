#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers (num_one, num_two):
    sum = num_one + num_two 
    return sum
print('sum of two numbers:', add_two_numbers(3, 5))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area 
print('Area of a circle:', area_of_circle(10))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums (*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "All arguments must be numbers."
    return total
print('Sum of all numbers:', add_all_nums(1, 2, 3, 4.5))
print(add_all_nums(1, 'two', 3))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_farenheit (celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
print('25°C in Farenheit is:', convert_celsius_to_farenheit(25))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season (month):
    month = month.lower()
    if month in ('september', 'october', 'november'):
        return "The season is Autumn."
    elif month in ('december', 'january', 'february'):
        return "The season is Winter."
    elif month in ('march', 'april', 'may'):
        return "The season is Spring."
    elif month in ('june', 'july', 'august'):
        return "The season is Summer."
    else:
        return "Invalid month."
enter_month = input("Enter month: ")
print(check_season(enter_month))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn
def solve_quadratic_eqn(a, b, c):
    D = b**2 - 4*a*c  # Discriminant
    if D > 0:
        root1 = (-b + D**0.5) / (2*a)
        root2 = (-b - D**0.5) / (2*a)
        return (root1, root2)
    elif D == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return "No real roots."
print('Roots of the equation 1x² + -3x + 2 = 0 are:', solve_quadratic_eqn(1, -3, 2))
print('Roots of the equation 1x² + 2x + 1 = 0 are:', solve_quadratic_eqn(1, 2, 1))
print('Roots of the equation 1x² + 0x + 1 = 0 are:', solve_quadratic_eqn(1, 0, 1))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list (items): 
    for item in items:
        print(item)
fruits = ['Apple', 'Banana', 'Cherry']
print_list(fruits)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list (arr):
    reversed_arr = []
    for iten in arr:
        reversed_arr = [iten] + reversed_arr
    return reversed_arr
numbers = [1, 2, 3, 4, 5]
print('Reversed list:', reverse_list(numbers))
print(reverse_list(["A", "B", "C"]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns the capitalized list of items.
def capitalize_list_items (items):
    capitalized_items = []
    for item in items:
        capitalized_items.append(item.capitalize())
    return capitalized_items
fruits = ['apple', 'banana', 'cherry']
print('Capitalized list items:', capitalize_list_items(fruits))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item (items, item):
    items.append(item)
    return items    
fruits = ['Apple', 'Banana']
print('List after adding item:', add_item(fruits, 'Cherry'))

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print('List after adding item:', add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print('List after adding item:', add_item(numbers, 5))      # [2, 3, 7, 9, 5]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total = 0
    for i in range(num+1):
        total+=i
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    total = 0
    for i in range(num+1):
        if i % 2 !=0:
            total+=i
    return total
print(sum_of_odds(5))  # 9
print(sum_of_odds(10)) # 25

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even (num):
    total = 0
    for i in range(num+1):
        if i % 2 == 0:
            total+=i
    return total
print(sum_of_even(5))  # 6
print(sum_of_even(10)) # 30

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds (num): 
    even_count = 0
    odd_count = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
print(evens_and_odds(100)) # (50, 50)
print(evens_and_odds(7))   # (3, 4)

def factorial (n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print('Factorial of 5 is:', factorial(5))  # 120
print('Factorial of 0 is:', factorial(0))  # 1
print('Factorial of -3 is:', factorial(-3))  # Factorial is not

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty (param):
    if not param:
        return True
    else:
        return False
print(is_empty([]))          # True
print(is_empty([1, 2, 3]))  # False

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean (numbers):
    return sum(numbers) / len(numbers)
print('Mean:', calculate_mean([1, 2, 3, 4, 5]))  # 3.0

def calculate_median (numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    return median
print('Median:', calculate_median([3, 1, 4, 2, 5]))  # 3

def calculate_mode (numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    mode = max(frequency, key=frequency.get)
    return mode
print('Mode:', calculate_mode([1, 2, 2, 3, 4]))  # 2

def calculate_range (numbers):
    return max(numbers) - min(numbers)
print('Range:', calculate_range([1, 2, 3, 4, 5]))  # 4

def calculate_variance (numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance
print('Variance:', calculate_variance([1, 2, 3, 4, 5]))  # 2.0

def calculate_std (numbers):
    variance = calculate_variance(numbers)
    std_dev = variance ** 0.5
    return std_dev
print('Standard Deviation:', calculate_std([1, 2, 3, 4, 5]))  # 1.4142135623730951

# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False 
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # True
# Write a functions which checks if all items are unique in the list.
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_all_items_unique([1, 2, 3, 4, 5]))  # True
print(are_all_items_unique([1, 2, 2, 4, 5]))  # False
# Write a function which checks if all the items of the list are of the same data type.
def are_all_items_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True
print(are_all_items_same_type([1, 2, 3]))  # True
print(are_all_items_same_type([1, 2, '3']))  # False

# Write a function which check if provided variable is a valid python variable
def is_valid_variable(var_name):
    if not var_name.isidentifier():
        return False
    reserved_keywords = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
        'yield'
    ]
    return var_name not in reserved_keywords
print(is_valid_variable('my_var'))  # True
print(is_valid_variable('2nd_var'))  # False

# Go to the data folder and access the countries-data.py file.
from countries_data import countries_data
# Test 
print(f"Successfully imported {len(countries_data)} countries.")

# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages (n):
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]
print('10 most spoken languages:', most_spoken_languages(10))

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(n):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:n]
print('10 most populated countries:', most_populated_countries(10))

