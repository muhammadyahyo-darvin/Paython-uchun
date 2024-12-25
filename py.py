import pygame
import sys
import random

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
kulrang = (169, 169, 169)

# Mashina parametrlari
mashina_width = 60
mashina_height = 120
mashina_x = n // 2 - mashina_width // 2
mashina_y = a - mashina_height - 10
tezlik = 10

# Yoldan tushayotgan mashinalar
yol_mashinalari = []
yol_mashina_width = 60
yol_mashina_height = 120
yol_mashina_tezlik = 5

# O'yin holati
soat = pygame.time.Clock()
oyin_ishlamoqda = True
yigish = 0

# Mashina va yoldan mashinalarni harakatlantirish
def move_road_cars():
    global yol_mashinalari, yigish
    for mashina in yol_mashinalari:
        mashina[1] += yol_mashina_tezlik  # Yoldan mashina pastga harakatlanadi
        if mashina[1] > a:
            yol_mashinalari.remove(mashina)  # Agar mashina pastga yetib borsa, uni olib tashlaymiz
            yigish += 1  # Har bir mashina o'tganda yig'ish o'sadi

# Yoldan mashinalar yaratish
def create_road_cars():
    if random.randint(1, 60) == 1:  # Har 60-chi siklda yangi mashina yaratish
        x_pos = random.randint(0, n - yol_mashina_width)
        yol_mashinalari.append([x_pos, -yol_mashina_height])  # Yangi mashina yuqoridan tushadi

# O'yinni tekshirish (to'qnashuvni aniqlash)
def check_collision():
    for mashina in yol_mashinalari:
        if mashina[1] + yol_mashina_height > mashina_y and mashina[1] < mashina_y + mashina_height:
            if mashina[0] < mashina_x + mashina_width and mashina[0] + yol_mashina_width > mashina_x:
                return True
    return False

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

    # Yangi mashinalar yaratish va ularni harakatlantirish
    create_road_cars()
    move_road_cars()

    # To'qnashuvni tekshirish
    if check_collision():
        print("O'yin tugadi!")
        oyin_ishlamoqda = False

    # Ekranni tozalash va yangi rasm chizish
    ekran.fill(kulrang)  # Ekranni to'liq kulrang bilan to'ldirish (yo'l rangi)

    # Yoldan tushayotgan mashinalarni chizish
    for mashina in yol_mashinalari:
        pygame.draw.rect(ekran, qizil, (mashina[0], mashina[1], yol_mashina_width, yol_mashina_height))

    # O'yinchining mashinasini chizish
    pygame.draw.rect(ekran, oq, (mashina_x, mashina_y, mashina_width, mashina_height))

    # Yig'ishni ko'rsatish
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Yigish: {yigish}", True, qora)
    ekran.blit(score_text, (10, 10))

    pygame.display.flip()
    soat.tick(30)

pygame.quit()
sys.exit()
