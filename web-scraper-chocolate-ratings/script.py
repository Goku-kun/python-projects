import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

soup = BeautifulSoup(webpage.content, "html.parser")

ratingtags = soup.find_all(attrs={"class":"Rating"})

ratings = []

for ratingtag in ratingtags[1:]:
    ratings.append(float(ratingtag.get_text()))

print(ratings[0])

plt.hist(ratings)
plt.show()

companytags = soup.find_all(attrs={"class": "Company"})
company = []
for companytag in companytags[1:]:
    company.append(companytag.get_text())

cocoa_percent = []
cocoatags = soup.find_all(attrs={"class": "CocoaPercent"})
# print(int(cocoatags[0].get_text().strip("%")))
for cocoatag in cocoatags[1:]:
    cocoa_percent.append(float(cocoatag.get_text().replace("%","")))

dictionary_for_dataframe = {"Company": company, "Rating": ratings, "CocoaPercent":cocoa_percent}

dataframe = pd.DataFrame.from_dict(dictionary_for_dataframe)

mean_vals = dataframe.groupby("Company").Rating.mean()
ten_best = mean_vals.nlargest(10)
print(ten_best)


plt.clf()
plt.scatter(dataframe.CocoaPercent, dataframe.Rating)
z = np.polyfit(dataframe.CocoaPercent, dataframe.Rating, 1)
line_function = np.poly1d(z)
plt.plot(dataframe.CocoaPercent, line_function(dataframe.CocoaPercent), "r--")
plt.show()
