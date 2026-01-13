
# UCI is one of the most common places to get data sets for data science and machine learning.
#  Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). 
# Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

import requests
from bs4 import BeautifulSoup

# The new, active URL
url = 'https://archive.ics.uci.edu/datasets'

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # In the new design, dataset names are usually within <a> tags 
        # inside specific container classes (like 'font-semibold')
        print("--- Top Datasets on UCI ---")
        
        # We find all links that point to a specific dataset page
        datasets = soup.find_all('a', href=True)
        
        count = 0
        for link in datasets:
            # New UCI URLs for individual datasets start with /dataset/
            if '/dataset/' in link['href']:
                name = link.get_text(strip=True)
                if name: # Ensure it's not empty
                    print(f"{count + 1}. {name}")
                    count += 1
            
            if count == 10: # Stop after 10
                break
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")