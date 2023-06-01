import streamlit as st


import requests
from bs4 import BeautifulSoup

def scrape_products():
    # Send a GET request to the website
    url = "https://www.example.com/products"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the HTML elements containing the products
        products = soup.find_all("div", class_="product")
        
        # Extract the title and price for each product
        for product in products:
            title = product.find("h2").text.strip()
            price = product.find("span", class_="price").text.strip()
            
            print("Title:", title)
            print("Price:", price)
            print("------")
    else:
        print("Failed to retrieve products.")

# Call the function to start scraping
scrape_products()
