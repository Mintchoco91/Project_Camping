from camper import views
from app_login import appLogin_views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('board/', views.board, name='board'),
    
    #app_login
    path('signUpPage/', appLogin_views.signUpPage , name='signUpPage'),
    path('signUp/', appLogin_views.signUp , name='signUp'),
    path('loginPage/', appLogin_views.loginPage , name='loginPage'),
    path('login/', appLogin_views.login , name='login')
]