import requests
import BeautifulSoup
import streamlit as st

def scrape_car_info():
    url = "https://en.wikipedia.org/wiki/Car"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Scrape relevant information
    car_name = soup.find("h1", id="firstHeading").text
    car_summary = soup.find("div", class_="mw-parser-output").p.text

    return car_name, car_summary

def main():
    st.title("Car Information Scraper")
    st.write("Scraping data from https://en.wikipedia.org/wiki/Car")

    car_name, car_summary = scrape_car_info()

    st.write(f"Car Name: {car_name}")
    st.write("Summary:")
    st.write(car_summary)

if __name__ == "__main__":
    main()
