from URL_scrapper import Scrapper
from page_scrapers import Info_Bot
import pandas
scrapper = Scrapper("https://www.amazon.in/s?i=kitchen&k=storage+organization", 100)
bot = Info_Bot(scrapper.list_of_urls)
print("Data Scrapping done arranging data")
product_names = []
product_asins = []
product_price = bot.list_of_prices
product_brands = bot.list_of_brand_names
product_ratings = bot.list_of_product_ratings
product_review_counts = bot.list_of_number_of_reviews
product_urls = []
for i in range(100):
    product_names.append(scrapper.list_of_product_names[i])
    product_asins.append(scrapper.asin_list[i])
    product_urls.append(scrapper.list_of_urls[i])


data = {
    "Product Name": product_names,
    "ASIN": product_asins,
    "Price": product_price,
    "Brand": product_brands,
    "Rating": product_ratings,
    "Number of Reviews": product_review_counts,
    "URL": product_urls
}

df = pandas.DataFrame(data)
df.to_csv("amazon_products.csv", index=False, encoding='utf-8-sig')
print("Data saved to amazon_products.csv")
