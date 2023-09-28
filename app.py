import requests
from bs4 import BeautifulSoup

def scrape_paragraphs(url):
    # Send a request to the URL and get the HTML content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Unable to retrieve content from {url}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <p> tags
    paragraphs = soup.find_all(['p', 'li'])

    # Extract the text content from the <p> tags
    paragraph_texts = [p.get_text() for p in paragraphs]

    return paragraph_texts

# Replace 'http://example.com' with the actual URL you want to scrape
url_to_scrape = 'https://www.designgurus.io/blog/system-design-interview-fundamentals'

paragraphs = scrape_paragraphs(url_to_scrape)

# Print the paragraphs
for i, paragraph in enumerate(paragraphs):
    print(f"Paragraph {i+1}:")
    print(paragraph)
    print("\n")
