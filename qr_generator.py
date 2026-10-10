import qrcode

URL = "https://google.com/"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("myqrcode.png")
print(f"QR code for {URL} saved as myqrcode.png")
