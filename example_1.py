import pygame
pygame.init()

# Buat jendela
layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Coba Keyboard & Mouse")

jalan = True
while jalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False

        # Jika tombol ditekan
        if event.type == pygame.KEYDOWN:
            print("Tombol ditekan:", event.key)

        # Jika mouse diklik
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse diklik di:", event.pos)

pygame.quit()