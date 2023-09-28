import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

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
#
# paragraphs = scrape_paragraphs(url_to_scrape)
#
# # Print the paragraphs
# for i, paragraph in enumerate(paragraphs):
#     print(f"Paragraph {i+1}:")
#     print(paragraph)
#     print("\n")


def generate_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for i, text in enumerate(content):
        try:
            # Try encoding with utf-8, fall back to latin1 if it fails
            pdf.multi_cell(0, 10, f"Content {i+1}:\n{text.encode('utf-8').decode('latin1')}\n")
        except UnicodeEncodeError:
            pdf.multi_cell(0, 10, f"Content {i+1}:\n{text.encode('latin1', errors='replace').decode('latin1')}\n")

    return pdf



url_to_scrape = 'https://www.designgurus.io/blog/system-design-interview-fundamentals'
content = scrape_paragraphs(url_to_scrape)

pdf = generate_pdf(content)

pdf.output("combined_content.pdf")
