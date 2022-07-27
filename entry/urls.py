#entry/urls.py
from django.urls import path 

from . import views

urlpatterns =[
    path('', views.EntryListView.as_view(), name='entry_list'),
    path('<int:pk>/edit/',
         views.EntryUpdateView.as_view(), name='entry_edit'),
    path('<int:pk>/',
         views.EntryDetailView.as_view(), name='entry_detail'),
    path('<int:pk>/delete/',
         views.EntryDeleteView.as_view(), name='entry_delete'),
    path('create/', views.EntryCreateView.as_view(), name="entry_create")
]