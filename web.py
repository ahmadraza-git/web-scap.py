import streamlit as st
from bs4 import BeautifulSoup
import requests


def scrape_news():
    # Send a GET request to the website
    url = "https://www.example.com/news"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the HTML elements containing the news articles
        articles = soup.find_all("div", class_="article")
        
        # Extract the title and URL for each article
        for article in articles:
            title = article.find("h2").text.strip()
            link = article.find("a")["href"]
            
            print("Title:", title)
            print("URL:", link)
            print("------")
    else:
        print("Failed to retrieve news.")

# Call the function to start scraping
scrape_news()
