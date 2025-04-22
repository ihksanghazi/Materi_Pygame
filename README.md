## Selamat datang di pertemuan 1!

Halo! 👋  
Pada pertemuan ini, kita akan belajar cara membuat **jendela game pertama** menggunakan **Python dan Pygame**.

## 🔧 Langkah-langkah

Ikuti langkah-langkah di bawah ini untuk membuat jendela game sederhana:

## 💻 Kode Program

```python
import pygame

# Inisialisasi Pygame
pygame.init()

# Buat jendela game
lebar = 500
tinggi = 400
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Game Pertama!")

# Warna latar belakang
warna_latar = (0, 0, 255)  # Biru

# Loop utama game
jalan = True
while jalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False  # Keluar dari game

    layar.fill(warna_latar)  # Mengisi layar dengan warna biru
    pygame.display.update()  # Perbarui tampilan layar

pygame.quit()  # Keluar dari Pygame
```

## 🧠 Penjelasan Kode

| Baris Kode                     | Penjelasan                                                    |
| ------------------------------ | ------------------------------------------------------------- |
| `import pygame`                | Menggunakan pustaka Pygame.                                   |
| `pygame.init()`                | Menyalakan fitur-fitur Pygame.                                |
| `pygame.display.set_mode()`    | Membuat jendela game dengan ukuran tertentu.                  |
| `pygame.display.set_caption()` | Memberi judul pada jendela game.                              |
| `while jalan:`                 | Program akan terus berjalan sampai kita keluar.               |
| `pygame.event.get()`           | Mengecek input dari pengguna (misalnya menutup jendela game). |
| `layar.fill(warna_latar)`      | Mengisi jendela dengan warna latar belakang.                  |
| `pygame.display.update()`      | Memperbarui isi layar agar perubahan bisa terlihat.           |

## 🎉 Coba Jalankan!

Jika kode dijalankan dengan benar, kamu akan melihat:

🟦 Sebuah jendela berwarna biru
📛 Dengan judul: "Game Pertama!"

---

## 📝 Tantangan (PR)

Berikut ini adalah beberapa hal yang perlu kamu ubah di dalam kode:

1. **Ubah warna latar belakang**  
   Ganti warna latar belakang jendela game menjadi **merah** atau **hijau**.

2. **Ganti ukuran jendela**  
   Ubah ukuran jendela game menjadi **600 x 500 piksel**.

3. **Ubah judul jendela**  
   Ganti judul jendela game menjadi:  
   `Game Keren Aku!`

---

## 💡 Tips

- Warna bisa diubah dengan mengganti nilai RGB di fungsi

  ```python
  screen.fill((R, G, B))
  ```

- Ukuran jendela diatur saat memanggil

  ```python
  pygame.display.set_mode((width, height))
  ```

- Judul jendela bisa diatur dengan

  ```python
  pygame.display.set_caption("Judul")
  ```

---

Semangat ngoding dan bersenang-senanglah membuat game kamu makin keren! 😎🔥
