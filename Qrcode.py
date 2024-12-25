import qrcode
from PIL import Image

def tasvirli_qr_yaratish(link, rasim_path, chiqish_fayli):
    # QR kod yaratish
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Tasvirni ochish
    rasim = Image.open(rasim_path)
    rasim = rasim.resize((60, 60))

    # Tasvirni QR kod markaziga qo'shish
    pos = (
        (qr_image.size[0] - rasim.size[0]) // 2,
        (qr_image.size[1] - rasim.size[1]) // 2
    )
    qr_image.paste(rasim, pos)

    # Chiqish faylini saqlash
    qr_image.save(chiqish_fayli)

# Namuna ishlatish
# tasvirli_qr_yaratish("https://example.com", "logo.png", "qr_with_image.png")
