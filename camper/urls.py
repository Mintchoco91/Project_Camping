from camper import views
from app_login import appLogin_views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('reviewBoard/', views.reviewBoard, name='reviewBoard'),
    
    #app_login
    path('signUpPage/', appLogin_views.signUpPage , name='signUpPage'),
    path('signUp/', appLogin_views.signUp , name='signUp'),
    path('loginPage/', appLogin_views.loginPage , name='loginPage'),
    path('login/', appLogin_views.login , name='login'),
    path('logout/', appLogin_views.logout , name='logout'),
    
    #product
    path('product/<str:category>/', views.productList, name='productList'),
    path('product/<str:category>/<int:no>', views.productDetail, name='productDetail'),
    
    #cart
    path('cart/addItem', views.addItemToCart, name='addItemToCart'),
    path('cart/', views.myCart, name='myCart'),

]