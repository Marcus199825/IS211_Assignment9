# Script for scraping NBA Finals information: https://en.wikipedia.org/wiki/NBA_Finals #

python
import requests
from bs4 import BeautifulSoup

def scrape_nba_finals_info():
    url = "https://en.wikipedia.org/wiki/NBA_Finals"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    info_paragraph = soup.find("div", class_="mw-parser-output").find_all("p")[0].text.strip()
    return info_paragraph

if __name__ == "__main__":
    nba_info = scrape_nba_finals_info()
    print(nba_info)



if __name__ == "__main__":
    pass
