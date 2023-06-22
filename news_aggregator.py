import requests
from bs4 import BeautifulSoup

def scrape_news():
    # List of news websites to scrape
    news_websites = [
        "https://www.bbc.com/news"
    ]

    # Initialize an empty list to store the news headlines
    headlines = []

    # Scrape each website and extract the headlines
    for website in news_websites:
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Specify the HTML tags containing the headlines
        headline_container_class = "gs-c-promo-heading__title"
        headline_tags = soup.find_all('h3', class_=headline_container_class)
        print(headline_tags)
    

        # Extract the text from the headline tags
        for tag in headline_tags:
            headline = tag.text.strip()
            if headline not in headlines:
                headlines.append(headline)

    return headlines

# Call the function to scrape the news headlines
news_headlines = scrape_news()

# Print the headlines
# for headline in news_headlines:
#     # print(headline)