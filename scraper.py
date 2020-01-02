from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url= "https://code.tutsplus.com/tutorials/building-ribbit-in-django--net-29957"
response=requests.get(url, timeout=5)

soup=BeautifulSoup(response.content, "html.parser")

print(soup.prettify())


