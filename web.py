import streamlit as st
import pandas as pd
import numpy as np
# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import streamlit as st

# Define the web scraping function
def scrape_website(url, keyword):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape the desired data from the website based on the keyword
    # Modify this section according to your specific requirements
    data = []
    items = soup.find_all('div', class_='example-class')
    for item in items:
        if keyword.lower() in item.text.lower():
            data.append(item.text.strip())

    # Return the scraped data
    return data

# Create a Streamlit app
def main():
    # Set the title of the app
    st.title("Web Scraping App")

    # Get the user input URL
    url = st.text_input("Enter the URL of the website to scrape:")

    # Get the user input search keyword
    keyword = st.text_input("Enter a keyword to search on the website:")

    # Check if the user has entered a URL and a keyword
    if url and keyword:
        # Add a submit button
        if st.button("Scrape"):
            # Call the web scraping function
            scraped_data = scrape_website(url, keyword)

            # Display the scraped data
            if scraped_data:
                st.write("Scraped Data:")
                for data in scraped_data:
                    st.write(data)
            else:
                st.write("No data found.")

# Run the Streamlit app
if __name__ == '__main__':
    main()

