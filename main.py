import pygame
pygame.init()

layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Karakter Utama")

# Warna
PUTIH = (255, 255, 255)

# Muat gambar sprite
karakter = pygame.image.load("assets/sprites/ninja.png")
karakter = pygame.transform.scale(karakter, (50, 50))  # Ubah ukuran

# Posisi awal karakter
x = 100
y = 150
kecepatan = 5

# ==================================================
## Kode disini untuk memuat suara latar dan efek suara

pygame.mixer.music.load("assets/sounds/latar.mp3")
pygame.mixer.music.play(-1)  # -1 artinya putar terus-menerus
langkah_channel = pygame.mixer.Channel(0) # Buat channel untuk efek suara
langkah = pygame.mixer.Sound("assets/sounds/langkah.mp3") # Muat efek suara langkah

# ==================================================

jalan = True
while jalan:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False

    if x < 0:
        x = 0
    if x > 500 - 50:
        x = 500 - 50
    if y < 0:
        y = 0
    if y > 400 - 50:
        y = 400 - 50

    # ==================================================
    # tambahkan langkah.play() di dalam if agar suara langkah hanya terdengar saat bergerak
    bergerak = False
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT]:
        x -= kecepatan
        bergerak =True
    if tombol[pygame.K_RIGHT]:
        x += kecepatan
        bergerak =True
    if tombol[pygame.K_UP]:
        y -= kecepatan
        bergerak =True
    if tombol[pygame.K_DOWN]:
        y += kecepatan
        bergerak =True

    if bergerak and not langkah_channel.get_busy(): # Jika tidak ada suara yang sedang diputar
        langkah_channel.play(langkah)

    # ==================================================

    layar.fill(PUTIH)
    layar.blit(karakter, (x, y))  # Tampilkan gambar
    pygame.display.update()

pygame.quit()
