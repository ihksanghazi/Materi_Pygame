# 🌟 🎶 Pertemuan 6: Efek Suara dan Musik

## 🔊 1. Mengapa Game Perlu Suara?

🎮 Pernah main game tanpa suara?
Pasti terasa sepi dan kurang seru, kan?

🧠 Efek suara dan musik membuat game terasa hidup dan menyenangkan!

---

## 🎵 2. Format File Suara

Agar bisa diputar di Pygame, file suara sebaiknya berformat:

- `.wav` → untuk efek suara (lebih ringan dan cepat)
- `.mp3` → untuk background music

---

## 3. Cara Memuat dan Memainkan Efek Suara

🎧 Contoh Suara: `lompat.wav`
Letakkan file `lompat.wav` di folder `assets/sounds`.
🧪 Contoh Kode:

```python
import pygame
pygame.init()

# Muat suara efek
efek_lompat = pygame.mixer.Sound("assets/sounds/lompat.wav")

# Mainkan suara efek
efek_lompat.play()
```

📌 Suara akan diputar 1 kali saat play() dipanggil.

---

## 🎼 4. Memutar Musik Latar (Background Music)

Contoh Musik: musik.mp3
🎶 Kode:

```python
pygame.mixer.music.load("assets/sounds/musik.mp3")
pygame.mixer.music.play(-1)  # -1 artinya putar terus-menerus

```

📌 Musik akan terus diputar selama game berjalan.

---

## 🕹️ 5. Tambahkan Suara Saat Karakter Bergerak

Kita bisa gabungkan suara ke dalam gerakan karakter. Contohnya:

```python
import pygame
pygame.init()

layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Suara Gerak")

# Muat suara
langkah = pygame.mixer.Sound("langkah.wav")

x = 200
y = 200
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
        langkah.play()
    elif tombol[pygame.K_RIGHT]:
        x += kecepatan
        langkah.play()

    layar.fill((255, 255, 255))
    pygame.draw.rect(layar, (0, 0, 255), (x, y, 50, 50))
    pygame.display.update()

pygame.quit()
```

🎧 Setiap kali karakter digerakkan ke kiri atau kanan, suara langkah.wav akan terdengar.

💡 Tips: Gunakan suara yang pendek untuk efek (0.5 - 2 detik).

---

## 📝 Tantangan (PR):

1. Cari atau buat efek suara sendiri untuk: lompat, tabrakan, dan menang
2. Tambahkan suara saat karakter menabrak dinding
3. Ubah musik latar dengan lagu favorit kamu (yang tenang atau seru)
4. Tambahkan tombol M untuk mematikan/menghidupkan musik 🎵
