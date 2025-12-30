# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input ("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else: 
    years_remaining = 18 - age
    print(f"You need to wait {years_remaining} more years to drive.")



#Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 25
your_age = int(input("Enter your age: "))

if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
elif your_age > my_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
else:
    print("We are the same age.")

# Get two numbers from the user using input prompt. If a is greater than b return a 
# is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter first number (a): "))
b = int(input ("Enter second number (b): "))
if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")

# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("You got an A.")
elif 70 <= score <= 79:
    print("You got a B.")
elif 60 <= score <= 69:
    print("You got a C.")
elif 50 <= score <= 59:
    print("You got a D.")
elif 0 <= score <= 49:
    print("You got an F.")
else:
    print("Invalid score.")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring
# June, July or August, the season is Summer
month = input("Enter month: ")
month = month.lower()
if month in ('september', 'october', 'november'):
    print("The season is Autumn.")
elif month in ('december', 'january', 'february'):
    print("The season is Winter.")
elif month in ('march', 'april', 'may'):
    print("The season is Spring.")
elif month in ('june', 'july', 'august'):
    print("The season is Summer.")
else:
    print("Invalid month.")

# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list.')
fruit = input("Enter a fruit name: ")
fruit = fruit.lower()
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print(fruits)

# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Jay',
    'last_name': 'Doe',
    'age': 25,
    'country': 'Finland',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"The middle skill is: {skills[middle_index]}")

    if 'Python' in skills:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

    if set(['JavaScript', 'React']).issubset(skills):
        print("He is a front end developer.")
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print("He is a backend developer.")
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")
if person.get('is_married') and person.get('country') == 'Finland':
    first_name = person.get('first_name', '')
    last_name = person.get('last_name', '')
    print(f"{first_name} {last_name} lives in Finland. He is married.")
else :
    print("The person is either not married or does not live in Finland.")