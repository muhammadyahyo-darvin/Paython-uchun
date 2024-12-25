# Kutubxona boshqaruv tizimi

class Kitob:
    def __init__(self, nomi, muallif, janr, narx):
        self.__nomi = nomi
        self.__muallif = muallif
        self.__janr = janr
        self.__narx = narx

    @property
    def nomi(self):
        return self.__nomi

    @property
    def muallif(self):
        return self.__muallif

    @property
    def janr(self):
        return self.__janr

    @property
    def narx(self):
        return self.__narx

    def __str__(self):
        return f"{self.nomi} - {self.muallif} ({self.janr}) : {self.narx} so'm"

class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def kitob_ochirish(self, nomi):
        self.kitoblar = [kitob for kitob in self.kitoblar if kitob.nomi != nomi]

    def kitob_qidirish(self, nomi):
        return next((kitob for kitob in self.kitoblar if kitob.nomi == nomi), None)

    def __str__(self):
        return "\n".join(str(kitob) for kitob in self.kitoblar)

class Foydalanuvchi:
    def __init__(self, ism):
        self.ism = ism
        self.qarzdagi_kitoblar = []

    def kitob_qarz_olish(self, kitob):
        self.qarzdagi_kitoblar.append(kitob)

    def kitob_qaytarish(self, kitob):
        self.qarzdagi_kitoblar.remove(kitob)

# 2. Shape class va voris classlar
class Shape:
    def draw(self):
        pass

class Line(Shape):
    def draw(self):
        return "*" * 25

class Triangle(Shape):
    def draw(self):
        result = ""
        for i in range(1, 6):
            result += " " * (5 - i) + "*" + (" " * (2 * i - 3) + "*" if i > 1 else "") + "\n"
        return result.strip()

class Rectangle(Shape):
    def draw(self):
        result = "*" * 10 + "\n"
        for _ in range(3):
            result += "*" + " " * 8 + "*\n"
        result += "*" * 10
        return result

class NullShape(Shape):
    def draw(self):
        return "Bo'sh shakl"

# 3. Telegram class
class Telegram:
    def __init__(self):
        self.user_name = ""
        self.accept_chat_text = ""
        self.chat_status = ""
        self.chat_time = ""

    def set_user(self, user_name):
        self.user_name = user_name

    def send(self, other, text):
        other.accept_chat_text = text
        other.chat_status = "sending"

    def read(self):
        self.chat_status = "reading"
        return self.accept_chat_text

    def delete(self):
        self.accept_chat_text = ""
        self.chat_status = "deleting"

# 4. Komanda class
class Komanda:
    def __init__(self, nomi, ishtirokchilar_soni, trener, kapitani):
        self.nomi = nomi
        self.ishtirokchilar_soni = ishtirokchilar_soni
        self.trener = trener
        self.kapitani = kapitani

    def __str__(self):
        return f"Komanda: {self.nomi}, Ishtirokchilar: {self.ishtirokchilar_soni}, Trener: {self.trener}, Kapitan: {self.kapitani}"

komandalar = [
    Komanda("Real Madrid", 25, "Anchelotti", "Modric"),
    Komanda("Barcelona", 24, "Xavi", "Lewandowski"),
    Komanda("Manchester City", 26, "Guardiola", "De Bruyne"),
    Komanda("PSG", 23, "Luis Enrique", "Mbappe"),
    Komanda("Bayern Munich", 25, "Tuchel", "Neuer")
]

def saralash_komanda(nomi):
    return next((komanda for komanda in komandalar if komanda.nomi == nomi), "Bunday komanda yo'q")

def komanda_bor_yoqligi(new_komanda):
    return next((komanda for komanda in komandalar if komanda.nomi == new_komanda), "Bunday komanda yo'q")

# QR kod uchun tasvir qo'shish
import qrcode
from PIL import Image

def tasvirli_qr_yaratish(link, tasvir_path, chiqish_fayli):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_kod = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    tasvir = Image.open(tasvir_path)
    tasvir = tasvir.resize((60, 60))

    qr_kod.paste(tasvir, (qr_kod.size[0] // 2 - 30, qr_kod.size[1] // 2 - 30))
    qr_kod.save(chiqish_fayli)

# Namuna ishlatish
# tasvirli_qr_yaratish("https://example.com", "logo.png", "qr_with_logo.png")
