import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def scrape_newegg():
    service = Service(os.path.join(os.path.dirname(__file__), 'chromedriver'))
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=service, options=options)
    url = "https://www.newegg.com/p/pl?d=laptop"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.item-cell")))

    items = driver.find_elements(By.CSS_SELECTOR, "div.item-cell")
    print(f"Found {len(items)} items")

    data = []

    for item in items[:5]:  # example with first 5 items
        title = item.find_element(By.CSS_SELECTOR, "a.item-title").text
        price_whole = item.find_elements(By.CSS_SELECTOR, "li.price-current strong")
        price_fraction = item.find_elements(By.CSS_SELECTOR, "li.price-current sup")
        if price_whole and price_fraction:
            price = price_whole[0].text + price_fraction[0].text
        else:
            price = "No price"

        print(f"{title} — {price}")
        data.append({"Title": title, "Price": price})

    driver.quit()

    # saving into CSV
    df = pd.DataFrame(data)
    df.to_csv("src/output/newegg_laptops.csv", index=False)
    print("Data saved to newegg_laptops.csv")

if __name__ == "__main__":
    scrape_newegg()
