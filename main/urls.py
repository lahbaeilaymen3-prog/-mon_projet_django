from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livraison/<int:id>/', views.detail_livraison, name='detail_livraison'),
]
