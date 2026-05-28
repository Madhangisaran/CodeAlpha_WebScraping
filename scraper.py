import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://quotes.toscrape.com/page/{}/"

data = []

for page in range(1, 4):

    print(f"Scraping Page {page}...")

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        text = quote.find("span", class_="text").text

        author = quote.find("small", class_="author").text

        tags = quote.find_all("a", class_="tag")

        tag_list = []

        for tag in tags:
            tag_list.append(tag.text)

        data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tag_list)
        })

df = pd.DataFrame(data)
df.to_excel("quotes_intermediate.xlsx", index=False)


print("Intermediate CSV File Saved Successfully!")