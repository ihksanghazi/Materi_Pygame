# 🔄 Pertemuan 3: Event dan Input Pemain

## 🌀 1. Apa Itu Event Loop?

Saat kamu main game, pasti kamu menekan tombol, klik mouse, atau keluar dari game, kan?

📌 Semua itu disebut event (kejadian).
Pygame punya sistem yang memeriksa event itu setiap saat.

🧠 Bayangkan seperti penjaga gerbang yang terus bertanya:
"Ada yang klik? Ada yang tekan tombol? Mau keluar dari game?"

📋 Contoh Event di Pygame:

- Menekan tombol di keyboard
- Menggerakkan mouse
- Menutup jendela game

---

## 🧪 2. Contoh Event Loop di Pygame

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        jalan = False
```

💡 Artinya:
Kalau ada event keluar (klik X), maka game berhenti.

---

## ⌨️ 3. Menangkap Keyboard dan Mouse

Sekarang kita lihat cara menangkap input dari pemain.

```python
import pygame
pygame.init()

# Buat jendela
layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Coba Keyboard & Mouse")

jalan = True
while jalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False

        # Jika tombol ditekan
        if event.type == pygame.KEYDOWN:
            print("Tombol ditekan:", event.key)

        # Jika mouse diklik
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse diklik di:", event.pos)

pygame.quit()
```

🧪 Coba Jalankan!
Lihat di terminal/console. Setiap tekan tombol atau klik mouse, akan keluar tulisan!

---

## 🕹️ 4. Menggerakkan Objek dengan Tombol Panah

Sekarang kita buat kotak yang bisa digerakkan dengan arrow keys (↑ ↓ ← →)

🔧 Kode Program:

```python
import pygame
pygame.init()

layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Gerakkan Kotak!")

# Warna dan posisi
PUTIH = (255, 255, 255)
MERAH = (255, 0, 0)
x = 200
y = 150
lebar = 50
tinggi = 50
kecepatan = 5

jalan = True
while jalan:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False

    # Cek tombol yang ditekan
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT]:
        x -= kecepatan
    if tombol[pygame.K_RIGHT]:
        x += kecepatan
    if tombol[pygame.K_UP]:
        y -= kecepatan
    if tombol[pygame.K_DOWN]:
        y += kecepatan

    # Gambar ulang
    layar.fill(PUTIH)
    pygame.draw.rect(layar, MERAH, (x, y, lebar, tinggi))
    pygame.display.update()

pygame.quit()
```

🎯 Penjelasan:

- `pygame.key.get_pressed()` → Mengecek tombol apa yang ditekan
- `K_LEFT, K_RIGHT, dst` → Tombol panah
- `x, y` → Posisi kotak
- `x += kecepatan` → Gerak ke kanan

🎉 Jalankan dan coba tekan panah! Kotak akan bergerak 🚀

---

## 📝 Tantangan (PR):

1. Ubah kecepatan kotak menjadi 10
2. Ubah bentuknya jadi lingkaran
3. Tambahkan batas agar kotak tidak keluar layar
