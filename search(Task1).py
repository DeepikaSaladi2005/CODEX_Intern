from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

# Function to perform Google search and scrape results
def google_search_scraper(query, num_results=10):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")  # Fix headless mode issue
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.google.com")

    # Find the search box and enter the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)  # Press Enter

    time.sleep(3)  # Allow time for results to load

    # Parse results using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    results = []
    for g in soup.find_all("div", class_="tF2Cxc")[:num_results]:  # Update this class if needed
        title = g.find("h3").text if g.find("h3") else "No Title"
        link = g.find("a")["href"] if g.find("a") else "No Link"
        snippet = g.find("div", class_="VwiC3b").text if g.find("div", class_="VwiC3b") else "No Description"
        
        results.append({"Title": title, "Link": link, "Snippet": snippet})

    driver.quit()
    
    return results

# Run the scraper and save results
if __name__ == "__main__":
    search_query = input("Enter search query: ")
    scraped_results = google_search_scraper(search_query, num_results=10)

    if scraped_results:
        # Display results
        for idx, result in enumerate(scraped_results, start=1):
            print(f"{idx}. {result['Title']}\n   {result['Link']}\n   {result['Snippet']}\n")

        # Save to CSV
        df = pd.DataFrame(scraped_results)
        df.to_csv("google_search_results.csv", index=False, encoding="utf-8-sig")
        print("Results saved to google_search_results.csv ✅")
    else:
        print("❌ No search results found. Try adjusting the code.")
