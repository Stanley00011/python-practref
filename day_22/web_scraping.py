""" 
What is Web Scrapping
The internet is full of huge amount of data which can be used for different purposes. To collect this data we need to know how to scrape data from a website.

Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.

In this section, we will use beautifulsoup and requests package to scrape data. The package version we are using is beautifulsoup 4.

To start scraping websites you need requests, beautifoulSoup4 and a website.
"""

'''
# To scrape data from websites, basic understanding of HTML tags and CSS selectors is needed. 
# We target content from a website using HTML tags, classes or/and ids. Let us import the requests 
# and BeautifulSoup module 

import requests
from bs4 import BeautifulSoup

# Let us declare url variable for the website which we are going to scrape.

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/datasets'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

'''
# Using beautifulSoup to parse content from the page
import requests
from bs4 import BeautifulSoup
import json

# 1. Setup the new URL and Headers (to avoid timeouts)
url = 'https://archive.ics.uci.edu/datasets'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# 2. Container for our data
datasets_list = []

# 3. Find the dataset containers
# On the new site, datasets are typically in <a> tags within specific div classes
# or simply identified by their unique URL path '/dataset/'
links = soup.find_all('a', href=True)

# We use a set to avoid duplicates since the site has multiple links for one dataset
seen_titles = set()

for link in links:
    href = link['href']
    if '/dataset/' in href:
        title = link.get_text(strip=True)
        
        # Ensure it's a valid title and not already processed
        if title and title not in seen_titles:
            seen_titles.add(title)
            
            # Find the sibling or parent text for a short description if available
            # This is a simplified extraction for the new dynamic layout
            datasets_list.append({
                "dataset_name": title,
                "url": f"https://archive.ics.uci.edu{href}"
            })

# 4. Save the results to a JSON file
with open('uci_datasets.json', 'w', encoding='utf-8') as f:
    json.dump(datasets_list, f, indent=4, ensure_ascii=False)

print(f"Successfully extracted {len(datasets_list)} datasets to uci_datasets.json")


