from django.urls import path

from main import views
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('info/<int:product_id>/', views.product_info, name='info'),
]
