import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_websites():
    url = "https://www.octoparse.com/blog/top-10-most-scraped-websites"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    website_list = []
    websites = soup.find_all("h3", class_="post-title")
    
    for website in websites:
        website_list.append(website.text.strip())

    return website_list

def main():
    st.title("Top 10 Most Scraped Websites")
    st.write("Scraping data from https://www.octoparse.com/blog/top-10-most-scraped-websites")

    websites = scrape_websites()

    if websites:
        st.write("Here are the top 10 most scraped websites:")
        for i, website in enumerate(websites, start=1):
            st.write(f"{i}. {website}")
    else:
        st.write("Failed to retrieve website data.")

if __name__ == "__main__":
    main()
