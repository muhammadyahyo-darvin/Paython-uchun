import pygame
import sys

pygame.init()

# Ekran o'lchamlari
n, a = 800, 800
ekran = pygame.display.set_mode((n, a))
pygame.display.set_caption("Shashka O'yini")

# Ranglar
oq = (255, 255, 255)
qora = (0, 0, 0)
qizil = (255, 0, 0)
yashil = (0, 255, 0)

# Shashka disklarining parametrlar
disktik_radiyus = 40
disktik_qizil = (255, 0, 0)
disktik_qora = (0, 0, 0)

# O'yin maydonini yaratish
def draw_board():
    for y in range(8):
        for x in range(8):
            color = yashil if (x + y) % 2 == 0 else qora
            pygame.draw.rect(ekran, color, (x * 100, y * 100, 100, 100))

# Disklarni chizish
def draw_pieces():
    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 1:  # faqat qora maydonlarda disk bo'ladi
                if y < 3:
                    pygame.draw.circle(ekran, disktik_qora, (x * 100 + 50, y * 100 + 50), disktik_radiyus)
                elif y > 4:
                    pygame.draw.circle(ekran, disktik_qizil, (x * 100 + 50, y * 100 + 50), disktik_radiyus)

# O'yin holati
soat = pygame.time.Clock()
oyin_ishlamoqda = True
selected_piece = None
current_player = disktik_qizil

while oyin_ishlamoqda:
    for hodisa in pygame.event.get():
        if hodisa.type == pygame.QUIT:
            oyin_ishlamoqda = False

        if hodisa.type == pygame.MOUSEBUTTONDOWN:
            x, y = hodisa.pos
            grid_x, grid_y = x // 100, y // 100
            
            # Agar biron diskni tanlasak
            if selected_piece is None:
                # Diskni tanlash
                if (grid_x + grid_y) % 2 == 1:  # faqat qora maydonlarda disk bo'ladi
                    selected_piece = (grid_x, grid_y)
            else:
                # Harakatni amalga oshirish
                if (grid_x + grid_y) % 2 == 1:  # faqat qora maydonga harakat mumkin
                    selected_piece = None

    # Ekranni tozalash va qayta chizish
    ekran.fill(qora)  # Ekranni to'liq qora bilan to'ldirish
    draw_board()
    draw_pieces()

    pygame.display.flip()
    soat.tick(30)

pygame.quit()
sys.exit()
