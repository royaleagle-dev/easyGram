from django.urls import path
from . import views

app_name = 'phonebook'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('trash/', views.TrashView.as_view(), name = 'trash'),
    path('log/', views.LogView.as_view(), name = 'log' ),
    path('delete/', views.DeleteView.as_view(), name = "delete"),
]