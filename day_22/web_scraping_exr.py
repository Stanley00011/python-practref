import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bu.edu/president/boston-university-facts-stats/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

data_collection = []

# 1. Target the specific list you found
stats_list = soup.find_all('li') # We'll filter these in the loop

for li in stats_list:
    # 2. Look for the specific span classes you identified
    label_tag = li.find('span', class_='stat-label')
    figure_tag = li.find('span', class_='stat-figure')
    
    # 3. Only add to our list if BOTH the label and figure exist
    if label_tag and figure_tag:
        label = label_tag.get_text(strip=True)
        figure = figure_tag.get_text(strip=True)
        
        data_collection.append({
            "stat_name": label,
            "stat_value": figure
        })

# 4. Save to JSON
with open('bu_stats.json', 'w', encoding='utf-8') as f:
    json.dump(data_collection, f, indent=4)

print(f"Success! Scraped {len(data_collection)} facts and saved to bu_stats.json")

# Quick print to console to verify
for item in data_collection[:5]:
    print(f"{item['stat_name']}: {item['stat_value']}")