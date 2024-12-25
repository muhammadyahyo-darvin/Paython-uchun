import random

# O'yin maydoni
class Game:
    def __init__(self):
        self.position = random.randint(0, 10)  # Tasodifiy boshlang'ich pozitsiya
        self.goal = 10  # Maqsad cho'qqi

    def get_neighbors(self):
        # Qo'shni pozitsiyalarni olish
        return [self.position - 1, self.position + 1]

    def move(self, new_position):
        self.position = new_position

    def score(self):
        # To'g'ri pozitsiyaning bahosi
        return abs(self.goal - self.position)

    def is_goal(self):
        return self.position == self.goal

# Asosiy o'yin funksiyasi
def hill_climbing():
    game = Game()
    print(f"Boshlang'ich pozitsiya: {game.position}")

    while not game.is_goal():
        neighbors = game.get_neighbors()
        # Eng yaxshi qo'shni pozitsiyani tanlash
        best_neighbor = min(neighbors, key=lambda x: game.score() if 0 <= x <= 10 else float('inf'))
        
        # Agar eng yaxshi qo'shni pozitsiya hozirgi pozitsiyadan yaxshi bo'lsa, harakat qilamiz
        if game.score() > abs(game.goal - best_neighbor):
            game.move(best_neighbor)
            print(f"Yangi pozitsiya: {game.position}")
        else:
            print("Yuqoriga harakat qilish mumkin emas!")
            break

    if game.is_goal():
        print("Tabriklaymiz! Siz maqsadga yetdingiz!")

# O'yinni ishga tushirish
if __name__ == "__main__":
    hill_climbing()
