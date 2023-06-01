import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the desired information from the web page
    title = soup.find("h1", id="firstHeading").text.strip()
    paragraphs = soup.find_all("p")

    content = ""
    for paragraph in paragraphs:
        content += paragraph.text.strip() + "\n"

    return title, content

def main():
    st.title("Wikipedia Web Scraper")
    st.write("Scraping data from Wikipedia")

    url = "https://en.wikipedia.org/wiki/Place"

    title, content = scrape_wikipedia(url)

    st.write(f"Title: {title}")
    st.write("Content:")
    st.write(content)

if __name__ == "__main__":
    main()
