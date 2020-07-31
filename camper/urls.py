from camper import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.productList, name='productList'),
    path('board/', views.board, name='board')
]