from django.shortcuts import render
from .functions import get_og_image

def my_view(request):
    url = "url" # substitua pela URL que deseja
    image_url = get_og_image(url)
    return render(request, 'my_template.html', {'image_url': image_url})
