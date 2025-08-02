# Newegg Price Scraper

A Python script to scrape laptop names and prices from [Newegg.com](https://www.newegg.com).

---

## Features

- Fetches the HTML page from Newegg  
- Parses product names and prices  
- Prints the results to the console  
- Saves results to CSV  
(in development) - Search laptops by parameters from saved CSV (max price, keyword)

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/newegg-price-scraper.git
    cd newegg-price-scraper
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r src/requirements.txt
    ```

---

## ChromeDriver Setup

This project requires **ChromeDriver** to control Chrome via Selenium.

1. Check your Chrome version:  
   Open Chrome and go to `chrome://settings/help`

2. Download the matching ChromeDriver version from:  
   [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)  
   or use the latest Chrome for Testing drivers:  
   [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

3. Extract the driver and place the `chromedriver` executable into the `src/` folder.

4. (Linux/macOS) Make it executable:  
    ```bash
    chmod +x src/chromedriver
    ```

---

## Usage

### Scrape laptops from Newegg:

```bash
python src/scraper.py
