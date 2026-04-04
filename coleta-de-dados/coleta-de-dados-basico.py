import requests
from bs4 import BeautifulSoup
import pandas

response = requests.get("https://stooq.com/q/d/?s=%5Ebvp&i=d")
print(response.text[:600])

soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:1000])

print('Pandas: ')
url_dados = pandas.read_html('https://stooq.com/q/d/?s=%5Ebvp&i=d')
print(url_dados[0].head(10))