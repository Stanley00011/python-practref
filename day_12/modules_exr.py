# Writ a function which generates a six digit/character random_user_id.
from random import randint, choice, random
import string   
def random_user_id():
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(6))
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random
import string

def user_id_gen_by_user():
    # 1. Take inputs inside the function
    # Using a single input line or two separate ones
    char_count = int(input("Enter number of characters: "))
    id_count = int(input("Enter number of IDs: "))
    
    all_chars = string.ascii_letters + string.digits
    generated_ids = []

    # 2. Generate the IDs
    for _ in range(id_count):
        # Create one ID of the specified length
        new_id = ''.join(random.choice(all_chars) for _ in range(char_count))
        generated_ids.append(new_id)

    # 3. Return all IDs joined by a newline character
    return '\n'.join(generated_ids)

# 4. Call the function as shown in your prompt
print(user_id_gen_by_user())


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
print(rgb_color_gen())

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    hex_chars = "0123456789abcdef"
    colors_list = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors_list.append(color)
    return colors_list
print(list_of_hexa_colors(3)) 
print(list_of_hexa_colors(1))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    return [rgb_color_gen()
             for _ in range(num_colors)]
print(list_of_rgb_colors(3))

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(num_colors, color_type="hex"):
    if color_type == "hex":
        return list_of_hexa_colors(num_colors)
    elif color_type == "rgb":
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type. Use 'hex' or 'rgb'."
    # --- Test Outputs ---
print(generate_colors(3, 'hexa')) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors(1, 'hexa')) # ['#b334ef']
print(generate_colors(3, 'rgb'))  # ['rgb(5, 55, 175)','rgb(50, 105, 100)','rgb(15, 26, 80'] 
print(generate_colors(1, 'rgb'))  # ['rgb(33,79, 176)']

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list
print(shuffle_list([1, 2, 3, 4, 5, 6, 7]))

def seven_random_numbers():
    return [random.randint(0, 9) for _ in range(7)]
print(seven_random_numbers())