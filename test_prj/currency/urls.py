from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('table/', views.currency, name='currency'),
    path('table/download_pdf', views.to_pdf, name='download_pdf')
]
