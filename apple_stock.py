# Script for scraping Nobel Memorial Prize laureates: https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences" #

python
import requests
from bs4 import BeautifulSoup

def scrape_nobel_laureates():
    url = "https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    laureates_list = []
    table = soup.find("table", class_="wikitable")
    rows = table.find_all("tr")[1:]
    
    for row in rows:
        columns = row.find_all("td")
        year = columns[0].text.strip()
        laureates = columns[1].text.strip()
        laureates_list.append(f"{year}. {laureates}")
    
    return laureates_list

if __name__ == "__main__":
    laureates = scrape_nobel_laureates()
    for laureate in laureates:
        print(laureate)


if __name__ == "__main__":
    pass
