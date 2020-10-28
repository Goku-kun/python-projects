import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.google.com/")

print(webpage.status_code)
print(webpage.headers)

sourcecode = webpage.content

soup = BeautifulSoup(sourcecode, "lxml")

# All the links on the page

links = soup.find_all("a")

with open("links.txt","w") as f:
    for link in links:
        f.write(link.attrs["href"] + "\n")
    f.close()