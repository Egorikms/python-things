from bs4 import BeautifulSoup as BS
import requests

url = "https://www.avito.ru/yaroslavl?cd=1&q=диван"
r = requests.get(url)
soup = BS(r.text, "html.parser")
items = soup.find_all("div", class_="items-listItem-Gd1jN js-catalog-item-enum").text

for item in items:
	print(item)






