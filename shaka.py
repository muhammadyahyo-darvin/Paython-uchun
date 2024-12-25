import pygame
import sys

# Pygame kutubxonasini ishga tushiramiz
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

# O'yinchilar
oyinchi_1 = disktik_qora
oyinchi_2 = disktik_qizil
current_player = oyinchi_1  # Boshlang'ich o'yinchi qora disk

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
                if y < 3:  # Qora disklar
                    pygame.draw.circle(ekran, disktik_qora, (x * 100 + 50, y * 100 + 50), disktik_radiyus)
                elif y > 4:  # Qizil disklar
                    pygame.draw.circle(ekran, disktik_qizil, (x * 100 + 50, y * 100 + 50), disktik_radiyus)

# O'yin holati
soat = pygame.time.Clock()
oyin_ishlamoqda = True
selected_piece = None
valid_moves = []
game_over = False

# Diskni tanlash
def select_piece(x, y):
    global selected_piece, valid_moves
    selected_piece = (x, y)
    valid_moves = []  # Yangi valid harakatlar ro'yxatini tozalash
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:  # Harakat qilish uchun mumkin bo'lgan yo'nalishlar
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and (nx + ny) % 2 == 1:  # Faqat qora maydonlar
            valid_moves.append((nx, ny))

# Diskni harakatlantirish
def move_piece(x, y):
    global selected_piece, current_player
    if selected_piece:
        sx, sy = selected_piece
        if (x, y) in valid_moves:  # Faqat valid harakatlar bo'yicha
            selected_piece = None
            return (x, y)  # Yangi pozitsiyani qaytaradi
    return selected_piece  # Agar noto'g'ri harakat bo'lsa, tanlangan diskni saqlash

# O'yin oynasi
while oyin_ishlamoqda:
    for hodisa in pygame.event.get():
        if hodisa.type == pygame.QUIT:
            oyin_ishlamoqda = False

        if hodisa.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = hodisa.pos
            grid_x, grid_y = x // 100, y // 100
            if selected_piece is None:
                # Agar diskni tanlash mumkin bo'lsa
                if (grid_x + grid_y) % 2 == 1 and (grid_y < 3 or grid_y > 4):  # Disk faqat tegishli maydonlarda
                    select_piece(grid_x, grid_y)
            else:
                # Harakat qilish
                new_position = move_piece(grid_x, grid_y)
                if new_position != selected_piece:
                    selected_piece = None
                    # Navbatni o'zgartirish
                    if current_player == disktik_qora:
                        current_player = disktik_qizil
                    else:
                        current_player = disktik_qora

    
    ekran.fill(qora)  
    draw_board()
    draw_pieces()

    pygame.display.flip()
    soat.tick(30)

pygame.quit()
sys.exit()
