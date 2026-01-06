# Explain the difference between map, filter, and reduce.
"""
map() : it is a built in function that takes a function and iterable as parameters 
filter() : it calls a specific function that returns a boolean for each item of specified iterable (list)
it filters the item that satisfies the filtering criteria 
reduce() The reduce() function is defined in the functools module and we should import it from this module.
 Like map and filter it takes two parameters,
 a function and an iterable. However, it does not return another iterable, instead it returns a single value. 
"""
"""
Explain the difference between higher order function, closure and decorator
higher-order functions are a general programming concept, while closures are a specific mechanism for data retention, and decorators are a common use case and syntactic sugar built upon both concepts. 
"""


# Define a call function before map, filter or reduce, see examples.
top_l = ['lot', 'park', 'field']

def call_func(top_l):
    return top_l.upper()

names_upper_cased = map(call_func, top_l)
print(list(names_upper_cased))  



countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use for loop to print each country in the countries list.
for country in countries:
        print(country) 

# Use for to print each name in the names list.
for name in names:
    print(name) 

# Use for to print each number in the numbers list.
for num in numbers:
    print(num)

# Use map to create a new list by changing each country to uppercase in the countries list
def change_to_upper(countries):
    return countries.upper()
countries_upper = map(change_to_upper, names)
print(list(countries_upper)) 

# Use map to create a new list by changing each number to its square in the numbers list
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

# Use map to change each name to uppercase in the names list
def name_capt(names):
     return names.upper()
name_upper = map(name_capt, names)
print(list(name_upper))

# Use filter to filter out countries containing 'land'.
def countries_out(countries):
     if "land" in countries:
        return countries 
with_land = filter(countries_out, countries)
print(list(with_land))

# Use filter to filter out countries having exactly six characters.
def countries_six(countries):
     if len(countries) == 6:
        return countries 
with_lsix = filter(countries_six, countries)
print(list(with_lsix))

# Use filter to filter out countries containing six letters and more in the country list.
def countries_more_six(countries):
     if len(countries) > 6:
        return countries 
with_msix = filter(countries_more_six, countries)
print(list(with_msix))

# Use filter to filter out countries starting with an 'E'
def countries_e(country):
        return country.startswith('E')

with_e = filter(countries_e, countries)
print(list(with_e))



#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Chaining: reduce(map(filter))
result = reduce(
    lambda x, y: x + y,                   # 3. Reduce (sum them up)
    map(lambda x: x**2,                   # 2. Map (square them)
        filter(lambda x: x % 2 == 0,      # 1. Filter (even numbers only)
               numbers)
    )
)

print(f"Sum of squares of even numbers: {result}") 

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(my_list):
     return [item for item in my_list if isinstance(item, str)]

mixed_list = [1, "Apple", 3.14, "Banana", True, "Cherry"]
print(get_string_lists(mixed_list))


# Use reduce to sum all the numbers in the numbers list.
def sum_all_nums(x, y):
     return int(x) + int(y)
total = reduce(sum_all_nums, numbers)
print(total)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence_names = reduce(
    lambda x, y: x + (", and " if y == countries[-1] else ", ") + y, 
    countries
)
final_sentence = f"{sentence_names} are north European countries"
print(final_sentence)
     
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
def categorize_countries(pattern, country_list):
    # Pattern matching is case-sensitive, so we lower() both to be safe
    return [c for c in country_list if pattern.lower() in c.lower()]

print(categorize_countries('land', countries)) # ['Finland', 'Iceland']
print(categorize_countries('stan', countries)) # ['Afghanistan', 'Pakistan']

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_starting_letters(country_list):
    letter_counts = {}
    for country in country_list:
        first_letter = country[0].upper()
        if first_letter in letter_counts:
            letter_counts[first_letter] += 1
        else:
            letter_counts[first_letter] = 1
    return letter_counts
print(count_starting_letters(countries))
# Example Output: {'A': 5, 'B': 2, 'E': 4, ...}

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(country_list):
    return country_list[:10]
print(get_first_ten_countries(countries))


# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(country_list):
    return country_list[-10:]
print(get_last_ten_countries(countries))


from countries_data import countries_data
# Test 
print(f"Successfully imported {len(countries_data)} countries.")


# Sort countries by name, by capital, by population
# Sort by Name (Alphabetical)
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])

# Sort by Capital (Alphabetical)
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])

# Sort by Population (Descending - Largest to Smallest)
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

# Example output check:
print(f"First country by name: {sorted_by_name[0]['name']}")
print(f"Largest population: {sorted_by_population[0]['name']} ({sorted_by_population[0]['population']})")


# Sort out the ten most spoken languages by location.
def ten_most_spoken_languages():
    language_counts = {}
    
    # Loop through each country and each language they speak
    for country in countries_data:
        for lang in country['languages']:
            # Increment the count for each language found
            language_counts[lang] = language_counts.get(lang, 0) + 1
    
    # Sort the dictionary items by count (the value at index 1)
    # We use reverse=True to get the most spoken first
    sorted_langs = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_langs[:10]

print("Ten Most Spoken Languages:")
for lang, count in ten_most_spoken_languages():
    print(f"{lang}: {count} countries")



# Sort out the ten most populated countries.

def ten_most_populated_countries():
    # Sort the whole list by population descending
    sorted_pop = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    
    # Return only the first 10 items
    return sorted_pop[:10]

print("\nTen Most Populated Countries:")
for country in ten_most_populated_countries():
    print(f"{country['name']}: {country['population']:,}")