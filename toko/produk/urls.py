from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('produk/', views.daftar_produk, name='daftar_produk'),
    path('produk/<int:produk_id>/', views.detail_produk, name='detail_produk'),
    path('kontak/', views.kontak, name='kontak'),
    path('stok/', views.stok_produk, name='stok_produk'),
]
