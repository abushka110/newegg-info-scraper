# Newegg Price Scraper

A Python script to scrape laptop names and prices from [Newegg.com](https://www.newegg.com).

---

## Features

- Fetches the HTML page from Newegg  
- Parses product names and prices  
- Prints the results to the console  
- Saves results to CSV  
(in developments) - Search laptops by parameters from saved CSV (max price, keyword)

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

## Usage

### Scrape laptops from Newegg:

```bash
python src/scraper.py
