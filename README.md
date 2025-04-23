# 🌟 Pertemuan 5: Menambahkan Karakter Utama

## 🎭 1. Apa Itu Sprite?

Sprite adalah gambar kecil yang mewakili karakter atau objek dalam game.
Contoh sprite: 🧍‍♂️ Karakter pemain

- 🌳 Pohon
- 🐱 Musuh
- 🎁 Koin

---

## 🖼️ 2. Cara Memuat dan Menampilkan Gambar Sprite

Untuk menampilkan gambar, kita butuh file gambar seperti .png (misalnya ninja.png).
Langkah:

1.  Siapkan gambar ninja.png di folder `assets/sprites`.
2.  Gunakan kode berikut:

    ```python
     import pygame
    pygame.init()

    layar = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Karakter Utama")

    # Warna

    PUTIH = (255, 255, 255)

    # Muat gambar sprite

    karakter = pygame.image.load("astro.png")
    karakter = pygame.transform.scale(karakter, (50, 50)) # Ubah ukuran

    # Posisi awal karakter

    x = 100
    y = 150
    kecepatan = 5

    jalan = True
    while jalan:
    pygame.time.delay(30)

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 jalan = False

         tombol = pygame.key.get_pressed()
         if tombol[pygame.K_LEFT]:
             x -= kecepatan
         if tombol[pygame.K_RIGHT]:
             x += kecepatan
         if tombol[pygame.K_UP]:
             y -= kecepatan
         if tombol[pygame.K_DOWN]:
             y += kecepatan

         layar.fill(PUTIH)
         layar.blit(karakter, (x, y))  # Tampilkan gambar
         pygame.display.update()

    pygame.quit()
    ```

🎉 Jalankan dan lihat karaktermu bisa digerakkan dengan tombol panah!

---

## 🛑 3. Deteksi Tabrakan dengan Batas Layar

Agar karakter tidak keluar dari layar, kita harus membatasi pergerakannya.
Tambahkan kode ini sebelum menggambar:

```python
if x < 0:
    x = 0
if x > 500 - 50:
    x = 500 - 50
if y < 0:
    y = 0
if y > 400 - 50:
    y = 400 - 50
```

📌 Angka 50 di atas adalah ukuran gambar (lebar & tinggi).
🎯 Sekarang karakter tidak bisa lewat batas layar!

---

## 📝 Tantangan (PR):

1. Ubah ukuran sprite jadi 80x80
2. Ubah kecepatan karakter jadi lebih cepat
3. Tambahkan latar belakang berwarna atau bergambar
4. Buat 1 sprite lagi (misalnya musuh) dan tampilkan di layar
