#entry/views.py
from django.views.generic import ListView

from . import models 

class EntryListView(ListView):
    model = models.Entry
    template_name = 'entry_list.html'