from camper import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('board/', views.board, name='board')
]