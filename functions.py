import requests
from bs4 import BeautifulSoup

def get_og_image(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    og_image = soup.find("meta", property="og:image")
    if og_image:
        return og_image["content"]
    return None
