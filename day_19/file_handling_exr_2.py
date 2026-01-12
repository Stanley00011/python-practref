# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

import re 
def extract_incoming_emails(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
# This regex looks specifically for the address following "From: "
        # \S+ matches any non-whitespace characters (the email address)
        emails = re.findall(r'From: (\S+@\S+)', content)
        return emails
        
    except FileNotFoundError:
        return "File not found."


emails_list = extract_incoming_emails('./day_19/email_exchanges.txt')
print(emails_list[:5]) # Show first 5

# Find the most common words in the English language. Call the name of your function find_most_common_words, 
# it will take two parameters - a string or a file and a positive integer, indicating the number of words. 
# Your function will return an array of tuples in descending order. Check the output.   day_19/email_exchanges.txt


import re
import os
from collections import Counter

def find_most_common_words(input_data, n):
    # 1. Check if input is a file or a string
    if os.path.isfile(input_data):
        with open(input_data, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = input_data

    # 2. Clean the text: remove non-alphabetic characters and lowercase everything
    # This ensures "The" and "the" are counted together
    words = re.findall(r'\b[a-z]+\b', text.lower())

    # 3. Count occurrences
    counts = Counter(words)

    # 4. Format to [(count, word)] and sort descending
    # Counter.most_common(n) gives [(word, count)], so we swap them
    result = [(count, word) for word, count in counts.most_common(n)]
    
    return result

# --- Test Outputs ---
print(find_most_common_words('sample.txt', 10))
print(find_most_common_words('sample.txt', 5))


# Use the function, find_most_frequent_words to find:
# The ten most frequent words used in Obama's speech
# The ten most frequent words used in Michelle's speech
# The ten most frequent words used in Trump's speech
# The ten most frequent words used in Melina's speech

import re
import os
from collections import Counter

def find_most_common_words(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Extract words: remove punctuation and lowercase
        words = re.findall(r'\b[a-z]+\b', text.lower())
        
        # Count and format as [(count, word)]
        counts = Counter(words)
        return [(count, word) for word, count in counts.most_common(n)]
        
    except FileNotFoundError:
        return f"File not found at {file_path}"

# Define the file paths
base_path = './day_19/'
speeches = {
    "Obama": "obama_speech.txt",
    "Michelle Obama": "michelle_obama_speech.txt",
    "Donald Trump": "donald_speech.txt",
    "Melania Trump": "melina_trump_speech.txt"
}

# Run the analysis for each speaker
for speaker, filename in speeches.items():
    full_path = os.path.join(base_path, filename)
    print(f"--- Top 10 Words: {speaker} ---")
    results = find_most_common_words(full_path, 10)
    
    if isinstance(results, list):
        for count, word in results:
            print(f"{count}: {word}")
    else:
        print(results)
    print("\n")


# Find the 10 most repeated words in the romeo_and_juliet.txt
romeo_path = os.path.join(base_path, 'romeo_and_juliet.txt')
print('--- Top 10 Words: Romeo and Juliet ---')
results = find_most_common_words(romeo_path, 10)

if isinstance(results, list):
    for count, word in results:
        print(f"{count}: {word}")
else:
    print(results)



# Read the hacker news csv file and find out:

# Count the number of lines containing python or Python
f = open('./day_19/hacker_news.csv', 'r', encoding='utf-8')
content = f.read()
matches = re.findall(r'python', content, re.I)
print(f"Total mentions: {len(matches)}")
print(matches[:10]) # Show the first 10 matches found

# Count the number lines containing JavaScript, javascript or Javascript

# Count the number lines containing Java and not JavaScript

# optimised

import csv

def analyze_hacker_news(file_path):
    # Initialize our counters
    python_count = 0
    javascript_count = 0
    java_only_count = 0

    try:
        # Use 'with' to ensure the file closes automatically
        with open(file_path, 'r', encoding='utf-8') as f:
            # Skip the header row if it exists
            next(f) 
            
            for line in f:
                # Convert line to lowercase once to make searching easier
                lowered_line = line.lower()
                
                # 1. Count Python or python
                if 'python' in lowered_line:
                    python_count += 1
                
                # 2. Count JavaScript, javascript, or Javascript
                if 'javascript' in lowered_line:
                    javascript_count += 1
                
                # 3. Count Java but NOT JavaScript
                # We check for 'java' and make sure 'javascript' isn't there
                if 'java' in lowered_line and 'javascript' not in lowered_line:
                    java_only_count += 1

        # Print the results
        print(f"Python mentions: {python_count}")
        print(f"JavaScript mentions: {javascript_count}")
        print(f"Java (only) mentions: {java_only_count}")

    except FileNotFoundError:
        print("File not found. Check your file path.")

# --- Run the function ---
analyze_hacker_news('./day_19/hacker_news.csv')