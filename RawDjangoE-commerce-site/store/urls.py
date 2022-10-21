
from django.urls import path
from .views import home, index, product_details

from shop import settings
urlpatterns = [
    path('', home, name="home"),
    path('index', index, name='index'),
    path('products/<str:slug>/', product_details, name='products' ),
]