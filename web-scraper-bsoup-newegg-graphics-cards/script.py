from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
my_url = "https://www.newegg.com/global/in-en/Video-Cards-Video-Devices/Category/ID-38"

uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

print(page_soup.p)

item_cells = page_soup.findAll("div", {"class" : "item-cell"})
print(item_cells[0])

with open("container.html","w", encoding="utf-8") as container:
    container.write(str(item_cells[0]))
    container.close()
print()
print()

with open("scraped-items.csv","w") as scraped:
    for item_cell in item_cells:
        brand = re.search(r"title=\"([\w ]*)\"",str(item_cell.findAll("a", {"class" : "item-brand"})[0])).group(1)
        name = item_cell.findAll("a", {"class" : "item-title"})[0].text
        scraped.write(brand + ", " + name + "\n")
