from bs4 import BeautifulSoup
import requests

PRODUCT_URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(PRODUCT_URL)

product_html = response.text

soup = BeautifulSoup(product_html, "html.parser")

price_whole = soup.select_one("#corePriceDisplay_desktop_feature_div .aok-offscreen")

price_as_float = float(price_whole.get_text(strip=True).replace('$', ""))
print(price_as_float)


## send email
