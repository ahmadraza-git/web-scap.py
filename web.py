import requests
from bs4 import BeautifulSoup
import streamlit as st


app = Flask(__name__)

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    paragraph = soup.find('p').text
    return title, paragraph

@app.route('/', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            title, paragraph = scrape_data(url)
            return render_template('result.html', title=title, paragraph=paragraph)
        else:
            return "Please enter a valid URL."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
