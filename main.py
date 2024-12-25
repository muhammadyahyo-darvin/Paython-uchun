import pygame
import sys

pygame.init()

n, a = 800, 600
ekran = pygame.display.set_mode((n, a))
pygame.display.set_caption("Mega O'yin")

oq = (255, 255, 255)
qora = (0, 0, 0)
qizil = (255, 0, 0)
kok = (0, 0, 255)

oyinchi_eni, oyinchi_balandlik = 50, 50
oyinchi_x, oyinchi_y = n // 2, a - 100
tezlik = 5

dushman_eni, dushman_balandlik = 50, 50
dushman_x, dushman_y = n // 3, 0
dushman_tezlik = 3

soat = pygame.time.Clock()
oyin_ishlamoqda = True

while oyin_ishlamoqda:
    for hodisa in pygame.event.get():
        if hodisa.type == pygame.QUIT:
            oyin_ishlamoqda = False

    tugmalar = pygame.key.get_pressed()
    if tugmalar[pygame.K_LEFT] and oyinchi_x > 0:
        oyinchi_x -= tezlik
    if tugmalar[pygame.K_RIGHT] and oyinchi_x < n - oyinchi_eni:
        oyinchi_x += tezlik

    dushman_y += dushman_tezlik
    if dushman_y > a:
        dushman_y = 0
        dushman_x = (pygame.time.get_ticks() // 100) % (n - dushman_eni)

    ekran.fill(oq)
    pygame.draw.rect(ekran, kok, (oyinchi_x, oyinchi_y, oyinchi_eni, oyinchi_balandlik))
    pygame.draw.rect(ekran, qizil, (dushman_x, dushman_y, dushman_eni, dushman_balandlik))

    if (
        oyinchi_x < dushman_x + dushman_eni and
        oyinchi_x + oyinchi_eni > dushman_x and
        oyinchi_y < dushman_y + dushman_balandlik and
        oyinchi_balandlik + oyinchi_y > dushman_y
    ):
        print("O'yin tugadi!")
        oyin_ishlamoqda = False

    pygame.display.flip()
    soat.tick(30)

pygame.quit()
sys.exit()
