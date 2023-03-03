from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finch/detail.html', { 'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'