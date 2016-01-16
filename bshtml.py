# using beautifulsoup to extract href tags using a python code
import urllib.request
from bs4 import BeautifulSoup


url = input('Enter -')

html =urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# retreive a list of anchor tags
# each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
    print(tag.get('href',None))
