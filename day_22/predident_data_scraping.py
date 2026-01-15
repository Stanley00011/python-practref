# Scrape the presidents table and store the data as json
# (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
# The table is not very structured and the scrapping may take very long time.


import requests
from bs4 import BeautifulSoup
import json
import re
import csv

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# 1. Find the specific table
# We find the <h2> with id="Presidents", then find the next table tag
presidents_table = soup.find('h2', {'id': 'Presidents'}).find_next('table', {'class': 'wikitable'})

presidents_list = []

# 2. Iterate through rows (skip the header row)
for row in presidents_table.find_all('tr')[1:]:
    cells = row.find_all(['td', 'th'])
    
    # Wikipedia tables are tricky; we filter for rows that actually have data
    if len(cells) > 5:
        # Extract data from specific columns
        # Indexing might vary slightly due to hidden cells, but usually:
        # cells[0] or [1] = Number, cells[2] or [3] = Name, cells[4] = Term
        
        # We use stripping and regex to remove Wikipedia citations like [a] or [1]
        name = re.sub(r'\[.*?\]', '', cells[2].get_text(strip=True))
        term = re.sub(r'\[.*?\]', '', cells[3].get_text(strip=True))
        party = re.sub(r'\[.*?\]', '', cells[5].get_text(strip=True))

        presidents_list.append({
            "name": name,
            "term": term,
            "party": party
        })

# # 3. Store as JSON
# with open('us_presidents.json', 'w', encoding='utf-8') as f:
#     json.dump(presidents_list, f, indent=4)

# print(f"Successfully scraped {len(presidents_list)} presidents.")


# 3. Store as CSV
filename = 'us_presidents.csv'
keys = presidents_list[0].keys()  # This gets ["name", "term", "party"] from your list

with open(filename, 'w', newline='', encoding='utf-8') as f:
    # DictWriter is perfect since your data is a list of dictionaries
    writer = csv.DictWriter(f, fieldnames=keys)
    
    # Write the header row (name, term, party)
    writer.writeheader()
    
    # Write all the data rows
    writer.writerows(presidents_list)

print(f"Successfully scraped {len(presidents_list)} presidents and saved to {filename}.")