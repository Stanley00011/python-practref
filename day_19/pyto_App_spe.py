import re
import os

def clean_text(text):
    """Removes special characters and lowercases the text."""
    # Removes everything except letters and spaces
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned.lower()

def remove_support_words(text_list, stop_words_path='./data/stop_words.py'):
    """Filters out common English stop words."""
    try:
        # Assuming stop_words.py contains a list named 'stop_words'
        # If it's a text file, you'd use f.read().split()
        from day_19.stop_words import stop_words
    except ImportError:
        # Fallback basic list if file is missing
        stop_words = ['the', 'and', 'is', 'to', 'of', 'in', 'a', 'that', 'i', 'it', 'for', 'on']
    
    return [word for word in text_list if word not in stop_words and len(word) > 1]

def get_text_from_source(source):
    """Helper to determine if input is a file path or a raw string."""
    if os.path.isfile(source):
        with open(source, 'r', encoding='utf-8') as f:
            return f.read()
    return source

def check_text_similarity(source1, source2):
    """Main function to evaluate similarity between two sources."""
    # 1. Get raw text
    raw1 = get_text_from_source(source1)
    raw2 = get_text_from_source(source2)
    
    # 2. Clean and Tokenize
    words1 = clean_text(raw1).split()
    words2 = clean_text(raw2).split()
    
    # 3. Remove stop words
    filtered1 = set(remove_support_words(words1))
    filtered2 = set(remove_support_words(words2))
    
    # 4. Calculate Jaccard Similarity (Intersection / Union)
    intersection = filtered1.intersection(filtered2)
    union = filtered1.union(filtered2)
    
    similarity_score = len(intersection) / len(union)
    return round(similarity_score * 100, 2)

# --- Execution: Michelle vs. Melania ---
michelle_path = './day_19/michelle_obama_speech.txt'
melina_path = './day_19/melina_trump_speech.txt'

score = check_text_similarity(michelle_path, melina_path)

print(f"Similarity Score: {score}%")