# 🕹️ Pertemuan 4: Animasi Dasar

## 🔁 1. Apa Itu Game Loop?

Game tidak jalan hanya satu kali. Game terus berputar seperti roda.
🌀 Game Loop artinya:

- Mengecek input pemain
- Mengupdate posisi objek
- Menggambar ulang ke layar

💡 Semua itu terjadi berulang-ulang sangat cepat!

---

## ⏱️ 2. Apa Itu FPS?

FPS = Frames Per Second
Artinya: Berapa kali layar diperbarui setiap detik.
🎯 Contoh:

- 30 FPS = 30 kali per detik
- 60 FPS = 60 kali per detik (lebih halus)

💬 Semakin tinggi FPS, semakin halus gerakannya.
🔧 Di Pygame, kita atur FPS pakai `pygame.time.Clock()`

---

## 🚀 3. Menggerakkan Objek Secara Otomatis

Sekarang kita buat lingkaran merah yang bergerak otomatis dari kiri ke kanan!
🔧 Kode:

```python
import pygame
pygame.init()

# Buat layar
layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Animasi Otomatis")

# Warna dan posisi
PUTIH = (255, 255, 255)
MERAH = (255, 0, 0)
x = 30
y = 200
radius = 30
kecepatan = 3

# Atur FPS
clock = pygame.time.Clock()

jalan = True
while jalan:
    clock.tick(60)  # Set ke 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False

    # Update posisi
    x += kecepatan

    # Gambar ulang
    layar.fill(PUTIH)
    pygame.draw.circle(layar, MERAH, (x, y), radius)
    pygame.display.update()

pygame.quit()
```

🎉 Jalankan dan lihat lingkarannya bergerak otomatis!

---

🧱 4. Menangani Batas Layar

Sekarang kita cegah objek keluar dari layar.

Tambahkan kode ini sebelum menggambar ulang:

```python
if x + radius > 500:   # batas kanan
    kecepatan = -kecepatan
if x - radius < 0:     # batas kiri
    kecepatan = -kecepatan
```

💡 Artinya:

Jika lingkaran menyentuh kanan atau kiri, arah geraknya dibalik.

🎯 Sekarang lingkaran akan memantul bolak-balik!

---

## 📝 Tantangan (PR):

1. Ubah lingkaran jadi persegi
2. Ubah kecepatan menjadi 5
3. Tambahkan batas atas dan bawah juga
4. Buat bola memantul ke segala arah (X dan Y)
