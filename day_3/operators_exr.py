#Declare your age as integer variable
age = 25

# Declare your height as a float variable
height = 5.10

# Declare a variable that store a complex number
complex_num = 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter base of the triangle: '))
height = float(input('Enter height of the triangle: '))
area_of_triangle = 0.5 * base * height
print('Area of the triangle:', area_of_triangle)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input('Enter side a of the triangle: '))
side_b = float(input('Enter side b of the triangle: '))
side_C = float(input('Enter side c of the triangle: '))
perimeter_of_triangle = side_a + side_b + side_C
print('Perimeter of the triangle:', perimeter_of_triangle)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenght = float(input('Enter length of the rectangle: '))
width = float(input('Enter width of the rectangle: '))
area_of_rectangle = lenght * width
perimeter_of_rectangle = 2 * (lenght + width)
print('Area of the rectangle:', area_of_rectangle)
print('Perimeter of the rectangle:', perimeter_of_rectangle)

# Get radius of a circle using prompt. Calculate its area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float (input('Enter radius of the circle: '))
pi = 3.14
area_of_Circle = pi * radius ** 2
circumfrence_of_circle = 2 * pi * radius 
print('Area of the circle:', area_of_Circle)
print('Circumference of the circle:', circumfrence_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope  = 2 
x_intercept  = 1
y_intercept  = -2
print('slope:', slope)
print('x-intercept:', x_intercept)
print('y-intercept:', y_intercept)  

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10  
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print('slope:', slope)
print('Euclidean distance:', euclidean_distance)

# Compare the slopes in tasks 8 and 9.
slope_task_8 = 2
slope_task_9 = (10 - 2) / (6 - 2)
print('Are the slopes equal?', slope_task_8 == slope_task_9)
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + 6*x + 9
print('Value of y when x is', x, 'is:', y)    

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len('dragon')
print('Is the length of python equal to the length of dragon?', len_python == len_dragon)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('Is "on" found in both "python" and "dragon"?', 'on' in 'python' and 'on' in 'dragon')

py_t = 'python'
dr_g = 'dragon'
print('on' in py_t and 'on' in dr_g)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('Is "jargon" found in the sentence?', 'jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
print('Is "on" not found in both "dragon" and "python"?', 'on' not in 'dragon' and 'on' not in 'python')

# Find the length of the text python and convert the value to float and convert it to string
len_python = len('python')
len_python_float = float(len_python)
len_python_str = str(len_python_float)
print('Length of python as float:', len_python_float)
print('Length of python as string:', len_python_str)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

# Check if type of '10' is equal to type of 10

# Check if int('9.8') is equal to 10

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Enter hours worked: '))
rate_per_hour = float(input('Enter rate per hour: '))
pay = hours * rate_per_hour
print('Pay of the person:', pay)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter number of years you have lived: '))
seconds_in_a_year = 365 * 24 * 60 * 60      
total_seconds_lived = years * seconds_in_a_year
print('You have lived for', total_seconds_lived, 'seconds.')

# Write a Python script that displays the following table
print('1\t1\t1\t1\t1')
print('2\t1\t2\t4\t8')
print('3\t1\t3\t9\t27')
print('4\t1\t4\t16\t64')
print('5\t1\t5\t25\t125')