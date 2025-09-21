from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, "my_app/home.html", {"items": items})
