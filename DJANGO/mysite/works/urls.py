from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:lavoro_id>/', views.lavori, name='lavori'),
    path('<int:lavoro_id>/', views.categorie, name='categorie'),
]
