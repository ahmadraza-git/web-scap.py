import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to scrape data from Wikipedia
def scrape_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the desired information from the page
    title = soup.find('h1', {'id': 'firstHeading'}).text
    paragraphs = soup.find_all('p')
    content = '\n\n'.join(p.text for p in paragraphs)
    
    return title, content

# Streamlit web application
def main():
    st.title("Wikipedia Web Scraper")
    url = st.text_input("Enter Wikipedia URL")
    
    if st.button("Scrape"):
        if url:
            try:
                title, content = scrape_wikipedia(url)
                st.subheader(title)
                st.markdown(content)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a valid URL.")

if __name__ == '__main__':
    main()
