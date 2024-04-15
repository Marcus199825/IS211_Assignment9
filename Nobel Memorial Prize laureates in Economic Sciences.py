# Script for scraping Nobel Memorial Prize laureates: https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences" #

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economics"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the laureates
table = soup.find("table", {"class": "wikitable"})

# Extract table data into a DataFrame
df = pd.read_html(str(table))[0]

# Display the DataFrame
print(df)

