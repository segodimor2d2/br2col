import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Mercado Libre search page
base_url = "https://listado.mercadolibre.com.co/"
search_query = "cadiveu-mascara"
search_url = f"{base_url}{search_query}"

# Fetch the search results page
response = requests.get(search_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find and extract product details
products = []
for item in soup.find_all("li", class_="ui-search-layout__item"):
    import ipdb; ipdb.set_trace()
    title = item.find("h2", class_="ui-search-item__title").text
    price = item.find("span", class_="price-tag-fraction").text
    link = item.find("a", class_="ui-search-link")["href"]

    products.append({"title": title, "price": price, "link": link})

# Convert to DataFrame and save to CSV
df = pd.DataFrame(products)
df.to_csv("mercado_libre_products.csv", index=False)

print("Scraping complete. Data saved to mercado_libre_products.csv")
