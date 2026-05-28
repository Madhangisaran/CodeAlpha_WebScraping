import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    availability = book.find("p", class_="instock availability").text.strip()

    rating = book.p["class"][1]

    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating
    })

df = pd.DataFrame(data)

df.to_excel("books.xlsx", index=False)

print("Excel File Saved Successfully!")