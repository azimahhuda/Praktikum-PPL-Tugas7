from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("""
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-family: Arial, sans-serif;
                }
                a {
                    margin: 10px;
                    text-decoration: none;
                    color: white;
                    background-color: #D39F3F;
                    padding: 15px 25px;
                    border-radius: 5px;
                    font-size: 16px;
                    display: inline-block;
                    transition: background-color 0.3s;
                }
                a:hover {
                    background-color: #9E6B0D;
                }
            </style>
        </head>
        <body>
            <h1>🥐 Selamat Datang di Toko Roti Riori 🥐</h1>
            <p>Temukan berbagai roti terbaik kesukaan Anda.</p>
            <div>
                <a href="/produk/">Lihat Produk</a> 
                <a href="/kontak/">Hubungi Kami</a> 
                <a href="/stok/">Lihat Stok</a>
            </div>
        </body>
        </html>
    """)


def daftar_produk(request):
    return HttpResponse("""
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-family: Arial, sans-serif;
                }
                .produk-container {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    flex-wrap: wrap;
                    margin-top: 20px;
                }
                .produk {
                    width: 150px;
                    padding: 20px;
                    text-align: center;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s;
                }
                .produk:hover {
                    transform: scale(1.05);
                }
                .produk .box {
                    background-color: #f0f0f0;
                    padding: 10px;
                    margin-bottom: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                .produk a {
                    margin-top: 10px;
                    text-decoration: none;
                    color: white;
                    background-color: #D39F3F;
                    padding: 10px 20px;
                    border-radius: 5px;
                    display: inline-block;
                    font-size: 14px;
                    transition: background-color 0.3s;
                }
                .produk a:hover {
                    background-color: #9E6B0D;
                }
                .kembali-homepage a {
                    margin-top: 20px;
                    text-decoration: none;
                    color: white;
                    background-color: #D39F3F;
                    padding: 15px 25px;
                    border-radius: 5px;
                    font-size: 16px;
                    display: inline-block;
                    transition: background-color 0.3s;
                }
                .kembali-homepage a:hover {
                    background-color: #9E6B0D;
                }
            </style>
        </head>
        <body>
            <h1>Daftar Produk Kami</h1>
            <div class="produk-container">
                <div class="produk">
                    <div class="box">1. Croissant</div>
                    <a href="/produk/1/">Lihat</a>
                </div>
                <div class="produk">
                    <div class="box">2. Scone</div>
                    <a href="/produk/2/">Lihat</a>
                </div>
                <div class="produk">
                    <div class="box">3. Panettone</div>
                    <a href="/produk/3/">Lihat</a>
                </div>
            </div>
            <div class="kembali-homepage">
                <a href="/">Kembali ke Homepage</a>
            </div>
        </body>
        </html>
    """)


def detail_produk(request, produk_id):
    return HttpResponse(f"""
        <html>
        <head>
            <style>
                body {{
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-family: Arial, sans-serif;
                }}
                a {{
                    margin: 10px;
                    text-decoration: none;
                    color: white;
                    background-color: #D39F3F;
                    padding: 15px 25px;
                    border-radius: 5px;
                    font-size: 16px;
                    display: inline-block;
                    transition: background-color 0.3s;
                }}
                a:hover {{
                    background-color: #9E6B0D;
                }}
            </style>
        </head>
        <body>
            <h1>Detail Produk</h1>
            <p>Anda sedang melihat detail produk dengan ID: {produk_id}.</p>
            <a href="/produk/">Kembali</a>
        </body>
        </html>
    """)


def kontak(request):
    return HttpResponse("""
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-family: Arial, sans-serif;
                }
                a {
                    margin: 10px;
                    text-decoration: none;
                    color: white;
                    background-color: #D39F3F;
                    padding: 15px 25px;
                    border-radius: 5px;
                    font-size: 16px;
                    display: inline-block;
                    transition: background-color 0.3s;
                }
                a:hover {
                    background-color: #9E6B0D;
                }
            </style>
        </head>
        <body>
            <h1>Kontak Kami</h1>
            <p>Hubungi kami melalui email: <strong>kontak@tokokami.com</strong> atau telepon: <strong>0812-3456-7890</strong>.</p>
            <a href="/">Kembali ke Homepage</a>
        </body>
        </html>
    """)


def stok_produk(request):
    return HttpResponse("""
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-family: Arial, sans-serif;
                }
                .produk-container {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin: 20px 0;
                }
                .produk-item {
                    border: 2px solid #4CAF50;
                    padding: 20px;
                    border-radius: 10px;
                    width: 200px;
                }
                a {
                    margin: 10px;
                    text-decoration: none;
                    color: white;
                    background-color: #D39F3F;
                    padding: 15px 25px;
                    border-radius: 5px;
                    font-size: 16px;
                    display: inline-block;
                    transition: background-color 0.3s;
                }
                a:hover {
                    background-color: #9E6B0D;
                }
            </style>
        </head>
        <body>
            <h1>Stok Produk</h1>
            <div class="produk-container">
                <div class="produk-item">
                    <p>Produk 1</p>
                    <p>Stok: 20</p>
                </div>
                <div class="produk-item">
                    <p>Produk 2</p>
                    <p>Stok: 15</p>
                </div>
                <div class="produk-item">
                    <p>Produk 3</p>
                    <p>Stok: 8</p>
                </div>
            </div>
            <a href="/">Kembali ke Homepage</a>
        </body>
        </html>
    """)

