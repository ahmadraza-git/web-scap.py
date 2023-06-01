import streamlit as st
import pandas as pd
# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import streamlit as st

# Define the web scraping function
def scrape_website(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape the desired data from the website
    # Modify this section according to your specific requirements
    title = soup.find('h1').text
    description = soup.find('p').text

    # Return the scraped data
    return title, description

# Create a Streamlit app
def main():
    # Set the title of the app
    st.title("Web Scraping App")

    # Get the user input URL
    url = st.text_input("Enter the URL of the website to scrape:")

    # Check if the user has entered a URL
    if url:
        # Call the web scraping function
        title, description = scrape_website(url)

        # Display the scraped data
        st.write("Title:", title)
        st.write("Description:", description)

# Run the Streamlit app
if __name__ == '__main__':
    main()

