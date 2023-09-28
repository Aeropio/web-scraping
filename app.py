import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from urllib.parse import urlparse
from play_audio import play_audio, text_to_audio


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
    # Extract the text content from the tags
    paragraph_texts = [p.get_text() for p in paragraphs]
    return paragraph_texts


def extract_domain_name(url):
    # Parse the URL
    parsed_url = urlparse(url)
    # Extract the domain name
    domain_name = parsed_url.netloc.split('.')[1]
    return domain_name


def generate_pdf(url_to_scrape, file_name):
    content = scrape_paragraphs(url_to_scrape)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for i, text in enumerate(content):
        try:
            # Try encoding with utf-8, fall back to latin1 if it fails
            pdf.multi_cell(0, 10, f"Content {i+1}:\n{text.encode('utf-8').decode('latin1')}\n")
        except UnicodeEncodeError:
            pdf.multi_cell(0, 10, f"Content {i+1}:\n{text.encode('latin1', errors='replace').decode('latin1')}\n")

    #return pdf
    pdf_file_path = f'{file_name}.pdf'
    pdf.output(pdf_file_path)
    #print(pdf_file_path)
    return pdf_file_path



url_to_scrape = 'https://www.designgurus.io/blog/system-design-interview-fundamentals'
file_name = extract_domain_name(url_to_scrape)
text_to_audio(generate_pdf(url_to_scrape, file_name))


