import requests
from bs4 import BeautifulSoup

# URL of the website
url = 'http://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book titles
book_titles = soup.find_all('h3')

# Extract and print the titles
for title in book_titles:
    print(title.text)
