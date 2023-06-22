from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.options import Options

import datetime
import logging
import time

app = Flask(__name__)

driver = webdriver.Chrome()

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def scrape_news():
    # List of news websites to scrape
    news_websites = [
        "https://www.bbc.com/news"
    ]

    # Initialize an empty list to store the news headlines
    headlines = []
    hrefs = []

    # Scrape each website and extract the headlines
    for website in news_websites:
        driver.get(website)
        # Specify the elements containing the headlines
        headline_container_class = "gs-c-promo-body"
        headline_tags = driver.find_elements("class name",headline_container_class)

        # Extract the headline information
        for tag in headline_tags:
            h3 = tag.find_element('tag name','h3')
            app.logger.debug(h3)
            headline = h3.text.strip()
            anchor = tag.find_element('tag name','a')
            href = anchor.get_attribute('href')
            if headline not in headlines:
                headlines.append((headline, href))

    driver.quit()
    return headlines


@app.route('/')
def index():
    # Call the function to scrape the news headlines
    news_headlines = scrape_news()

    # Pass the headlines to the HTML template
    return render_template('index.html', headlines=news_headlines)

if __name__ == '__main__':
    app.run()