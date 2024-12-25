import datetime
import re
from twilio.rest import Client

class Register:
    def init(self, fullname, email, birthday, gender, phone, karta, tarifi, password):
        self.check_fullname(fullname)
        self.fullname = fullname

        if self.is_registered_email(email):
            raise Exception("Bu email ro'yhatdan o'tmagan!")

        self.check_email(email)
        self.email = email

        self.check_birthday(birthday)
        self.birthday = birthday

        self.check_gender(gender)
        self.gender = gender

        self.check_phone(phone)
        self.phone = phone

        self.check_karta(karta)
        self.karta = karta

        self.check_tarifi(tarifi)
        self.tarifi = tarifi

        self.check_password(password)
        self.password = password

        with open("Plastik_royhat.txt", "a+") as f:
            f.write(f"F.I.SH: {self.fullname}\n")
            f.write(f"Email: {self.email}\n")
            f.write(f"Tug'ilgan sana: {self.birthday}\n")
            f.write(f"Jinsi: {self.gender}\n")
            f.write(f"Telefon: {self.phone}\n")
            f.write(f"Karta raqami: {self.karta}\n")
            f.write(f"Kartani tarifi: {self.tarifi}\n")
            f.write(f"Parol: {self.password}\n\n")

        print("Sizning plastikingiz ro'yhatdan o'tdi.")
        
        self.send_sms(self.phone, "Siz ro'yhatdan o'tdingiz!")

    def is_registered_email(self, email):
        try:
            with open("Plastik_royhat.txt", "r") as f:
                registered_emails = [line.split(": ")[1].strip() for line in f.readlines() if line.startswith("Email:")]
                return email in registered_emails
        except FileNotFoundError:
            return False  

    def send_sms(self, phone_number, message):
        account_sid = 'YOUR_TWILIO_ACCOUNT_SID' 
        auth_token = 'YOUR_TWILIO_AUTH_TOKEN'    
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=message,
                from_='+1234567890',  # Twilio'dan olgan telefon raqamingiz
                to=phone_number
            )
            print(f"Xabar yuborildi: {message.sid}")
        except Exception as e:
            print(f"Xabar yuborishda xato yuz berdi: {e}")

    def check_fullname(self, name: str):
        if len(name.split()) != 4:
            raise Exception("F.I.SH yetarli emas")
        assert name.lower().endswith("o'g'li") or name.lower().endswith("qizi"), "F.I.SH format xato"

    def check_email(self, email):
        if type(email) != str:
            raise TypeError("Email satr bo'lishi kerak")
        if not self.is_valid_email(email):
            raise Exception("Email formati noto'g'ri.")
        assert "@" in email, "Email ichida @ belgisi yo'q"
        assert email.endswith(".com"), "Email .com bilan tugashi kerak"
        assert len(email[:email.find("@")]) > 5, "Email uzunligi kam"

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zAZ0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def check_birthday(self, date):
        date = date.split(".")
        assert len(date) == 3, "Tug'ilgan sana noto'g'ri formatda"
        try:
            new = datetime.datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]))
        except:
            raise Exception("Tug'ilgan sana noto'g'ri")
        else:
            today = datetime.datetime.now()
            age = (today - new).days // 365
            assert age >= 18, "Yoshingiz kichik ekan plastikdan ro'yhatga o'ta olmaysiz."

    def check_gender(self, gender):
        assert type(gender) == str, "Jins satr bo'lishi kerak"
        if gender.lower() not in ["male", "female"]:
            raise Exception("Jinsi bo'yicha xato")

    def check_phone(self, phone):
        assert type(phone) == str, "Telefon raqami harf bo'lmasligi kerak"
        assert phone.startswith("+998") and len(phone) == 13, "Telefon nomer xato"