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
