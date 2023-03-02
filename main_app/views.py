from django.shortcuts import render

#temporary finch
finch=[
    {'name': 'Bobi', 'color': 'blue', 'age': 5},
    {'name': 'Kino', 'color': 'gray', 'age': 3}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finch/index.html', { 'finch': finch })