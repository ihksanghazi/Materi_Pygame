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