import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/"
response = requests.get(BASE_URL + "index.html")
html = response.content
scraped = BeautifulSoup(html, 'html.parser')

title_descriptions = []

articles = scraped.select(".product_pod")

for article in articles:
    title = article.h3.a["title"]
    title_url = article.h3.a["href"]
    
    product_response = requests.get(BASE_URL + title_url)
    product_html = product_response.content
    product_scraped = BeautifulSoup(product_html, 'html.parser')
    
    description = product_scraped.find("div", id="product_description").next_sibling.next_sibling
    
    title_descriptions.append({title: description.text.strip()})
    
print(title_descriptions)