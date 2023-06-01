import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to scrape data from the provided URL
def scrape_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the content you want to scrape
        content = soup.find('div', {'id': 'mw-content-text'})

        # Extract the text from the content
        text = content.get_text()

        return text
    else:
        return None

# Create the Streamlit app
def main():
    st.title("Web Scraper")
    url = st.text_input("Enter the URL:")
    if st.button("Scrape"):
        if url:
            scraped_data = scrape_data(url)
            if scraped_data:
                st.text_area("Scraped Data", value=scraped_data)
            else:
                st.error("Error: Failed to scrape data. Please check the URL.")
        else:
            st.warning("Please enter a URL.")

if __name__ == '__main__':
    main()
