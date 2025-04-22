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
        print(event.type)
        if event.type == pygame.QUIT:
            jalan = False  # Keluar dari game
            
    layar.fill(warna_latar)  # Mengisi layar dengan warna biru
    pygame.display.update()  # Perbarui tampilan layar

pygame.quit()  # Keluar dari Pygame