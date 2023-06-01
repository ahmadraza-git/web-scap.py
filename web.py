import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_articles(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the HTML elements containing the articles
        articles = soup.find_all("h2", class_="article-title")
        
        # Extract the titles of the articles
        titles = [article.text.strip() for article in articles]
        
        return titles
    else:
        st.error("Failed to retrieve articles.")

# Create a Streamlit app
def main():
    st.title("Web Scraping App")
    
    # Input URL
    url = st.text_input("Enter a website URL")
    
    if st.button("Scrape"):
        if url:
            titles = scrape_articles(url)
            if titles:
                st.success("Articles scraped successfully!")
                st.write("Titles:")
                for title in titles:
                    st.write(title)
            else:
                st.error("No articles found.")
        else:
            st.warning("Please enter a website URL.")

if __name__ == "__main__":
    main()
