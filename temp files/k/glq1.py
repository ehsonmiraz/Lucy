from google import search
import urllib
from bs4 import BeautifulSoup
import webbrowser
def google_scrape(url):
    thepage = urllib.urlopen(url)
   # thepage=webbrowser.open(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text
i = 1
query = input('enter')
for url in search(query, stop=10):
    a = google_scrape(url)
    i += 1
