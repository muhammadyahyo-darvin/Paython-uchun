import pygame
import sys

# Pygame kutubxonasini ishga tushuramiz
pygame.init()

# Ekran o'lchamlari
n, a = 800, 600
ekran = pygame.display.set_mode((n, a))
pygame.display.set_caption("Mashina Haydash O'yini")

# Ranglar
oq = (255, 255, 255)
qora = (0, 0, 0)
qizil = (255, 0, 0)
yashil = (0, 255, 0)

# Mashina parametrlari
mashina_width = 60
mashina_height = 120
mashina_x = n // 2 - mashina_width // 2
mashina_y = a - mashina_height - 10
tezlik = 10

# Yig'ishlar va darajalar
yigish = 0

# O'yin holati
soat = pygame.time.Clock()
oyin_ishlamoqda = True

while oyin_ishlamoqda:
    for hodisa in pygame.event.get():
        if hodisa.type == pygame.QUIT:
            oyin_ishlamoqda = False

    tugmalar = pygame.key.get_pressed()

    # Chap va o'ngga harakatlanish
    if tugmalar[pygame.K_LEFT] and mashina_x > 0:
        mashina_x -= tezlik
    if tugmalar[pygame.K_RIGHT] and mashina_x < n - mashina_width:
        mashina_x += tezlik

    # Ekranni tozalash va yangi rasm chizish
    ekran.fill(qora)  # Ekranni to'liq qora bilan to'ldirish

    # Mashina rasmni chizish
    pygame.draw.rect(ekran, qizil, (mashina_x, mashina_y, mashina_width, mashina_height))

    # Yig'ishni ko'rsatish
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Yigish: {yigish}", True, oq)
    ekran.blit(score_text, (10, 10))

    pygame.display.flip()
    soat.tick(30)

pygame.quit()
sys.exit()
