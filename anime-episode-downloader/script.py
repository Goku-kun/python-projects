import requests
from bs4 import BeautifulSoup
import re
import urllib

url = "https://4anime.to/anime/shingeki-no-kyojin-the-final-season"
webpage = requests.get(url).content
parsed_webpage = BeautifulSoup(webpage, "html.parser")
webpage_str = parsed_webpage.prettify()
with open('value.html', 'w') as f:
    f.write(webpage_str)
    f.close()
name = "shingeki"
search_string = ".*" + name + ".*"
a_tags = parsed_webpage.find_all('a', href=re.compile(r""+search_string))

print(a_tags[0]['href'])

episode_webpage = requests.get(str(a_tags[0]['href'])).content
parsed_episode = BeautifulSoup(episode_webpage, 'html.parser')
str_episode = parsed_episode.prettify()
with open('episode.html', 'w') as f:
    f.write(str_episode)
    f.close()

video_link = parsed_episode.find_all('source', src=True)[0]['src']

r = requests.get(video_link, stream=True)

# download started
with open('episode-1.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024*1024):
        if chunk:
            f.write(chunk)

with open('links.txt', 'w') as f:
    for a_tag in a_tags:
        f.write(str(a_tag) + '\n')
