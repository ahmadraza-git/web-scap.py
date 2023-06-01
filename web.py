import streamlit as st
from bs4 import BeautifulSoup
import requests
import scrapy

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [
        "https://www.example.com/news",
    ]

    def parse(self, response):
        # Extract information from the HTML response
        articles = response.css("div.article")

        for article in articles:
            title = article.css("h2::text").get().strip()
            link = article.css("a::attr(href)").get()

            yield {
                "title": title,
                "link": link,
            }

        # Follow pagination links
        next_page = response.css("a.next-page::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# Run the spider
process = scrapy.crawler.CrawlerProcess()
process.crawl(NewsSpider)
process.start()
