import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = [title.text for title in soup.find_all('span', class_='text')]
for title in titles:
    print(title)