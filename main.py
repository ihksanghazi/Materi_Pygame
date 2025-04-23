import pygame
pygame.init()

layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Karakter Utama")

# Warna
PUTIH = (255, 255, 255)

# ==================================================
# Kode disini untuk memuat gambar sprite
# Muat gambar sprite
karakter = pygame.image.load("assets/sprites/ninja.png")
karakter = pygame.transform.scale(karakter, (50, 50))  # Ubah ukuran

# ==================================================

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

    # ==================================================
    # Kode disini untuk mengatur batas gerakan karakter
    if x < 0:
        x = 0
    if x > 500 - 50:
        x = 500 - 50
    if y < 0:
        y = 0
    if y > 400 - 50:
        y = 400 - 50
    # ==================================================

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
    # ==================================================
    # Kode disini untuk menampilkan gambar sprite

    layar.blit(karakter, (x, y))  # Tampilkan gambar

    # ==================================================
    pygame.display.update()

pygame.quit()
