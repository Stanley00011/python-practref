# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:

# Read obama_speech.txt file and count number of lines and words
f = open('./day_19/obama_speech.txt')
read_o = f.read() 
line = f.readline()
print(len(read_o))
print(len(line))
f.close()

# Read michelle_obama_speech.txt file and count number of lines and words
f = open('./day_19/michelle_obama_speech.txt') 
read_m = f.read()
line = f.readline()
print(len(line))
print(len(read_m))
f.close()

# Read donald_speech.txt file and count number of lines and words
f = open('./day_19/donald_speech.txt') 
read_d = f.read()
line = f.readline()
print(len(read_d))
print(len(line))
f.close()

# Read melina_trump_speech.txt file and count number of lines and words
f = open('./day_19/melina_trump_speech.txt') 
read_mt = f.read()
line = f.readline()
print(len(read_mt))
print(len(line))
f.close()


# optimised way

import os

def count_lines_and_words(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # .readlines() gives us a list where each item is one line
            lines = f.readlines()
            num_lines = len(lines)
            
            # To get words, we take the whole text and split it by whitespace
            # We can join the lines back together to get the full string
            full_text = "".join(lines)
            words = full_text.split()
            num_words = len(words)
            
            return num_lines, num_words
    except FileNotFoundError:
        return "File not found", 0

# --- Applying the function to your files ---
files = [
    'obama_speech.txt', 
    'michelle_obama_speech.txt', 
    'donald_speech.txt', 
    'melina_trump_speech.txt'
]

# Set the directory path
data_dir = './day_19/'

for file_name in files:
    path = os.path.join(data_dir, file_name)
    lines, words = count_lines_and_words(path)
    print(f"{file_name}:")
    print(f"  Lines: {lines}")
    print(f"  Words: {words}")
    print("-" * 20)


# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages


import json
from collections import Counter

def most_spoken_languages(filename, limit):
    try:
        # 1. Load the JSON data
        with open(filename, 'r', encoding='utf-8') as f:
            countries_data = json.load(f)
        
        # 2. Extract every language instance into a single list
        all_languages = []
        for country in countries_data:
            # country['languages'] is a list, so we extend our main list
            all_languages.extend(country['languages'])
        
        # 3. Count the occurrences of each language
        counts = Counter(all_languages)
        
        # 4. Format into (count, language) and sort
        # Counter.items() gives (language, count), so we flip them
        result = [(count, lang) for lang, count in counts.items()]
        
        # Sort by count (index 0) in descending order
        result.sort(key=lambda x: x[0], reverse=True)
        
        # 5. Return the top N results
        return result[:limit]

    except FileNotFoundError:
        return "File not found. Please check the path."

# --- Test Outputs ---
print(most_spoken_languages(filename='./day_19/countries_data.json', limit=10))
print(most_spoken_languages(filename='./day_19/countries_data.json', limit=3))



# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

import json

def most_populated_countries(filename, limit):
    try:
        # 1. Load the JSON data
        with open(filename, 'r', encoding='utf-8') as f:
            countries_data = json.load(f)
        
        # 2. Sort the list of dictionaries by the 'population' key
        # We use reverse=True to get the highest population first
        sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
        
        # 3. Format the output to show only country name and population
        # This creates a list of dictionaries as usually required by this exercise
        result = []
        for i in range(min(limit, len(sorted_countries))):
            country = sorted_countries[i]
            result.append({
                'country': country['name'],
                'population': country['population']
            })
            
        return result

    except FileNotFoundError:
        return "File not found. Please check the path."
    except KeyError:
        return "The JSON structure is missing 'name' or 'population' keys."

# --- Test Outputs ---
print(most_populated_countries(filename='./day_19/countries_data.json', limit=10))
print(most_populated_countries(filename='./day_19/countries_data.json', limit=3))