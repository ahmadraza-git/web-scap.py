import requests
from bs4 import BeautifulSoup
import streamlit as st

# Fetch the HTML content of the page
def fetch_page_content(url):
    response = requests.get(url)
    return response.text

# Extract relevant information from the HTML
def extract_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Modify the code below based on the specific information you want to extract
    # For example, let's extract the page title and the first paragraph
    title = soup.find('h1', {'id': 'firstHeading'}).text
    first_paragraph = soup.find('p').text
    return title, first_paragraph

# Main function to run the web scraper
def main():
    st.title("Web Scraper")
    url = "https://simple.wikipedia.org/wiki/Muhammad_Iqbal"

    # Fetch the page content
    html_content = fetch_page_content(url)

    # Extract relevant information
    title, first_paragraph = extract_info(html_content)

    # Display the information using Streamlit
    st.header(title)
    st.write(first_paragraph)

if __name__ == '__main__':
    main()
