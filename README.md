# 💻 Amazon Product Data Scraper (OOP with Selenium & Pandas)

This project is a robust web scraper designed to extract detailed product information from Amazon's
search resultsand individual product pages. It utilizes **Object-Oriented Programming (OOP)** and industry-standard 
Python libraries to handle dynamic content and structure data efficiently.

---

## ✨ Features

* **Object-Oriented Design (OOP):** Logic is separated into two classes (`Scrapper` and `Info_Bot`) for modularity and easy maintenance.
* **Dynamic Content Handling:** Uses **Selenium WebDriver** to interact with JavaScript-rendered pages (essential for Amazon).
* **Anti-Detection Measures:** Configured with headless mode, a custom User-Agent, and specific flags to mitigate common bot-detection challenges.
* **Data Extraction:** Fetches key metrics including **ASINs**, **Prices**, **Brands**, **Ratings**, and **Review Counts**.
* **Data Output:** Structures the scraped data using **Pandas** and saves it to a clean CSV file.

---

## 🚀 Getting Started

### Prerequisites

You need **Python** installed on your system, and the following libraries:
Ensure you have a browser installed (like Chrome) as Selenium will control it.
```bash
pip install selenium pandas
(The script generates an amazon_products.csv file in the project folder. An example of the structured data output
 is available in the example_output.csv file in this repository, shown in part below:)

### Project Structure

| File | Description |
| :--- | :--- |
| `main.py` | The main execution script. It initializes the scraper, runs the workflow, and uses Pandas to process and save the final data. |
| `page_scrapers.py` | Contains the **`Info_Bot`**  |
| `URL_scrapper.py` | Contains the **`Scrapper`** |

---

## 📈 Output Data Sample

The scraper structures the collected information into an `amazon_products.csv` file. A sample of the output data is shown below:

| Product Name | ASIN | Price | Brand | Rating | Number of Reviews | URL |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **XMART INDIA Drawer Organizers...** | B08BVV3FVQ | 219 | XMART INDIA | 4.2 | 1,834 ratings | https://www.amazon.in/XMART-INDIA... |
| **HomeWiz Multi-Purpose 360° Rotating...** | B0CJXCT62J | 99 | HomeWiz | 4.8 | 222 ratings | https://www.amazon.in/HomeWiz-Multi-Purpose... |
| **Satpurush Fridge Storage Boxes (Pack of 6)** | B0DZT3QQ59 | 288 | Satpurush | 4.3 | 1,779 ratings | https://www.amazon.in/Satpurush-Refrigerator... |
| **Xiran 6 Fridge Storage Boxes Fridge Organize...** | B0BQQ2ZSQX | 319 | Xiran | 4.2 | 3,892 ratings | https://www.amazon.in/Xiran-Fridge-Organizer... |

*Note: The product URLs have been truncated here for readability.*
* **[Download Full Sample Data (CSV)](./example_output.csv)**

## ⚠️ Important Note (Stability)

As a web scraping tool, this project relies on the current structure (HTML/CSS selectors) of the Amazon website.
 **Amazon frequently updates its site layout.** If Amazon changes its page structure, the selectors used in the `Scrapper`
and `Info_Bot` classes may become invalid, rendering the script temporarily useless until the selectors are updated.
