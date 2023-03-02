from django.shortcuts import render
from .models import Finch

# temporary finch
# finch=[
#     {'name': 'Bilu', 'color': 'blue', 'age': 5},
#     {'name': 'Kino', 'color': 'gray', 'age': 3}
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finch= Finch.objects.all()
    return render(request, 'finch/index.html', { 'finch': finch })