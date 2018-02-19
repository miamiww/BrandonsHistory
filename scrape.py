import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import lxml

url = "http://localhost:3000/brandon.html"


response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"html.parser")
brs = soup.findAll('br')
dateZ = []
for br in brs:
    dateZ.append(br.nextSibling)
#    print br.nextSibling

dateZ = [date for date in dateZ if date is not None]
# dateZ = [date for date in dateZ if date is not "Search"]
dateZ = [date for date in dateZ if "Search" not in date]
for date in dateZ:
    print date.encode("utf-8")
