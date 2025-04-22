# 🎨 Pertemuan 2: Menggambar di Layar

## 📍 1. Dasar Koordinat di Pygame

Sebelum menggambar, kita harus paham sistem koordinat di Pygame.

📌 Sistem koordinat:

- `(0, 0)` berada di pojok kiri atas layar.
- Nilai `x` bertambah ke kanan.
- Nilai `y` bertambah ke bawah.

🔍 Contoh:

- `(100, 50)` artinya 100 ke kanan, 50 ke bawah.
- `(200, 300)` artinya 200 ke kanan, 300 ke bawah.

💡 Bayangkan posisi `(400, 200)` di layar. Di mana posisinya? 🤔

---

## 🟢 2. Menggambar Bentuk Sederhana

Sekarang kita akan menggambar **persegi**, **lingkaran**, dan **garis**.

### 🧱 Kode Program

```python
    # Menggambar bentuk
    pygame.draw.rect(layar, MERAH, (50, 50, 100, 100))      # Persegi merah
    pygame.draw.circle(layar, HIJAU, (250, 200), 50)        # Lingkaran hijau
    pygame.draw.line(layar, BIRU, (100, 300), (400, 300), 5) # Garis biru
```

---

## 🧠 Penjelasan Kode

| Baris Kode                                                 | Penjelasan                                                                 |
| ---------------------------------------------------------- | -------------------------------------------------------------------------- |
| `pygame.draw.rect(layar, MERAH, (50, 50, 100, 100))`       | Menggambar persegi merah di koordinat (50, 50) ukuran 100x100.             |
| `pygame.draw.circle(layar, HIJAU, (250, 200), 50)`         | Menggambar lingkaran hijau di titik (250, 200) dengan radius 50.           |
| `pygame.draw.line(layar, BIRU, (100, 300), (400, 300), 5)` | Menggambar garis biru dari (100, 300) ke (400, 300) dengan ketebalan 5 px. |

---

## 🔤 3. Menampilkan Teks di Layar

Tambahkan teks seperti "Halo, Pygame!" ke layar.

```python
# Font teks
font = pygame.font.Font(None, 50)
teks = font.render("Halo, Pygame!", True, MERAH)

# Menampilkan teks di posisi (120, 20)
layar.blit(teks, (120, 20))
```

## 🧠 Penjelasan:

| Baris Kode                                         | Penjelasan                            |
| -------------------------------------------------- | ------------------------------------- |
| `pygame.font.Font(None, 50)`                       | Membuat font ukuran 50 px.            |
| `teks = font.render("Halo, Pygame!", True, MERAH)` | Membuat teks berwarna merah.          |
| `layar.blit(teks, (120, 20))`                      | Menampilkan teks di posisi (120, 50). |

---

## 🧪 Tantangan (PR)

1. 🔺 Gambar segitiga menggunakan 3 garis.
2. 📝 Tampilkan teks "Aku Bisa!" di posisi (200, 150).
3. 🔠 Coba ubah ukuran font menjadi lebih besar atau lebih kecil.
4. 🎨 Gunakan warna favoritmu untuk mempercantik tampilan!
