# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'


import requests
import re
from collections import Counter

def find_most_common_words(input_data, n):
    # If input_data is a URL or file path, it would be a string.
    # But here, we pass the raw text string directly.
    
    # 1. Clean the text: remove non-alphabetic characters and lowercase
    # This regex finds all sequences of letters
    words = re.findall(r'\b[a-z]+\b', input_data.lower())
    
    # 2. Count the words
    counts = Counter(words)
    
    # 3. Format as [(count, word)] in descending order
    return [(count, word) for word, count in counts.most_common(n)]

# --- Fetching the Data ---
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)

if response.status_code == 200:
    # Use .text for plain text files (Gutenberg is NOT JSON)
    romeo_text = response.text
    
    # Analyze the text string directly
    top_words = find_most_common_words(romeo_text, 10)
    
    print(f"Top 10 words in Romeo and Juliet:")
    for count, word in top_words:
        print(f"{count}: {word}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

import requests
import statistics
from collections import Counter

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats_data = response.json()

weights = []
lifespans = []
countries = []

for cat in cats_data:
    # 1. Extract Weight (Metric)
    # The API format is "weight": {"metric": "3 - 5"}
    # We take the average of the range provided
    w_range = cat['weight']['metric'].split(' - ')
    avg_w = sum(float(x) for x in w_range) / len(w_range)
    weights.append(avg_w)

    # 2. Extract Lifespan
    # Format: "lifespan": "12 - 15"
    l_range = cat['life_span'].split(' - ')
    avg_l = sum(float(x) for x in l_range) / len(l_range)
    lifespans.append(avg_l)
    
    # 3. Collect Countries
    countries.append(cat['origin'])

def get_stats(data_list):
    return {
        'min': min(data_list),
        'max': max(data_list),
        'mean': statistics.mean(data_list),
        'median': statistics.median(data_list),
        'std_dev': statistics.stdev(data_list)
    }

# Output Results
print("--- Weight Stats (Metric) ---")
print(get_stats(weights))

print("\n--- Lifespan Stats (Years) ---")
print(get_stats(lifespans))

print("\n--- Frequency Table: Country ---")
country_counts = Counter(countries)
for country, count in country_counts.items():
    print(f"{country}: {count}")


# Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
import requests
from collections import Counter

# 1. We now MUST add the ?fields= parameter
# We request only the specific data points we need for your tasks
url = 'https://restcountries.com/v3.1/all?fields=name,area,languages'

response = requests.get(url)

if response.status_code == 200:
    countries_data = response.json()
    
    # --- Task: 10 Largest Countries ---
    # Safe sorting: handle cases where area might be missing or None
    sorted_by_area = sorted(
        countries_data, 
        key=lambda x: x.get('area', 0) if x.get('area') is not None else 0, 
        reverse=True
    )
    
    print("--- 10 Largest Countries ---")
    for country in sorted_by_area[:10]:
        # Note: 'name' is now a dict because we asked for the whole 'name' field
        common_name = country.get('name', {}).get('common', 'Unknown')
        area = country.get('area', 0)
        print(f"{common_name}: {area} sq km")

    # --- Task: 10 Most Spoken Languages ---
    all_languages = []
    for country in countries_data:
        # 'languages' comes as a dictionary like {"eng": "English", "fra": "French"}
        langs_dict = country.get('languages', {})
        for lang_name in langs_dict.values():
            all_languages.append(lang_name)
    
    counts = Counter(all_languages)
    print("\n--- 10 Most Spoken Languages ---")
    for lang, count in counts.most_common(10):
        print(f"{lang}: {count} countries")

else:
    print(f"Failed! Status: {response.status_code}")
    print(f"Reason: {response.json().get('message')}")