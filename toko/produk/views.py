from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homepage(request):
    return HttpResponse("""
        <h1>Selamat Datang di Toko Kami</h1>
        <p>Temukan berbagai produk terbaik untuk kebutuhan Anda.</p>
        <a href="/produk/">Lihat Produk</a> | <a href="/kontak/">Hubungi Kami</a> | <a href="/stok">Lihat Stok</a>
    """)
