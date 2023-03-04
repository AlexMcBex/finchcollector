from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Nest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RibbonForm

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
    id_list = finch.nests.all().values_list('id')
    nests_finch_hasnt_been = Nest.objects.exclude(id__in=id_list)
    ribbon_form = RibbonForm()
    return render(request, 'finch/detail.html', { 'finch': finch , 'ribbon_form': ribbon_form, 'nests': nests_finch_hasnt_been})


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields =['color', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_ribbon(request, finch_id):
    form = RibbonForm(request.POST)
    if form.is_valid():
        new_ribbon = form.save(commit=False)
        new_ribbon.finch_id = finch_id
        new_ribbon.save()
    return redirect('detail', finch_id=finch_id)

def assoc_nest(request, finch_id, nest_id):
    Finch.objects.get(id=finch_id).nests.add(nest_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_nest(request, finch_id, nest_id):
    Finch.objects.get(id=finch_id).nests.remove(nest_id)
    return redirect('detail', finch_id=finch_id)

class NestList(ListView):
    model = Nest
    template_name = 'nests/index.html'

class NestDetail(DetailView):
    model = Nest
    template_name = 'nests/detail.html'

class NestCreate(CreateView):
    model = Nest
    fields = ['city', 'location']

    def form_valid(self, form):
        return super().form_valid(form)
    
class NestUpdate(UpdateView):
    model = Nest
    fields = ['city', 'location']

class NestDelete(DeleteView):
    model = Nest
    success_url = '/nests/'

