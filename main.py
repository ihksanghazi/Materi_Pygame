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

    # ========================================================
    # Kode Disini Untuk Menggerakan Objek
    # Update posisi
    
    if x + radius > 500:
        kecepatan = -kecepatan
    elif x - radius < 0:
        kecepatan = -kecepatan
    x += kecepatan

    # ========================================================

    # Gambar ulang
    layar.fill(PUTIH)
    pygame.draw.circle(layar, MERAH, (x, y), radius)
    pygame.display.update()

pygame.quit()