from camper import views
from app_login import appLoginViews
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.productList, name='productList'),
    path('board/', views.board, name='board'),
    
    #app_login
    path('signUpPage/', appLoginViews.signUpPage , name='signUpPage'),
    path('loginPage/', appLoginViews.loginPage , name='loginPage')
]