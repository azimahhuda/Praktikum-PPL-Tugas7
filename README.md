# Toko — Django Project Sederhana

Ini adalah proyek Django sederhana yang menampilkan:
- **Homepage** (``)
- **Daftar Produk** (`/produk/`)
- **Detail Produk** (`produk/<int:produk_id>/`)
- **Kontak** (`/kontak/`)
- **Stok Produk** (`/stok/`)

Semua halaman menggunakan **Function-Based View (FBV)** dan menampilkan konten sederhana langsung melalui **HttpResponse**, tanpa menggunakan template rendering.

## Cara Menjalankan Program

1. **Aktifkan virtual environment**:
   
   Sesuaikan dengan sistem operasi masing-masing.
   ```bash
   # Windows
   env\Scripts\activate

   # macOS/Linux
   source env/bin/activate
   ```

2. **Install dependencies**:

   Jika belum ada Django, install dulu:
   ```bash
   pip install django
   ```

3. **Jalankan server**:

   ```bash
   python manage.py runserver
   ```

4. **Akses project di browser**:

   Buka `http://127.0.0.1:8000/`

---

## Catatan Penting

- Pastikan environment (`env`) sudah disesuaikan dengan konfigurasi dan kebutuhan device masing-masing.
- Gunakan minimal **Python 3.7** ke atas untuk kompatibilitas terbaik.
