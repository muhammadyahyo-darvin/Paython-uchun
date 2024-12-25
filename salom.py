import qrcode

a = input("Iltimos, havolani kiriting: ")

d = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

d.add_data(a)
d.make(fit=True)

b = d.make_image(fill='black', back_color='white')
b.show()