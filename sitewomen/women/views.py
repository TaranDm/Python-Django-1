from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the wo men index page.")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Categories</h1><p>id: {cat_id}</p>")  # Вставка для запроса страницы HTML
