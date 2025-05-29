import qrcode
from qrcode.constants import ERROR_CORRECT_L

url = "https://irma-warsaw-website-glow.lovable.app/"

qr = qrcode.QRCode(
    version=1,  
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("irma_qr_code.png")

print("QR code successfully generated and saved as 'irma_qr_code.png'.")

