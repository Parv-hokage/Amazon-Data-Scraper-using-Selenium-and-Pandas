from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scrapper:
    def __init__(self, first_page_url, number_of_pages):
        self.url = first_page_url
        self.number_of_pages = number_of_pages
        self.asin_list = []
        #driver setup
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
        chrome_options.add_argument("--window-size=1280,800")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.url)
        print("set up done\nStarting scraping...\nWait for 9 minutes...")
        #logic
        self.list_of_urls = []
        self.list_of_product_names = []
        while len(self.list_of_urls) < self.number_of_pages:
            self.scrape()
            self.next_page()
        self.driver.close()
        self.driver.quit()
    def scrape(self):
        try:
            import time
            time.sleep(2)
            links = self.driver.find_elements(By.CSS_SELECTOR, "[data-cy='title-recipe'] a")
            for link in links:
                url = link.get_attribute("href")
                text = link.text
                if not url:
                    continue
                if url == "javascript:void(0)":
                    continue
                if url.endswith("#"):
                    continue
                if "/dp/" not in url and "/sspa/" not in url:
                    continue
                if text.strip() == "Sponsored" or text.strip() == "":
                    continue
                if "/dp/" not in url and "/gp/product/" not in url:
                    continue
                try:
                    if "/dp/" in url:
                        part = url.split("/dp/")[1]
                        asin = part.split("/")[0]
                    elif "/gp/product/" in url:
                        part = url.split("/gp/product/")[1]
                        asin = part.split("/")[0]
                    else:
                        continue
                except:
                    continue
                if asin in self.asin_list:
                    continue
                self.asin_list.append(asin)
                self.list_of_urls.append(url)
                self.list_of_product_names.append(text)
        except Exception as e:
            print(f"Error: {e}")

    def next_page(self):
        try:
            target = self.driver.find_element(By.LINK_TEXT, "Next")
            link = target.get_attribute("href")
            self.driver.get(link)
        except Exception as e:
            print(f"Could not go to next page: {e}")