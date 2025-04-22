import pygame  

# Inisialisasi Pygame
pygame.init()  

# Buat layar
lebar = 500
tinggi = 400
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Menggambar di Pygame")

# Warna
PUTIH = (255, 255, 255)
MERAH = (255, 0, 0)
HIJAU = (0, 255, 0)
BIRU = (0, 0, 255)

# Loop utama
jalan = True
while jalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False  

    layar.fill(PUTIH)  # Latar belakang putih

    # ========================================================
    # Kode Disini Untuk Menggambar Bentuk dan Menampilkan Teks

    # Menggambar bentuk
    pygame.draw.rect(layar, MERAH, (50, 50, 100, 100))      # Persegi merah
    pygame.draw.circle(layar, HIJAU, (250, 200), 50)        # Lingkaran hijau
    pygame.draw.line(layar, BIRU, (100, 300), (400, 300), 5) # Garis biru

    # Font teks
    font = pygame.font.Font(None, 50)
    teks = font.render("Halo, Pygame!", True, MERAH)

    # Menampilkan teks di posisi (120, 20)
    layar.blit(teks, (120, 20))

    # ========================================================

    pygame.display.update()  # Perbarui layar

pygame.quit()
