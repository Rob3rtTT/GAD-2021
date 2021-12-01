"""This was done for educational purposes only"""
from bs4 import BeautifulSoup
import requests
import re

product_name = input("What Product are you looking for? ")
url = f'https://www.emag.ro/search/stoc/{product_name}'
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
page_text = doc.find(class_="visible-xs visible-sm").text.strip()
pages = int(str(page_text).split(" ")[-1])
items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.emag.ro/search/stoc/{product_name}/p{page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="page-container")
    items = div.find_all(text=re.compile(product_name))
    
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent['href']
        price = div.find(class_="product-new-price").get_text()

        items_found[item] = {"price": price, "link": link}

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
	print(item[0])
	print(f"${item[1]['price']}")
	print(item[1]['link'])
	print("-----------------------------------------------------")
