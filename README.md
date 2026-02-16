Sebagai peneliti dan auditor sistem, saya telah menyusun dokumentasi repositori Anda agar memiliki standar profesional yang setara dengan contoh "iPusnas Downloader CLI" yang Anda berikan.

Berikut adalah draf final untuk file `README.md` Anda. Pastikan untuk menyimpan ini di root direktori proyek Anda.

---

# 🖐️ 3D Pro Presentation - Gesture Control

Sistem presentasi berbasis web yang memanfaatkan teknologi **Computer Vision** untuk kontrol navigasi nirsentuh melalui gestur tangan secara real-time.

## ## Features

* **🖼️ 3D Immersive Carousel**: Visualisasi slide interaktif dengan efek *depth* dan *dynamic blur* menggunakan Three.js.
* **🖐️ Hand Gesture Navigation**: Kontrol penuh (Next, Prev, Zoom) hanya dengan menggerakkan tangan di depan kamera.
* **🔒 Secure Lock System**: Fitur pengunci sensor menggunakan gestur khusus (Peace/Rock sign) untuk mencegah input tidak sengaja.
* **🔍 Smart Zoom 65%**: Fitur fokus otomatis yang dihitung secara matematis berdasarkan FOV kamera untuk pembacaan konten yang optimal.
* **⚙️ Dynamic Backend**: Integrasi Flask untuk pemindaian otomatis direktori gambar (`JPG/PNG`) secara dinamis.

## ## Prerequisites

* **Python 3.10+**: Diperlukan untuk menjalankan server backend Flask.
* **Modern Web Browser**: Disarankan Google Chrome atau Microsoft Edge untuk akselerasi hardware MediaPipe.
* **Webcam**: Kamera fungsional untuk deteksi gestur.

## ## Installation

1. Clone the repository:
```bash
git clone https://github.com/username/3d-gesture-presentation.git
cd 3d-gesture-presentation

```


2. Install dependencies:
```bash
pip install -r requirements.txt

```


3. Setup folder:
* Pastikan gambar presentasi Anda berada di direktori `D:\1\PYTHON\input` (atau sesuaikan di `Input.py`).



## ## Usage

Anda dapat menjalankan server backend melalui CMD untuk mengaktifkan antarmuka web.

### 1. Start Server

```bash
python assets/Input.py

```

*Aplikasi akan berjalan di `http://127.0.0.1:5000*`

### 2. Gesture Controls

| Action | Gesture | Deskripsi |
| --- | --- | --- |
| **LOCK** | ✌️ Peace Sign | Menonaktifkan semua kontrol sensor |
| **UNLOCK** | 🤘 Rock Sign | Mengaktifkan kembali kontrol sensor |
| **NEXT** | 👉 Tangan Kanan | Berpindah ke slide berikutnya |
| **PREV** | 👈 Tangan Kiri | Berpindah ke slide sebelumnya |
| **ZOOM** | ☝️ Atas | Zoom masuk sebesar 65% |
| **RESET** | 👇 Bawah | Mengembalikan posisi kamera awal |

## ## Configuration

### Custom Image Path

Jika Anda ingin mengubah lokasi folder gambar, edit variabel berikut di `Input.py`:

```python
IMAGE_DIR = r"D:\your\custom\path"

```

### Virtual Environment (Optional)

Untuk menjaga kebersihan sistem, disarankan menggunakan `venv`:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

```

## ## Disclaimer

Alat ini dikembangkan untuk tujuan **edukasi dan riset** mengenai interaksi manusia dan komputer (HCI). Pengembang tidak bertanggung jawab atas penyalahgunaan alat ini dalam lingkungan produksi tanpa pengawasan.

---

### Langkah Selanjutnya:

1. Simpan teks di atas ke dalam file bernama **`README.md`**.
2. Pastikan file **`requirements.txt`** sudah berisi `Flask` dan `Flask-CORS`.
3. Gunakan perintah `git push` seperti yang kita bahas sebelumnya untuk mengunggah semuanya ke GitHub.

Apakah ada bagian fitur spesifik lagi yang ingin Anda tambahkan ke dalam dokumentasi ini?
