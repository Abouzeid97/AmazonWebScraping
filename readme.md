# 🛍️ Amazon Product Scraper API

This project is a Django-based POST API built with Django REST Framework and Selenium. It scrapes Amazon.eg based on a search term and returns a list of matching products with the following fields:

- **title**
- **url**
- **price**
- **rating**

---

## 🚀 Features

- Accepts a search query via POST request.
- Returns a JSON response with scraped Amazon product data.
- Uses **Selenium** to bypass Amazon’s bot detection and dynamic rendering.

---

## 📦 Requirements

- Python 3.9+
- Chrome + [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Django 5.x
- Django REST Framework
- Selenium

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/amazon-scraper-api.git
cd amazon-scraper-api
```
2. **Create a Virtual Environment & Activate**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the Server**
```bash
python manage.py runserver
```
5. **Test the API**
```bash
POST localhost:8000/scrape/
```
Send a JSON body like:
```bash
{
  "search_term": "laptop"
}
```
Response
```bash
[
  {
    "title": "HP Laptop 15s...",
    "url": "https://www.amazon.eg/dp/B0DNMM1RYQ",
    "price": 14599,
    "rating": 4.3
  },
  ...
]
```

❓ Why Selenium?

While BeautifulSoup is a great tool for parsing static HTML, Amazon dynamically loads product data and actively implements bot detection mechanisms that block traditional scrapers. Therefore, this project uses Selenium, which:

Interacts with the website like a real user.

Handles JavaScript-rendered content.

Helps bypass bot protection and load dynamic elements reliably.


This ensures more accurate and consistent scraping results from Amazon.eg.
