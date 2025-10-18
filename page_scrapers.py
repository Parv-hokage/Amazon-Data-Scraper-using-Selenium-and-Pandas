from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Info_Bot:
    def __init__(self, url_list):
        #driver setup
        self.list_of_brand_names = []
        self.list_of_product_ratings = []
        self.list_of_number_of_reviews = []
        self.list_of_prices = []
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
        chrome_options.add_argument("--window-size=1280,800")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        for i in range(100):
            self.driver.get(url_list[i])
            self.scrape()
            print(f"{i + 1} product info scrapped")
        self.driver.quit()
    def scrape(self):
        try:
            main_price = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
            )
            self.list_of_prices.append(main_price.text)
        except:
            self.list_of_prices.append("N/A")
        try:
            brand_name = self.driver.find_element(By.CSS_SELECTOR, ".po-brand .a-span9 span").text
        except:
            brand_name = "N/A"
        self.list_of_brand_names.append(brand_name)
        try:
            product_rating = self.driver.find_element(By.CSS_SELECTOR, "#acrPopover span a span").text
        except:
            product_rating = "Not Available"
        self.list_of_product_ratings.append(product_rating)
        try:
            number_of_reviews = self.driver.find_element(By.ID, "acrCustomerReviewText").text
        except:
            number_of_reviews = "Not Available"
        self.list_of_number_of_reviews.append(number_of_reviews)