#entry/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from . import models 

class EntryListView(ListView):
    model = models.Entry
    template_name = 'entry_list.html'

class EntryDetailView(DetailView):
    model = models.Entry
    template_name = 'entry_detail.html'

class EntryUpdateView(UpdateView):
    model = models.Entry
    fields = ['title', 'body', ]
    template_name = 'entry_edit.html'
    
class EntryDeleteView(DeleteView):
    model = models.Entry
    template_name = 'entry_delete.html'
    success_url = reverse_lazy('entry_list')
    
class EntryCreateView(CreateView):
    model = models.Entry
    template_name = 'entry_create.html'
    fields = ['title', 'body', 'author', ]