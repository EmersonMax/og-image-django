# og-image-django
Como capturar a tag og:image utilizando o django 

#instale a biblioteca BeautifulSoup

pip install requests beautifulsoup4

#crie um arquivo no diretorio do seu projeto neste caso criei arquivo chamado functions.py

#defina a função apra extrair a tag og:image

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

    na sua view import o função criar e segue um exemplo de como passar para o template

    def my_view(request):
    url = "url/" # substitua pela URL que deseja
    image_url = get_og_image(url)
    return render(request, 'my_template.html', {'image_url': image_url})
