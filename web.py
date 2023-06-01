import streamlit as st
from bs4 import BeautifulSoup
import requests

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    paragraph = soup.find('p').text
    return title, paragraph

st.title("Data Scraping App")
url = st.text_input("Enter the URL to scrape")

if st.button("Scrape"):
    if url:
        title, paragraph = scrape_data(url)
        st.write(f"Title: {title}")
        st.write(f"Paragraph: {paragraph}")
    else:
        st.warning("Please enter a valid URL.")
