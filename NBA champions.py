# Script for scraping NBA Finals information: https://en.wikipedia.org/wiki/NBA_Finals #

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the NBA champions
table = soup.find("table", {"class": "wikitable"})

# Extract table data into a DataFrame
df = pd.read_html(str(table))[0]

# Display the DataFrame
print(df)

