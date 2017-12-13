from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

quotes = soup.select('div.quote')[0]

quotes.select('span.text')

print(quotes)