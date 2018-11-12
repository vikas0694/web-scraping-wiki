import requests
from bs4 import BeautifulSoup
import pandas as pd

# get html code  from source page
url = "https://en.wikipedia.org/wiki/NIFTY_50"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# extract required table
table = soup.find("table", { "class" : "wikitable sortable" })
companies = []
symbols = []
sectors = []

for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 3:
        companies.append(cells[0].find(text=True))
        symbols.append(cells[1].findAll(text=True))
        sectors.append(cells[2].find(text=True))


# write data to dataframe
data = pd.DataFrame({"Company Name": companies, "Symbol": symbols, "Sector": sectors})

print(data)
