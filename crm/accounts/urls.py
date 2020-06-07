from django.urls import path
from . import views             #relative import

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]
