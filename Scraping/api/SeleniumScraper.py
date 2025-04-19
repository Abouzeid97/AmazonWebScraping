from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time, re

def DataCleaning(price, rating):
    if price:
        price_text = price
        price_text = price_text.replace(",", "")
        price = float(price_text)
    else:
        price = None

    rating_text = rating
    rating_match = re.match(r"(\d+(\.\d+)?)", rating_text)
    if rating_match:
        rating = float(rating_match.group(1))
        print("Rating:", rating)
    else:
        rating = None

    return price, rating

def scraper(search_term):
    # Setup Selenium WebDriver
    driver = webdriver.Chrome()
    # Ask user for search input
    url = f"https://www.amazon.eg/s?k={search_term}&language=en_AE"
    driver.maximize_window()

    driver.get(url)
    if "503" in driver.page_source:
        time.sleep(6)
        link = driver.find_element(By.XPATH, '//a[@href="https://www.amazon.eg/ref=cs_503_link/"]')
        original_href = link.get_attribute("href")
        actions = ActionChains(driver)
        actions.move_to_element(link).click().perform()
        time.sleep(6)
        new_href = original_href + "?language=en_AE"
        driver.get(new_href)
        time.sleep(5)
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        # Click the search box to focus it
        search_box.click()
        # Type the product name (e.g., "laptop") and hit Enter
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)

    last_page_element = driver.find_element(By.XPATH, '//span[@class="s-pagination-item s-pagination-disabled"]')

    # Get the text content and convert to int
    last_page_number = int(last_page_element.text)

    print("Last page number:", last_page_number)
    time.sleep(10)
    
    results = []
    for i in range(last_page_number):
        # Get all product elements    
        print(f"page {i}")
        products = driver.find_elements(By.XPATH, '//div[@role="listitem"]')

        print(f"\nFound {len(products)} products with role='listitem'\n")

        # Loop through and extract titles + hrefs
        for product in products:
            try:
                title_elem = product.find_element(By.XPATH, ".//h2//span")
                link_elem = product.find_element(By.XPATH, ".//a[@class='a-link-normal s-line-clamp-4 s-link-style a-text-normal']")
                rating_elem = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']")
                rating_text = rating_elem.get_attribute("textContent").strip()
                price_elem = product.find_element(By.XPATH, ".//span[@class='a-price-whole']")
                price, rating = DataCleaning(price_elem.text, rating_text)
                results.append({
                "title": title_elem.text,
                "url": "https://www.amazon.eg" + link_elem.get_attribute("href"),
                "price": price,
                "rating": rating
            })
            except Exception as e:
                print("this is not a product")
        if i != last_page_number-1:
            next_button = driver.find_element(By.XPATH, '//a[contains(@aria-label, "Go to next page")]')
            next_button.click()
            time.sleep(5)


    driver.quit()
    return results
